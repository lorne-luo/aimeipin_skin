import os
import threading

import logging
from django.conf import settings
from django.db import models
from django.db.models import Q
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

    is_delivered = models.BooleanField(default=False)  # 用户是否关注公众账号
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
            self._analysis_product()
        super(Report, self).save(*args, **kwargs)

    def start_pdf_generation(self):
        self.generate_pdf()
        # self.pdf = None
        # self.pdf_created_at = None
        # self.save(update_fields=['pdf', 'pdf_created_at'])
        # t = threading.Thread(target=self.generate_pdf, args=())
        # t.setDaemon(True)
        # t.start()

    def generate_pdf(self):
        context = {'object': self, 'BASE_URL': settings.BASE_URL}
        template_name = 'report/report_download_%s.html' % self.level
        template = get_template(template_name)
        html = template.render(context)

        url = '%s/%s.pdf' % (settings.REPORT_PDF_FOLDER, self.uuid)
        file_path = os.path.join(settings.MEDIA_ROOT, url)
        pdf = HTML(string=html).write_pdf(file_path)
        self.pdf_created_at = timezone.now()
        self.pdf = url
        self.save(update_fields=['pdf', 'pdf_created_at'])
        log.info('[PDF GENERATION] #%s Finished' % id)
        return file_path

    @property
    def uuid(self):
        if self.answer:
            return self.answer.uuid
        return None

    def get_words(self):

        words = Word.objects.filter(
            # demension 1
            Q(purpose=self.purpose, oily_type=None, sensitive_type=None, pigment_type=None, loose_type=None) |
            Q(purpose='', oily_type=self.oily_type, sensitive_type=None, pigment_type=None, loose_type=None) |
            Q(purpose='', oily_type=None, sensitive_type=self.sensitive_type, pigment_type=None, loose_type=None) |
            Q(purpose='', oily_type=None, sensitive_type=None, pigment_type=self.pigment_type, loose_type=None) |
            Q(purpose='', oily_type=None, sensitive_type=None, pigment_type=None, loose_type=self.loose_type) |
            # demension 2
            Q(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=None, pigment_type=None, loose_type=None) |
            Q(purpose=self.purpose, oily_type=None, sensitive_type=self.sensitive_type, pigment_type=None,
              loose_type=None) |
            Q(purpose=self.purpose, oily_type=None, sensitive_type=None, pigment_type=self.pigment_type,
              loose_type=None) |
            Q(purpose=self.purpose, oily_type=None, sensitive_type=None, pigment_type=None,
              loose_type=self.loose_type) |
            Q(purpose='', oily_type=self.oily_type, sensitive_type=self.sensitive_type, pigment_type=None,
              loose_type=None) |
            Q(purpose='', oily_type=self.oily_type, sensitive_type=None, pigment_type=self.pigment_type,
              loose_type=None) |
            Q(purpose='', oily_type=self.oily_type, sensitive_type=None, pigment_type=None,
              loose_type=self.loose_type) |
            Q(purpose='', oily_type=None, sensitive_type=self.sensitive_type, pigment_type=self.pigment_type,
              loose_type=None) |
            Q(purpose='', oily_type=None, sensitive_type=self.sensitive_type, pigment_type=None,
              loose_type=self.loose_type) |
            Q(purpose='', oily_type=None, sensitive_type=None, pigment_type=self.pigment_type,
              loose_type=self.loose_type) |
            # demension 3
            Q(purpose='', oily_type=self.oily_type, sensitive_type=self.sensitive_type,
              pigment_type=self.pigment_type, loose_type=self.loose_type) |
            Q(purpose=self.purpose, oily_type=None, sensitive_type=self.sensitive_type,
              pigment_type=self.pigment_type, loose_type=self.loose_type) |
            Q(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=None,
              pigment_type=self.pigment_type, loose_type=self.loose_type) |
            Q(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=self.sensitive_type,
              pigment_type=None, loose_type=self.loose_type) |
            Q(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=self.sensitive_type,
              pigment_type=self.pigment_type, loose_type=None) |
            # fully match
            Q(purpose=self.purpose, oily_type=self.oily_type, sensitive_type=self.sensitive_type,
              pigment_type=self.pigment_type, loose_type=self.loose_type)
        )
        return words

    def generate(self):
        if not self.answer:
            raise Http404
        self.classify_skin_type()
        self.allergy = self.answer.other_question2

        self.clear_word()
        words = self.get_words()
        for word in words:
            self.summary += word.report + '\n'
            self.problem += word.problem + '\n'
            self.avoid_component += word.avoid_component + '\n'
            self.doctor_advice += word.doctor_advice + '\n'
            self.emergency_solution += word.emergency_solution + '\n'
            self.maintain_solution += word.maintain_solution + '\n'
            self.day_instruct += word.day_instruct + '\n'
            self.night_instruct += word.night_instruct + '\n'
            self.mask_instruct += word.mask_instruct + '\n'

        self._analysis_product(True)

        self.save()

    def clear_word(self):
        self.summary = ''
        self.problem = ''
        self.avoid_component = ''
        self.doctor_advice = ''
        self.emergency_solution = ''
        self.maintain_solution = ''
        self.day_instruct = ''
        self.night_instruct = ''
        self.mask_instruct = ''

    def _analysis_product(self, force_update=False):
        if self.answer:
            for ap in self.answer.answerproduct_set.all():
                ap.update_analysis(force_update)

    def regenerate(self):
        if not self.answer:
            return

        self.classify_skin_type()
        self.allergy = self.answer.other_question2
        for ap in self.answer.answerproduct_set.all():
            ap.update_analysis(False)

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


class ReportPremiumProduct(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)

    def __str__(self):
        return '%s @ %s %s' % (self.product, self.report, self.type)
