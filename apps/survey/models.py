from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.constants import SEX_CHOICES, INCOME_CHOICES, PURPOSE_CHOICES, SKIN_OILY_TYPE_CHOICES, \
    SKIN_SENSITIVE_TYPE_CHOICES, SKIN_PIGMENT_TYPE_CHOICES, SKIN_LOOSE_TYPE_CHOICES, \
    PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, \
    SURVEY_LEVEL_CHOICES


class Answer(models.Model):
    """问卷报告回答,answer"""
    customer = models.ForeignKey('customer.Customer', null=False, blank=False)
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    level = models.CharField(max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 9.9 or 98

    # replica of customer basic info
    address = models.CharField(_(u'地址'), max_length=255, blank=True) # 自动抓取地址
    name = models.CharField(_(u'1. 您的姓名？'), max_length=64, null=False, blank=False, help_text='')
    sex = models.CharField(_(u'2. 您的性别？'), choices=SEX_CHOICES, max_length=30, null=False, blank=False,help_text='')
    birth = models.DateTimeField(_(u'6. 您的出生日期？'), null=False, blank=False,help_text='')
    height = models.PositiveIntegerField(_(u'7. 您的身高'), null=False, blank=False)
    weight = models.PositiveIntegerField(_(u'体重'), null=False, blank=False)
    job = models.CharField(_(u'8. 您目前从事的职业?'), max_length=64, blank=False)
    monthly_income = models.CharField(_(u'9. 月收入水平？'), choices=INCOME_CHOICES, max_length=50, blank=False)
    weixin_id = models.CharField(_(u'10. 您的微信号？'), max_length=128, blank=False, help_text='提示：微信号不是昵称')
    mobile = models.CharField(_(u'11. 您的手机号？'), max_length=15, blank=False)

    # 记分选择题
    # 12-21 是干油
    question1 = models.PositiveIntegerField('12. 在照片上，你的皮肤看起来油光发亮？', blank=False, null=False)  # No. 12
    question2 = models.PositiveIntegerField('13. 在干燥的环境中，如果不使用面霜. 乳液或者防晒霜，你的面部皮肤会？',blank=False, null=False)  # No. 13
    question3 = models.PositiveIntegerField('14. 使用面霜或乳液后2-3小时你的面部会？',blank=False, null=False)  # No. 14
    question4 = models.PositiveIntegerField('15. 早上正常护肤后，中午到下午会大量出油？',blank=False, null=False)  # No. 15
    question5 = models.PositiveIntegerField('16. 在使用粉底液. BB霜或者隔离霜，但不涂粉饼或散粉的情况下，2~3小时后，你的妆容会？',blank=False, null=False)  # No. 16
    question6 = models.PositiveIntegerField('17. 你的脸部哪些部位有毛孔粗大问题？ ',blank=False, null=False)  # No. 17
    question7 = models.PositiveIntegerField('18. 你会怎样描述你的脸部肌肤的干油性？',blank=False, null=False)  # No. 18
    question8 = models.PositiveIntegerField('19. 当你使用肥皂泡沫. 泡沫乳. 泡沫丰富的洁面产品洁面时，你的面部皮肤会？',blank=False, null=False)  # No. 19
    question9 = models.PositiveIntegerField('20. 在当前季节里，如果不使用面霜或乳液，你的脸部会？',blank=False, null=False)  # No. 20
    question10 = models.PositiveIntegerField('21. 你会长粉刺. 闭口或痘痘等吗？',blank=False, null=False)  # No. 21
    # 22-32 是敏感
    question11 = models.PositiveIntegerField('22. 你的面部会出现泛红的情况（点状或片状）吗？',blank=False, null=False)  # No. 22
    question12 = models.PositiveIntegerField('23. 护肤产品（包括洁面产品. 水. 精华. 乳液/面霜等）会使你的面部出现发红. 发痒. 刺痛. 灼热的感觉吗？',blank=False, null=False)  # No. 23
    question13 = models.PositiveIntegerField('24. 你曾经被诊断过有痤疮. 玫瑰痤疮. 遗传性皮炎. 湿疹. 接触性皮炎吗？',blank=False, null=False)  # No. 24
    question14 = models.PositiveIntegerField('25. 你会对金属首饰过敏吗？',blank=False, null=False)  # No. 25
    question15 = models.PositiveIntegerField('26. 你喝酒后经常脸红吗？',blank=False, null=False)  # No. 26
    question16 = models.PositiveIntegerField('27. 防晒产品会使你的皮肤过敏（发红. 发痒. 刺痛. 灼热. 起疹子的感觉）吗？',blank=False, null=False)  # No. 27
    question17 = models.PositiveIntegerField('28. 你的直系亲属中有几位被诊断为过敏体质（如：遗传过敏性皮炎. 湿疹. 哮喘. 过敏症）？',blank=False, null=False)  # No. 28
    question18 = models.PositiveIntegerField('29. 如果皮肤接触含香味的洗衣剂或柔顺剂，你会出现什么反应？',blank=False, null=False)  # No. 29
    question19 = models.PositiveIntegerField('30. 在长时间运动后，或情绪波动较大的情况下，你的脸部或颈部会变红吗？',blank=False, null=False)  # No. 30
    question20 = models.PositiveIntegerField('31. 你在吃完辣的或是烫的食物后皮肤会发红吗？',blank=False, null=False)  # No. 31
    question21 = models.PositiveIntegerField('32. 你脸上哪些部位有红血丝？',blank=False, null=False)  # No. 32
    # 33-41 是色素
    question22 = models.PositiveIntegerField('33. 在你长粉刺. 闭口. 痘痘之后，愈合处会出现棕色或黑色的印吗？',blank=False, null=False)  # No. 33
    question23 = models.PositiveIntegerField('34. 皮肤划伤后，愈合后的深色（不是粉色）痕迹会保持多久？',blank=False, null=False)  # No. 34
    question24 = models.PositiveIntegerField('35. 如果几个月没被长时间（2小时以上）日晒过，当你第一次被长时间日晒时，你的皮肤会变黑变暗吗？',blank=False, null=False)  # No. 35
    question25 = models.PositiveIntegerField('36. 你是否被诊断过脸上有斑（表现为浅褐色. 深褐色或灰色斑）？',blank=False, null=False)  # No. 36
    question26 = models.PositiveIntegerField('37. 当你在太阳下长时间日晒（2小时以上）后，你脸上的斑点会变得更明显吗？',blank=False, null=False)  # No. 37
    question27 = models.PositiveIntegerField('38. 你的脸上. 胸上. 背部或胳膊上，是否有或者曾经有过斑点？',blank=False, null=False)  # No. 38
    question28 = models.PositiveIntegerField('39. 连续长时间日晒（2小时以上）几天后，你的皮肤会出现下列哪种情况？',blank=False, null=False)  # No. 39
    question29 = models.PositiveIntegerField('40. 在你的面部有斑（点状或片状都算）吗？',blank=False, null=False)  # No. 40
    question30 = models.PositiveIntegerField('41. 你头发的自然色是？',blank=False, null=False)  # No. 41
    # 42-49 是皱纹
    question31 = models.PositiveIntegerField('42. 你的脸上有皱纹吗？',blank=False, null=False)  # No. 42
    question32 = models.PositiveIntegerField('43. 日常生活中，你曾经在每年或不到一年中经历过多于两周的长时间日晒（2小时以上）吗？（包括暑假在内）如果是，多长时间一次？',blank=False, null=False)  # No. 43
    question33 = models.PositiveIntegerField('44. 你认为自己看上去有多大年龄？',blank=False, null=False)  # No. 44
    question34 = models.PositiveIntegerField('45. 过去五年里，你有意或者无意通过户外活动或者其他方式晒黑，大概多久一次？',blank=False, null=False)  # No. 45
    question35 = models.PositiveIntegerField('46. 根据你所居住的地方，你每天受日照的时间是多少？',blank=False, null=False)  # No. 46
    question36 = models.PositiveIntegerField('47. 在你的生活中，你共抽过多少烟（或者二手烟）？',blank=False, null=False)  # No. 47
    question37 = models.PositiveIntegerField('48. 请描述你居住地的空气污染状况：',blank=False, null=False)  # No. 48
    question38 = models.PositiveIntegerField('49. 你的母亲面部皮肤年龄看上去多大？',blank=False, null=False)  # No. 49

    # 不记分选择题 50-64
    non_score_question1 = models.CharField('50. 排便是否正常?',blank=True, max_length=255)  # No. 50
    non_score_question2 = models.CharField('51. 洁面',blank=True, max_length=255)  # No. 51
    non_score_question3 = models.CharField('52. 化妆水',blank=True, max_length=255)  # No. 52
    non_score_question4 = models.CharField('53. 精华',blank=True, max_length=255)  # No. 53
    non_score_question5 = models.CharField('54. 乳液或面霜',blank=True, max_length=255)  # No. 54
    non_score_question6 = models.CharField('55. 防晒',blank=True, max_length=255)  # No. 55
    non_score_question7 = models.CharField('56. 卸妆',blank=True, max_length=255)  # No. 56
    non_score_question8 = models.CharField('57. 洁面',blank=True, max_length=255)  # No. 57
    non_score_question9 = models.CharField('58. 化妆水',blank=True, max_length=255)  # No. 58
    non_score_question10 = models.CharField('59. 精华',blank=True, max_length=255)  # No. 59
    non_score_question11 = models.CharField('60. 乳液或面霜',blank=True, max_length=255)  # No. 60
    non_score_question12 = models.CharField('61. 面膜（非清洁类面膜）',blank=True, max_length=255)  # No. 61
    non_score_question13 = models.CharField('62. 去角质清洁面膜（去角质啫喱，泥面膜或其它清洁面膜）的频次',blank=True, max_length=255)  # No. 62
    non_score_question14 = models.CharField('63. 您是否去有定期去美容院或医美机构做皮肤护理的习惯？',blank=True, max_length=255)  # No. 63
    non_score_question15 = models.CharField('64. 近半年内您是否有出现过严重的皮肤问题(例如：大面积的痤疮. 湿疹. 皮肤过敏)：',blank=True, max_length=255)  # No. 64

    # 非选项问题
    fill_blank_question1 = models.TextField('65. 如果有出现严重的皮肤问题，请详细描述具体情况)：',blank=True, max_length=255)  # No. 65
    fill_blank_question2 = models.CharField('66、目前正在使用的卸妆类的护肤品名称',blank=True, max_length=512)  # No. 66
    fill_blank_question3 = models.CharField('67、目前正在使用的洁面乳/洁面霜/洁面油类的护肤品名称',blank=True, max_length=512)  # No. 67
    fill_blank_question4 = models.CharField('68、目前正在使用的化妆水类的护肤品名称',blank=True, max_length=512)  # No. 68
    fill_blank_question5 = models.CharField('69、目前正在使用的精华类的护肤品名称',blank=True, max_length=512)  # No. 69
    fill_blank_question6 = models.CharField('70、目前正在使用的乳液/面霜类的护肤品名称',blank=True, max_length=512)  # No. 70
    fill_blank_question7 = models.CharField('71、目前正在使用的去角质类的护肤品名称',blank=True, max_length=512)  # No. 71
    fill_blank_question8 = models.CharField('72、目前正在使用的面膜类的护肤品名称',blank=True, max_length=512)  # No. 72
    fill_blank_question9 = models.CharField('73、目前正在使用的防晒类的护肤品名称',blank=True, max_length=512)  # No. 73
    fill_blank_question10 = models.CharField('74、您使用哪些成分或护肤品会过敏？如果有请描述过敏的现象。',blank=True, max_length=512, help_text='提示：如没有，请填写无')  # No. 74

    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)


class Report(models.Model):
    """问卷报告结果, user_content,user_content_word"""
    answer = models.ForeignKey('survey.Answer', null=False, blank=False)
    purpose = models.CharField(max_length=64, choices=PURPOSE_CHOICES, blank=True)  # 问卷目标
    level = models.CharField(max_length=64, choices=SURVEY_LEVEL_CHOICES, blank=True)  # 问卷目标

    # 肤质4个维度种类
    oily_type = models.CharField(max_length=64, choices=SKIN_OILY_TYPE_CHOICES, blank=True)
    sensitive_type = models.CharField(max_length=64, choices=SKIN_SENSITIVE_TYPE_CHOICES, blank=True)
    pigment_type = models.CharField(max_length=64, choices=SKIN_PIGMENT_TYPE_CHOICES, blank=True)
    loose_type = models.CharField(max_length=64, choices=SKIN_LOOSE_TYPE_CHOICES, blank=True)
    # 肤质4个维度的测试评分
    oily_score = models.PositiveIntegerField(blank=True, null=True)
    sensitivity_score = models.PositiveIntegerField(blank=True, null=True)
    pigment_score = models.PositiveIntegerField(blank=True, null=True)
    loose_score = models.PositiveIntegerField(blank=True, null=True)

    summary = models.TextField(max_length=128, blank=True)  # 报告总结
    problem = models.TextField(max_length=128, blank=True)  # 存在的问题
    # allergy = models.TextField(max_length=128, blank=True)  # 过敏，copy from answer
    avoid_component = models.TextField(max_length=128, blank=True)  # 避免使用的成分
    doctor_advice = models.TextField(max_length=128, blank=True)  # 医生建议
    day_instruct = models.CharField(max_length=512, blank=True)  # 日间指导
    night_instruct = models.CharField(max_length=512, blank=True)  # 夜间指导
    mask_instruct = models.CharField(max_length=512, blank=True)  # 面膜指导
    emergency_solution = models.TextField(max_length=128, blank=True)  # 应急方案
    maintain_solution = models.TextField(max_length=128, blank=True)  # 维稳方案

    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)


class ReportProductAnalysis(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)  # 产品外键或名称
    name = models.CharField(max_length=255, blank=True)
    analysis = models.TextField(max_length=128, blank=True)  # 护肤品分析


class ReportProductAdvice(models.Model):
    report = models.ForeignKey(Report, null=False, blank=False)
    type = models.CharField(max_length=64, choices=PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES, blank=True)
    product = models.ForeignKey('premium_product.PremiumProduct', null=False, blank=False)
