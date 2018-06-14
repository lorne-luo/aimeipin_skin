import os
import threading

import logging
from django.conf import settings
from django.db import models
from django.http import Http404
from django.template.loader import get_template
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from weasyprint import HTML

from apps.analysis.models import SkinType, Word
from config.constants import PURPOSE_CHOICES, PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, SURVEY_LEVEL_CHOICES

log = logging.getLogger(__name__)


class Report(models.Model):
    """问卷报告结果, user_content,user_content_word"""
    answer = models.ForeignKey('survey.Answer', null=False, blank=False, verbose_name='调查问卷')
    purpose = models.CharField('目标', max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    level = models.CharField('价位', max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 价位

    # 肤质4个维度种类
    oily_type = models.ForeignKey('analysis.SkinType', verbose_name=_('油性or干性'), blank=True, null=True,
                                  related_name='report_oily_type')
    sensitive_type = models.ForeignKey('analysis.SkinType', verbose_name=_('敏感or耐受'), blank=True, null=True,
                                       related_name='report_sensitive_type')
    pigment_type = models.ForeignKey('analysis.SkinType', verbose_name=_('色素or非色素'), blank=True, null=True,
                                     related_name='report_pigment_type')
    loose_type = models.ForeignKey('analysis.SkinType', verbose_name=_('易皱纹or紧致'), blank=True, null=True,
                                   related_name='report_loose_type')

    # 肤质4个维度的测试评分
    oily_score = models.PositiveIntegerField('油干分数', blank=True, null=True)
    sensitive_score = models.PositiveIntegerField('敏感耐受分数', blank=True, null=True)
    pigment_score = models.PositiveIntegerField('色素分数', blank=True, null=True)
    loose_score = models.PositiveIntegerField('易皱纹紧致分数', blank=True, null=True)

    summary = models.TextField('总结', blank=True)  # 报告总结
    problem = models.TextField('2. 我们认为您存在的问题', blank=True)  # 存在的问题
    avoid_component = models.TextField('4) 需要避免使用的皮肤护理成分', blank=True)  # 避免使用的成分
    doctor_advice = models.TextField('三、听听皮肤科医生怎么说', blank=True)  # 医生建议
    day_instruct = models.TextField('日间', blank=True)  # 日间指导
    night_instruct = models.TextField('夜间', blank=True)  # 夜间指导
    mask_instruct = models.TextField('面膜', blank=True)  # 面膜指导
    emergency_solution = models.TextField('应急方案', blank=True)  # 应急方案
    maintain_solution = models.TextField('日常维稳方案', blank=True)  # 维稳方案
    allergy = models.TextField('过敏', blank=True)  # 过敏, answer.other_question2
    remark = models.TextField('温馨提示', blank=True)  # 温馨提示, for 9.9

    pdf = models.FileField('PDF', blank=True)
    pdf_created_at = models.DateTimeField('PDF生成时间', null=True, blank=True)

    modified_at = models.DateTimeField('最后更新', auto_now=True, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    def classify_skin_type(self):
        self.oily_score = self.answer.oily_score
        self.sensitive_score = self.answer.sensitive_score
        self.pigment_score = self.answer.pigment_score
        self.loose_score = self.answer.loose_score

        self.oily_type = SkinType.get_oily_type(self.oily_score)
        self.sensitive_type = SkinType.get_sensitive_type(self.sensitive_score)
        self.pigment_type = SkinType.get_pigment_type(self.pigment_score)
        self.loose_type = SkinType.get_loose_type(self.loose_score)

    def get_update_fields(self):
        # exclude `pdf` and `pdf_created_at` which should updated by background thread
        if self.id:
            l = [f.name for f in self._meta.fields]
            l.remove('id')
            l.remove('pdf')
            l.remove('pdf_created_at')
            return l
        return None

    def save(self, *args, **kwargs):
        if 'update_fields' not in kwargs:
            self.classify_skin_type()
            self.start_pdf_generation()
            kwargs['update_fields'] = self.get_update_fields()
        super(Report, self).save(*args, **kwargs)

    def start_pdf_generation(self):
        def generate_pdf(id):
            log.info('[PDF GENERATION] #%s Started' % id)
            report = Report.objects.filter(id=id).first()
            if report:
                context = {'object': report}
                template_name = 'report/report_download2_%s.html' % report.level
                template = get_template(template_name)
                html = template.render(context)

                url = '%s/%s.pdf' % (settings.REPORT_PDF_FOLDER, report.uuid)
                file_path = os.path.join(settings.MEDIA_ROOT, url)
                pdf = HTML(string=html).write_pdf(file_path)
                report.pdf_created_at = timezone.now()
                report.pdf = url
                report.save(update_fields=['pdf', 'pdf_created_at'])
                log.info('[PDF GENERATION] #%s Finished' % id)

        t = threading.Thread(target=generate_pdf,
                             args=(self.id,))
        t.setDaemon(True)
        t.start()

    @property
    def uuid(self):
        if self.answer:
            return self.answer.uuid
        return None

    def get_word(self):
        return Word.objects.filter(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=self.sensitive_type,
                                   pigment_type=self.pigment_type, loose_type=self.loose_type).first()

    def generate(self):
        if not self.answer:
            raise Http404
        self.classify_skin_type()
        self.allergy = self.answer.other_question2

        word = self.get_word()
        if word:
            self.summary = word.report
            self.problem = word.problem
            self.avoid_component = word.avoid_component
            self.doctor_advice = word.doctor_advice
            self.emergency_solution = word.emergency_solution
            self.maintain_solution = word.maintain_solution
            self.day_instruct = word.day_instruct
            self.night_instruct = word.night_instruct
            self.mask_instruct = word.mask_instruct

        for ap in self.answer.answerproduct_set.all():
            ap.update_analysis(True)

        self.save()

    def __str__(self):
        return '%s %s#%s' % (self.answer.name, self.purpose, self.level)

    @property
    def day_premiumproducts(self):
        return self.reportpremiumproduct_set.filter(type='日间')

    @property
    def night_premiumproducts(self):
        return self.reportpremiumproduct_set.filter(type='夜间')

    @property
    def mask_premiumproducts(self):
        return self.reportpremiumproduct_set.filter(type='面膜')


class ReportProductAnalysis(models.Model):
    '''用户使用产品的分析 user_product_txt'''
    report = models.ForeignKey(Report, null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)  # 产品外键或名称
    name = models.CharField('名称', max_length=512, blank=True)
    analysis = models.TextField('分析', blank=True)  # 护肤品分析


class ReportPremiumProduct(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)

    def __str__(self):
        return '%s @ %s %s' % (self.product, self.report, self.type)
