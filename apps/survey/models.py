import os
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage import StdImageField

from config.constants import SEX_CHOICES, INCOME_CHOICES, PURPOSE_CHOICES, SURVEY_LEVEL_CHOICES, SURVEY_STATUS_CHOICES
from config.settings import ANSWER_PHOTO_FOLDER


def get_answer_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = instance.name_en + '_' if instance.name_en else ''
    filename = '%s%s' % (filename, instance.name_en)
    filename = filename.replace(' ', '-')
    filename = '%s.%s' % (filename, ext)
    file_path = os.path.join(ANSWER_PHOTO_FOLDER, filename)

    return file_path


class AnswerManager(models.Manager):
    def filled(self):
        return self.exclude(status='CREATED')

    def created(self):
        return self.filter(status='CREATED')


class Answer(models.Model):
    """问卷报告回答,answer"""
    customer = models.ForeignKey('customer.Customer', null=True, blank=True)
    uuid = models.CharField('uuid', max_length=255, blank=True, unique=True)
    # purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    # level = models.CharField(max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 9.9 or 98
    city = models.CharField(_(u'城市'), max_length=255, blank=True)  # 自动抓取地址

    # replica of customer basic info
    name = models.CharField(_(u'1. 您的姓名？'), max_length=64, null=True, blank=True, help_text='提示：请填写您下单时登记的姓名')
    sex = models.CharField(_(u'2. 您的性别？'), choices=SEX_CHOICES, max_length=30, null=True, blank=True, help_text='')
    portrait = StdImageField(_('3. 无PS、无滤镜、清晰纯素颜照片一张'), upload_to=get_answer_photo_path, blank=True, null=True,
                             variations={
                                 'medium': (1000, 1000, True),
                                 'thumbnail': (400, 400, True)
                             }, help_text='提示：上传文件不超过4M')
    portrait_part = StdImageField(_('4. 如需重点关注部位可在此上传无PS、无滤镜、清晰的纯素颜照片'), upload_to=get_answer_photo_path, blank=True,
                                  null=True,
                                  variations={
                                      'medium': (1000, 1000, True),
                                      'thumbnail': (400, 400, True)
                                  }, help_text='提示：上传文件不超过4M')
    cosmetics = StdImageField(_('5. 现阶段使用护肤品合集'), upload_to=get_answer_photo_path, blank=True, null=True,
                              variations={
                                  'medium': (1000, 1000, True),
                                  'thumbnail': (400, 400, True)
                              }, help_text='提示：上传文件不超过4M')
    birth = models.DateField(_(u'6. 您的出生日期？'), null=True, blank=True, help_text='提示：格式：2017-01-01')
    height = models.PositiveIntegerField(_(u'7. 您的身高'), null=True, blank=True)
    weight = models.PositiveIntegerField(_(u'体重'), null=True, blank=True)
    job = models.CharField(_(u'8. 您目前从事的职业?'), max_length=64, blank=True)
    monthly_income = models.CharField(_(u'9. 月收入水平？'), choices=INCOME_CHOICES, max_length=50, blank=True)
    weixin_id = models.CharField(_(u'10. 您的微信号？'), max_length=128, blank=True, help_text='提示：微信号不是昵称')
    mobile = models.CharField(_(u'11. 您的手机号？'), max_length=15, blank=True)

    # 记分选择题
    # 12-21 是干油
    question1 = models.PositiveIntegerField('12. 在照片上，你的皮肤看起来油光发亮？', blank=True, null=True)  # No. 12
    question2 = models.PositiveIntegerField('13. 在干燥的环境中，如果不使用面霜. 乳液或者防晒霜，你的面部皮肤会？', blank=True, null=True)  # No. 13
    question3 = models.PositiveIntegerField('14. 使用面霜或乳液后2-3小时你的面部会？', blank=True, null=True)  # No. 14
    question4 = models.PositiveIntegerField('15. 早上正常护肤后，中午到下午会大量出油？', blank=True, null=True)  # No. 15
    question5 = models.PositiveIntegerField('16. 在使用粉底液. BB霜或者隔离霜，但不涂粉饼或散粉的情况下，2~3小时后，你的妆容会？', blank=True,
                                            null=True)  # No. 16
    question6 = models.PositiveIntegerField('17. 你的脸部哪些部位有毛孔粗大问题？ ', blank=True, null=True)  # No. 17
    question7 = models.PositiveIntegerField('18. 你会怎样描述你的脸部肌肤的干油性？', blank=True, null=True)  # No. 18
    question8 = models.PositiveIntegerField('19. 当你使用肥皂泡沫. 泡沫乳. 泡沫丰富的洁面产品洁面时，你的面部皮肤会？', blank=True, null=True)  # No. 19
    question9 = models.PositiveIntegerField('20. 在当前季节里，如果不使用面霜或乳液，你的脸部会？', blank=True, null=True)  # No. 20
    question10 = models.PositiveIntegerField('21. 你会长粉刺. 闭口或痘痘等吗？', blank=True, null=True)  # No. 21
    # 22-32 是敏感
    question11 = models.PositiveIntegerField('22. 你的面部会出现泛红的情况（点状或片状）吗？', blank=True, null=True,
                                             help_text='提示：不是痘印')  # No. 22
    question12 = models.PositiveIntegerField('23. 护肤产品（包括洁面产品. 水. 精华. 乳液/面霜等）会使你的面部出现发红. 发痒. 刺痛. 灼热的感觉吗？', blank=True,
                                             null=True)  # No. 23
    question13 = models.PositiveIntegerField('24. 你曾经被诊断过有痤疮. 玫瑰痤疮. 遗传性皮炎. 湿疹. 接触性皮炎吗？', blank=True,
                                             null=True)  # No. 24
    question14 = models.PositiveIntegerField('25. 你会对金属首饰过敏吗？', blank=True, null=True)  # No. 25
    question15 = models.PositiveIntegerField('26. 你喝酒后经常脸红吗？', blank=True, null=True)  # No. 26
    question16 = models.PositiveIntegerField('27. 防晒产品会使你的皮肤过敏（发红. 发痒. 刺痛. 灼热. 起疹子的感觉）吗？', blank=True,
                                             null=True)  # No. 27
    question17 = models.PositiveIntegerField('28. 你的直系亲属中有几位被诊断为过敏体质（如：遗传过敏性皮炎. 湿疹. 哮喘. 过敏症）？', blank=True,
                                             null=True)  # No. 28
    question18 = models.PositiveIntegerField('29. 如果皮肤接触含香味的洗衣剂或柔顺剂，你会出现什么反应？', blank=True, null=True)  # No. 29
    question19 = models.PositiveIntegerField('30. 在长时间运动后，或情绪波动较大的情况下，你的脸部或颈部会变红吗？', blank=True, null=True)  # No. 30
    question20 = models.PositiveIntegerField('31. 你在吃完辣的或是烫的食物后皮肤会发红吗？', blank=True, null=True)  # No. 31
    question21 = models.PositiveIntegerField('32. 你脸上哪些部位有红血丝？', blank=True, null=True,
                                             help_text='提示：成片的红血丝或根根分明的红血丝')  # No. 32
    # 33-41 是色素
    question22 = models.PositiveIntegerField('33. 在你长粉刺. 闭口. 痘痘之后，愈合处会出现棕色或黑色的印吗？', blank=True, null=True)  # No. 33
    question23 = models.PositiveIntegerField('34. 皮肤划伤后，愈合后的深色（不是粉色）痕迹会保持多久？', blank=True, null=True)  # No. 34
    question24 = models.PositiveIntegerField('35. 如果几个月没被长时间（2小时以上）日晒过，当你第一次被长时间日晒时，你的皮肤会变黑变暗吗？', blank=True,
                                             null=True)  # No. 35
    question25 = models.PositiveIntegerField('36. 你是否被诊断过脸上有斑（表现为浅褐色. 深褐色或灰色斑）？', blank=True, null=True)  # No. 36
    question26 = models.PositiveIntegerField('37. 当你在太阳下长时间日晒（2小时以上）后，你脸上的斑点会变得更明显吗？', blank=True, null=True)  # No. 37
    question27 = models.PositiveIntegerField('38. 你的脸上. 胸上. 背部或胳膊上，是否有或者曾经有过斑点？', blank=True, null=True)  # No. 38
    question28 = models.PositiveIntegerField('39. 连续长时间日晒（2小时以上）几天后，你的皮肤会出现下列哪种情况？', blank=True, null=True)  # No. 39
    question29 = models.PositiveIntegerField('40. 在你的面部有斑（点状或片状都算）吗？', blank=True, null=True)  # No. 40
    question30 = models.PositiveIntegerField('41. 你头发的自然色是？', blank=True, null=True)  # No. 41
    # 42-49 是皱纹
    question31 = models.PositiveIntegerField('42. 你的脸上有皱纹吗？', blank=True, null=True)  # No. 42
    question32 = models.PositiveIntegerField('43. 日常生活中，你曾经在每年或不到一年中经历过多于两周的长时间日晒（2小时以上）吗？（包括暑假在内）如果是，多长时间一次？',
                                             blank=True, null=True)  # No. 43
    question33 = models.PositiveIntegerField('44. 你认为自己看上去有多大年龄？', blank=True, null=True)  # No. 44
    question34 = models.PositiveIntegerField('45. 过去五年里，你有意或者无意通过户外活动或者其他方式晒黑，大概多久一次？', blank=True, null=True)  # No. 45
    question35 = models.PositiveIntegerField('46. 根据你所居住的地方，你每天受日照的时间是多少？', blank=True, null=True)  # No. 46
    question36 = models.PositiveIntegerField('47. 在你的生活中，你共抽过多少烟（或者二手烟）？', blank=True, null=True)  # No. 47
    question37 = models.PositiveIntegerField('48. 请描述你居住地的空气污染状况：', blank=True, null=True)  # No. 48
    question38 = models.PositiveIntegerField('49. 你的母亲面部皮肤年龄看上去多大？', blank=True, null=True)  # No. 49

    # 不记分选择题 50-64
    non_score_question1 = models.CharField('50. 排便是否正常?', blank=True, max_length=255)  # No. 50
    non_score_question2 = models.CharField('51. 洁面', blank=True, max_length=255)  # No. 51
    non_score_question3 = models.CharField('52. 化妆水', blank=True, max_length=255)  # No. 52
    non_score_question4 = models.CharField('53. 精华', blank=True, max_length=255)  # No. 53
    non_score_question5 = models.CharField('54. 乳液或面霜', blank=True, max_length=255)  # No. 54
    non_score_question6 = models.CharField('55. 防晒', blank=True, max_length=255)  # No. 55
    non_score_question7 = models.CharField('56. 卸妆', blank=True, max_length=255)  # No. 56
    non_score_question8 = models.CharField('57. 洁面', blank=True, max_length=255)  # No. 57
    non_score_question9 = models.CharField('58. 化妆水', blank=True, max_length=255)  # No. 58
    non_score_question10 = models.CharField('59. 精华', blank=True, max_length=255)  # No. 59
    non_score_question11 = models.CharField('60. 乳液或面霜', blank=True, max_length=255)  # No. 60
    non_score_question12 = models.CharField('61. 面膜（非清洁类面膜）', blank=True, max_length=255)  # No. 61
    non_score_question13 = models.CharField('62. 去角质清洁面膜（去角质啫喱，泥面膜或其它清洁面膜）的频次', blank=True, max_length=255)  # No. 62
    non_score_question14 = models.CharField('63. 您是否去有定期去美容院或医美机构做皮肤护理的习惯？', blank=True, max_length=255)  # No. 63
    non_score_question15 = models.TextField('64. 近半年内您是否有出现过严重的皮肤问题(例如：大面积的痤疮. 湿疹. 皮肤过敏),请详细描述具体情况：', blank=True,
                                            max_length=255, help_text='提示：如没有，请留空')  # No. 64

    # 非选项问题 65-72
    cosmetic_question1 = models.TextField('65. 目前正在使用的卸妆类的护肤品名)：', blank=True, max_length=255)  # No. 65
    cosmetic_question2 = models.TextField('66、目前正在使用的洁面乳/洁面霜/洁面油类的护肤品名称', blank=True, max_length=255)  # No. 66
    cosmetic_question3 = models.TextField('67、目前正在所使用化妆水类护肤品名称', blank=True, max_length=255)  # No. 67
    cosmetic_question4 = models.TextField('68、目前正在所使用乳液／面霜类护肤品名称', blank=True, max_length=255)  # No. 68
    cosmetic_question5 = models.TextField('69、目前正在使用的精华类的护肤品名称', blank=True, max_length=255)  # No. 69
    cosmetic_question6 = models.TextField('70、目前正在使用的去角质类的护肤品名称', blank=True, max_length=255)  # No. 70
    cosmetic_question7 = models.TextField('71、目前正在使用的的面膜类的护肤品名称', blank=True, max_length=255)  # No. 71
    cosmetic_question8 = models.TextField('72、目前正在使用的防晒类的护肤品名称', blank=True, max_length=255)  # No. 72

    other_question1 = models.TextField('73、您是否每天（一年四季，不管晴天、阴天、雨天，室内室外）涂抹足量（面部一元硬币大小）专门的防晒产品（不包括隔离霜，底妆）？', blank=True,
                                       max_length=255)  # No. 73
    other_question2 = models.TextField('74、您使用哪些成分或护肤品会过敏？如果有请描述过敏的现象。', blank=True, max_length=255,
                                       help_text='提示：如没有，请留空')  # No. 74

    status = models.CharField(u'状态', choices=SURVEY_STATUS_CHOICES, blank=False, max_length=32, default='CREATED')
    is_changeable = models.BooleanField(u'是否可修改', default=True, blank=False)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

    objects = AnswerManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)

    def get_oily_score(self):
        return sum([self.question1, self.question2, self.question3, self.question4, self.question5, self.question6,
                    self.question7, self.question8, self.question9, self.question10])

    def get_sensitive_score(self):
        return sum([self.question11, self.question12, self.question13, self.question14, self.question15,
                    self.question16, self.question17, self.question18, self.question19, self.question20,
                    self.question21])

    def get_pigment_score(self):
        return sum([self.question22, self.question23, self.question24, self.question25, self.question26,
                    self.question27, self.question28, self.question29, self.question30])

    def get_loose_score(self):
        return sum([self.question31, self.question32, self.question33, self.question34, self.question35,
                    self.question36, self.question37, self.question38])
