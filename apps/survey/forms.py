from django import forms
from django.utils.translation import ugettext_lazy as _

from config.constants import SEX_CHOICES, INCOME_CHOICES
from core.django.widgets import ThumbnailImageInput
from .models import Answer


class AnswerAddForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerUpdateForm(AnswerAddForm):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerDetailForm(AnswerAddForm):
    class Meta:
        model = Answer
        fields = '__all__'


class SurveyFillForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect(), label='2. 您的性别？')
    monthly_income = forms.ChoiceField(choices=INCOME_CHOICES, widget=forms.RadioSelect(), label='9. 月收入水平？')
    question1 = forms.ChoiceField(widget=forms.RadioSelect(), label='12. 在照片上，你的皮肤看起来油光发亮？',
                                  choices=(('从来不会', 'A. 从来不会'),
                                           ('偶尔', 'B. 偶尔'),
                                           ('经常', 'C. 经常'),
                                           ('一直如此', 'D. 一直如此'),))
    question2 = forms.ChoiceField(widget=forms.RadioSelect(), label='13. 在干燥的环境中，如果不使用面霜. 乳液或者防晒霜，你的面部皮肤会？',
                                  choices=(('感觉很干或很裂', 'A. 感觉很干或很裂'),
                                           ('感觉很紧绷', 'B. 感觉很紧绷'),
                                           ('感觉很正常', 'C. 感觉很正常'),
                                           ('看上去很光亮，或我从来没有感觉到我需要面霜、乳液或者防晒霜', 'D. 看上去很光亮，或我从来没有感觉到我需要面霜、乳液或者防晒霜'),
                                           ('我不知道', 'E. 我不知道')))
    question3 = forms.ChoiceField(widget=forms.RadioSelect(), label='14. 使用面霜或乳液后2-3小时你的面部会？',
                                  choices=(('非常粗糙，起屑', 'A. 非常粗糙，起屑'),
                                           ('平滑（不油不干）', 'B. 平滑（不油不干）'),
                                           ('轻度油光发亮', 'C. 轻度油光发亮'),
                                           ('光滑油亮，或我不需要用面霜或乳液', 'D. 光滑油亮，或我不需要用面霜或乳液'),))
    question4 = forms.ChoiceField(widget=forms.RadioSelect(), label='15. 早上正常护肤后，中午到下午会大量出油？',
                                  choices=(('从来不会', 'A. 从来不会'),
                                           ('只在夏天会', 'B. 只在夏天会'),
                                           ('在春夏秋会', 'C. 在春夏秋会'),
                                           ('四季都是如此', 'D. 四季都是如此'),))
    question5 = forms.ChoiceField(widget=forms.RadioSelect(), label='16. 在使用粉底液. BB霜或者隔离霜，但不涂粉饼或散粉的情况下，2~3小时后，你的妆容会？',
                                  choices=(('花妆泛油', 'A. 花妆泛油'),
                                           ('微微泛油', 'B. 微微泛油'),
                                           ('保持良好妆容', 'C. 保持良好妆容'),
                                           ('卡粉起屑', 'D. 卡粉起屑'),
                                           ('我不用粉底', 'E. 我不用粉底')))
    question6 = forms.ChoiceField(widget=forms.RadioSelect(), label='17. 你的脸部哪些部位有毛孔粗大问题？ ',
                                  choices=(('几乎没有', 'A. 几乎没有'),
                                           ('只在鼻头有', 'B. 只在鼻头有'),
                                           ('T区和鼻子周围', 'C. T区和鼻子周围'),
                                           ('全脸都有', 'D. 全脸都有'),))
    question7 = forms.ChoiceField(widget=forms.RadioSelect(), label='18. 你会怎样描述你的脸部肌肤的干油性？', choices=(('干性', 'A. 干性'),
                                                                                                      ('不油不干',
                                                                                                       'B. 不油不干'),
                                                                                                      ('T区油，其他部位干',
                                                                                                       'C. T区油，其他部位干'),
                                                                                                      ('油性', 'D. 油性'),))
    question8 = forms.ChoiceField(widget=forms.RadioSelect(), label='19. 当你使用肥皂泡沫. 泡沫乳. 泡沫丰富的洁面产品洁面时，你的面部皮肤会？',
                                  choices=(('感觉很干或很裂', 'A. 感觉很干或很裂'),
                                           ('感觉轻微的干，但是没有很裂', 'B. 感觉轻微的干，但是没有很裂'),
                                           ('感觉正常', 'C. 感觉正常'),
                                           ('感觉很油', 'D. 感觉很油'),))
    question9 = forms.ChoiceField(widget=forms.RadioSelect(), label='20. 在当前季节里，如果不使用面霜或乳液，你的脸部会？',
                                  choices=(('经常感觉紧绷', 'A. 经常感觉紧绷'),
                                           ('有时感觉紧绷', 'B. 有时感觉紧绷'),
                                           ('很少感觉紧绷', 'C. 很少感觉紧绷'),
                                           ('从来不会感觉紧绷', 'D. 从来不会感觉紧绷'),))
    question10 = forms.ChoiceField(widget=forms.RadioSelect(), label='21. 你会长粉刺. 闭口或痘痘等吗？',
                                   choices=(('从来不长', 'A. 从来不长'),
                                            ('很少长', 'B. 很少长'),
                                            ('有时会长', 'C. 有时会长'),
                                            ('总是长', 'D. 总是长'),))
    question11 = forms.ChoiceField(widget=forms.RadioSelect(), label='22. 你的面部会出现泛红的情况（点状或片状）吗？',
                                   help_text='提示：不是痘印',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('很少', 'B. 很少'),
                                            ('每月至少会有一次', 'C. 每月至少会有一次'),
                                            ('每周至少会有一次', 'D. 每周至少会有一次'),))
    question12 = forms.ChoiceField(widget=forms.RadioSelect(),
                                   label='23. 护肤产品（包括洁面产品. 水. 精华. 乳液/面霜等）会使你的面部出现发红. 发痒. 刺痛. 灼热的感觉吗？',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('很少', 'B. 很少'),
                                            ('经常', 'C. 经常'),
                                            ('总会有', 'D. 总会有'),
                                            ('我不用护肤品', 'E. 我不用护肤品')))
    question13 = forms.ChoiceField(widget=forms.RadioSelect(), label='24. 你曾经被诊断过有痤疮. 玫瑰痤疮. 遗传性皮炎. 湿疹. 接触性皮炎吗？',
                                   choices=(('没有', 'A. 没有'),
                                            ('没去看过，但是朋友或熟人说我有', 'B. 没去看过，但是朋友或熟人说我有'),
                                            ('是，不过不严重', 'C. 是，不过不严重'),
                                            ('是，而且很严重', 'D. 是，而且很严重'),
                                            ('不确定', 'E. 不确定')))
    question14 = forms.ChoiceField(widget=forms.RadioSelect(), label='25. 你会对金属首饰过敏吗？', choices=(('从来没有', 'A. 从来没有'),
                                                                                                 ('很少', 'B. 很少'),
                                                                                                 ('经常', 'C. 经常'),
                                                                                                 ('一带就过敏', 'D. 一带就过敏'),
                                                                                                 ('不确定', 'E. 不确定')))
    question15 = forms.ChoiceField(widget=forms.RadioSelect(), label='26. 你喝酒后经常脸红吗？', choices=(('从来没有', 'A. 从来没有'),
                                                                                                ('有时会', 'B. 有时会'),
                                                                                                ('很频繁', 'C. 很频繁'),
                                                                                                ('总会有，或因为这个原因我不喝酒',
                                                                                                 'D. 总会有，或因为这个原因我不喝酒'),
                                                                                                ('我从不喝酒', 'E. 我从不喝酒')))
    question16 = forms.ChoiceField(widget=forms.RadioSelect(), label='27. 防晒产品会使你的皮肤过敏（发红. 发痒. 刺痛. 灼热. 起疹子的感觉）吗？',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('很少', 'B. 很少'),
                                            ('经常', 'C. 经常'),
                                            ('总是有', 'D. 总是有'),
                                            ('我从不使用防晒霜', 'E. 我从不使用防晒霜')))
    question17 = forms.ChoiceField(widget=forms.RadioSelect(), label='28. 你的直系亲属中有几位被诊断为过敏体质（如：遗传过敏性皮炎. 湿疹. 哮喘. 过敏症）？',
                                   choices=(('没有', 'A. 没有'),
                                            ('我知道的有一位', 'B. 我知道的有一位'),
                                            ('有几位', 'C. 有几位'),
                                            ('很多家人都有皮炎、湿疹、哮喘和过敏症', 'D. 很多家人都有皮炎、湿疹、哮喘和过敏症'),
                                            ('不确定', 'D. 不确定'),))
    question18 = forms.ChoiceField(widget=forms.RadioSelect(), label='29. 如果皮肤接触含香味的洗衣剂或柔顺剂，你会出现什么反应？',
                                   choices=(('没有特殊的反应', 'A. 没有特殊的反应'),
                                            ('感觉皮肤有点干', 'B. 感觉皮肤有点干'),
                                            ('皮肤会痒', 'C. 皮肤会痒'),
                                            ('皮肤会发红发痒', 'D. 皮肤会发红发痒'),
                                            ('不确定，或我从没使用过', 'E. 不确定，或我从没使用过')))
    question19 = forms.ChoiceField(widget=forms.RadioSelect(), label='30. 在长时间运动后，或情绪波动较大的情况下，你的脸部或颈部会变红吗？',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('有时会', 'B. 有时会'),
                                            ('很频繁', 'C. 很频繁'),
                                            ('总会有', 'D. 总会有'),))
    question20 = forms.ChoiceField(widget=forms.RadioSelect(), label='31. 你在吃完辣的或是烫的食物后皮肤会发红吗？',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('有时会', 'B. 有时会'),
                                            ('很频繁', 'C. 很频繁'),
                                            ('每次都会', 'D. 每次都会'),
                                            ('我从来不吃辣的食物（如果由于吃完辣的或者烫的食物后会出现上述皮肤症状而不吃，选d）',
                                             'E. 我从来不吃辣的食物（如果由于吃完辣的或者烫的食物后会出现上述皮肤症状而不吃，选d）')))
    question21 = forms.ChoiceField(widget=forms.RadioSelect(), label='32. 你脸上哪些部位有红血丝？',
                                   help_text='提示：成片的红血丝或根根分明的红血丝',
                                   choices=(('没有', 'A. 没有'),
                                            ('鼻翼两侧', 'B. 鼻翼两侧'),
                                            ('鼻翼和脸颊有', 'C. 鼻翼和脸颊有'),
                                            ('全脸都有', 'D. 全脸都有'),))
    question22 = forms.ChoiceField(widget=forms.RadioSelect(), label='33. 在你长粉刺. 闭口. 痘痘之后，愈合处会出现棕色或黑色的印吗？',
                                   choices=(('从来没有或我没注意', 'A. 从来没有或我没注意'),
                                            ('有时', 'B. 有时'),
                                            ('经常', 'C. 经常'),
                                            ('只要长就有印', 'D. 只要长就有印'),
                                            ('我从没长过粉刺、闭口、痘痘', 'E. 我从没长过粉刺、闭口、痘痘')))
    question23 = forms.ChoiceField(widget=forms.RadioSelect(), label='34. 皮肤划伤后，愈合后的深色（不是粉色）痕迹会保持多久？',
                                   choices=(('没有留下深色的痕迹或没注意到过', 'A. 没有留下深色的痕迹或没注意到过'),
                                            ('一周', 'B. 一周'),
                                            ('几周', 'C. 几周'),
                                            ('几个月', 'D. 几个月'),))
    question24 = forms.ChoiceField(widget=forms.RadioSelect(),
                                   label='35. 如果几个月没被长时间（2小时以上）日晒过，当你第一次被长时间日晒时，你的皮肤会变黑变暗吗？',
                                   choices=(('有灼热感并发红，但不会变黑变暗', 'A. 有灼热感并发红，但不会变黑变暗'),
                                            ('灼热发红后肤色变暗', 'B. 灼热发红后肤色变暗'),
                                            ('肤色变暗', 'C. 肤色变暗'),
                                            ('我的皮肤已经很黑了，所以很难看出来（不能说自己没有从来没有被上时间日晒过，想想你的童年经历）',
                                             'D. 我的皮肤已经很黑了，所以很难看出来（不能说自己没有从来没有被上时间日晒过，想想你的童年经历）'),))
    question25 = forms.ChoiceField(widget=forms.RadioSelect(), label='36. 你是否被诊断过脸上有斑（表现为浅褐色. 深褐色或灰色斑）？',
                                   choices=(('没有', 'A. 没有'),
                                            ('有过，但是现在没有了', 'B. 有过，但是现在没有了'),
                                            ('是的', 'C. 是的'),
                                            ('是的，而且情况很严重', 'D. 是的，而且情况很严重'),
                                            ('不确定', 'E. 不确定')))
    question26 = forms.ChoiceField(widget=forms.RadioSelect(), label='37. 当你在太阳下长时间日晒（2小时以上）后，你脸上的斑点会变得更明显吗？',
                                   choices=(('我没有斑', 'A. 我没有斑'),
                                            ('不确定', 'B. 不确定'),
                                            ('有轻微的变深', 'C. 有轻微的变深'),
                                            ('变得很严重', 'D. 变得很严重'),
                                            ('我每天都涂防晒霜，我几乎不在太阳下（注意：如果您一直在用防晒霜是因为怕有晒斑或者雀斑，请选d）',
                                             'E. 我每天都涂防晒霜，我几乎不在太阳下（注意：如果您一直在用防晒霜是因为怕有晒斑或者雀斑，请选d）')))
    question27 = forms.ChoiceField(widget=forms.RadioSelect(), label='38. 你的脸上. 胸上. 背部或胳膊上，是否有或者曾经有过斑点？',
                                   choices=(('没有', 'A. 没有'),
                                            ('是的，有几个（1-5个）', 'B. 是的，有几个（1-5个）'),
                                            ('是的，很多（6-15个）', 'C. 是的，很多（6-15个）'),
                                            ('是的，非常多（16个或以上）', 'D. 是的，非常多（16个或以上）'),))
    question28 = forms.ChoiceField(widget=forms.RadioSelect(), label='39. 连续长时间日晒（2小时以上）几天后，你的皮肤会出现下列哪种情况？',
                                   choices=(('会晒伤，但是皮肤不会改变颜色', 'A. 会晒伤，但是皮肤不会改变颜色'),
                                            ('我的皮肤会黑一些', 'B. 我的皮肤会黑一些'),
                                            ('我的皮肤会变得很黑', 'C. 我的皮肤会变得很黑'),
                                            ('我的皮肤已经很黑了，所以看不出来又没有更黑', 'D. 我的皮肤已经很黑了，所以看不出来又没有更黑'),
                                            ('不确定（不能说自己没有从来没有被长时间日晒（2小时以上）过，想想你的童年经历）',
                                             'E. 不确定（不能说自己没有从来没有被长时间日晒（2小时以上）过，想想你的童年经历）')))
    question29 = forms.ChoiceField(widget=forms.RadioSelect(), label='40. 在你的面部有斑（点状或片状都算）吗？', choices=(('没有', 'A. 没有'),
                                                                                                        ('不知道（请仔细观察）',
                                                                                                         'B. 不知道（请仔细观察）'),
                                                                                                        ('有一点，不太明显',
                                                                                                         'C. 有一点，不太明显'),
                                                                                                        ('是的，很明显',
                                                                                                         'D. 是的，很明显'),))
    question30 = forms.ChoiceField(widget=forms.RadioSelect(), label='41. 你头发的自然色是？', choices=(('特黑', 'A. 特黑'),
                                                                                               ('黑', 'B. 黑'),
                                                                                               ('偏棕色', 'C. 偏棕色'),
                                                                                               ('偏黄色', 'D. 偏黄色'),))
    question31 = forms.ChoiceField(widget=forms.RadioSelect(), label='42. 你的脸上有皱纹吗？',
                                   choices=(('没有，即使笑、皱眉抬眉也都没有', 'A. 没有，即使笑、皱眉抬眉也都没有'),
                                            ('只有当我笑、皱眉或抬眉时才出现', 'B. 只有当我笑、皱眉或抬眉时才出现'),
                                            ('做表情时有，不做表情的时候也有一些', 'C. 做表情时有，不做表情的时候也有一些'),
                                            ('即使面无表情，也有很多细小皱纹', 'D. 即使面无表情，也有很多细小皱纹'),))
    question32 = forms.ChoiceField(widget=forms.RadioSelect(),
                                   label='43. 日常生活中，你曾经在每年或不到一年中经历过多于两周的长时间日晒（2小时以上）吗？（包括暑假在内）如果是，多长时间一次？',
                                   choices=(('从来没有过', 'A. 从来没有过'),
                                            ('一到五年', 'B. 一到五年'),
                                            ('五到十年', 'C. 五到十年'),
                                            ('多于十年', 'D. 多于十年'),))
    question33 = forms.ChoiceField(widget=forms.RadioSelect(), label='44. 你认为自己看上去有多大年龄？',
                                   choices=(('比你的年龄要年轻五到十岁', 'A. 比你的年龄要年轻五到十岁'),
                                            ('实际年龄', 'B. 实际年龄'),
                                            ('比你的年龄大五岁', 'C. 比你的年龄大五岁'),
                                            ('比你的年龄要多于五岁', 'D. 比你的年龄要多于五岁'),))
    question34 = forms.ChoiceField(widget=forms.RadioSelect(), label='45. 过去五年里，你有意或者无意通过户外活动或者其他方式晒黑，大概多久一次？',
                                   choices=(('从来没有', 'A. 从来没有'),
                                            ('一个月一次', 'B. 一个月一次'),
                                            ('一周一次', 'C. 一周一次'),
                                            ('每天', 'D. 每天'),))
    question35 = forms.ChoiceField(widget=forms.RadioSelect(), label='46. 根据你所居住的地方，你每天受日照的时间是多少？',
                                   choices=(('很少，我大多居住在灰色和阴暗的地方', 'A. 很少，我大多居住在灰色和阴暗的地方'),
                                            ('有一些，我住在比较阴暗的地方，但是有时候也会住在有正常阳光的地方', 'B. 有一些，我住在比较阴暗的地方，但是有时候也会住在有正常阳光的地方'),
                                            ('比较适中，我住在阳光比较适中的地方', 'C. 比较适中，我住在阳光比较适中的地方'),
                                            ('很多，我住在热带、南方、阳光很充足的地方', 'D. 很多，我住在热带、南方、阳光很充足的地方'),))
    question36 = forms.ChoiceField(widget=forms.RadioSelect(), label='47. 在你的生活中，你共抽过多少烟（或者二手烟）？',
                                   choices=(('没有', 'A. 没有'),
                                            ('几包', 'B. 几包'),
                                            ('几包到很多包', 'C. 几包到很多包'),
                                            ('我每天都吸很多烟', 'D. 我每天都吸很多烟'),
                                            ('我从不吸烟，但是我居住、生活和工作的周围都有经常吸烟的人', 'E. 我从不吸烟，但是我居住、生活和工作的周围都有经常吸烟的人')))
    question37 = forms.ChoiceField(widget=forms.RadioSelect(), label='48. 请描述你居住地的空气污染状况：',
                                   choices=(('空气清新', 'A. 空气清新'),
                                            ('一年中有一段时间空气污染，不能保证全年空气清新', 'B. 一年中有一段时间空气污染，不能保证全年空气清新'),
                                            ('空气轻度污染', 'C. 空气轻度污染'),
                                            ('空气污染严重', 'D. 空气污染严重'),))
    question38 = forms.ChoiceField(widget=forms.RadioSelect(), label='49. 你的母亲面部皮肤年龄看上去多大？',
                                   choices=(('比实际年龄小', 'A. 比实际年龄小'),
                                            ('与实际年龄相符', 'B. 与实际年龄相符'),
                                            ('比实际年龄大', 'C. 比实际年龄大'),
                                            ('我不记得了', 'D. 我不记得了'),))

    # 不计分选择题
    non_score_question1 = forms.ChoiceField(widget=forms.RadioSelect(), label='50. 排便是否正常?',
                                            choices=(('长期便秘', 'A. 长期便秘'),
                                                     ('1周1-2次', 'B. 1周1-2次'),
                                                     ('大概2天1次', 'C. 大概2天1次'),
                                                     ('每天都去，排便正常', 'D. 每天都去，排便正常'),
                                                     ('不一定，有时候会有一点便秘', 'E. 不一定，有时候会有一点便秘')))
    non_score_question2 = forms.ChoiceField(widget=forms.RadioSelect(), label='51. 洁面',
                                            choices=(('洁面产品洁面1次', 'A. 洁面产品洁面1次'),
                                                     ('清水洗脸（不用任何洁面产品）', 'B. 清水洗脸（不用任何洁面产品）'),
                                                     ('不洁面', 'C. 不洁面'),
                                                     ('其它', 'D. 其它'),))  # todo 如选择d，请备注具体情况：
    non_score_question3 = forms.ChoiceField(widget=forms.RadioSelect(), label='52. 化妆水', choices=(('使用', 'A. 使用'),
                                                                                                  ('不使用', 'B. 不使用'),
                                                                                                  ('喷雾代替', 'C. 喷雾代替'),
                                                                                                  ('先用肌底液再用化妆水',
                                                                                                   'D. 先用肌底液再用化妆水'),))
    non_score_question4 = forms.ChoiceField(widget=forms.RadioSelect(), label='53. 精华', choices=(('使用', 'A. 使用'),
                                                                                                 ('不使用', 'B. 不使用'),
                                                                                                 ('其它产品代替',
                                                                                                  'C. 其它产品代替')))  # todo 如选择c，请备注具体情况：
    non_score_question5 = forms.ChoiceField(widget=forms.RadioSelect(), label='54. 乳液或面霜', choices=(('使用', 'A. 使用'),
                                                                                                    ('不使用', 'B. 不使用'),
                                                                                                    ('两个都用', 'C. 两个都用'),
                                                                                                    ('其它产品代替',
                                                                                                     'D. 其它产品代替'),))  # todo 如选择d，请备注具体情况：
    non_score_question6 = forms.ChoiceField(widget=forms.RadioSelect(), label='55. 防晒',
                                            choices=(('四季每日使用，不管晴天阴天', 'A. 四季每日使用，不管晴天阴天'),
                                                     ('仅仅夏季使用', 'B. 仅仅夏季使用'),
                                                     ('不固定，想起来就用', 'C. 不固定，想起来就用'),
                                                     ('用底妆产品代替', 'D. 用底妆产品代替'),
                                                     ('从来不用', 'E. 从来不用')))
    non_score_question7 = forms.ChoiceField(widget=forms.RadioSelect(), label='56. 卸妆', choices=(('使用', 'A. 使用'),
                                                                                                 ('不使用，直接洗脸',
                                                                                                  'B. 不使用，直接洗脸'),
                                                                                                 ('偶尔使用，不固定',
                                                                                                  'C. 偶尔使用，不固定')))
    non_score_question8 = forms.ChoiceField(widget=forms.RadioSelect(), label='57. 洁面',
                                            choices=(('洁面产品洁面1次', 'A. 洁面产品洁面1次'),
                                                     ('清水洗脸（不用任何洁面产品）', 'B. 清水洗脸（不用任何洁面产品）'),
                                                     ('不洁面', 'C. 不洁面'),
                                                     ('其他', 'D. 其他'),))  # todo 如选择d，请备注具体情况：
    non_score_question9 = forms.ChoiceField(widget=forms.RadioSelect(), label='58. 化妆水', choices=(('使用', 'A. 使用'),
                                                                                                  ('不使用', 'B. 不使用'),
                                                                                                  ('喷雾代替', 'C. 喷雾代替'),
                                                                                                  ('先用肌底液再用化妆水',
                                                                                                   'D. 先用肌底液再用化妆水'),))
    non_score_question10 = forms.ChoiceField(widget=forms.RadioSelect(), label='59. 精华', choices=(('使用', 'A. 使用'),
                                                                                                  ('不使用', 'B. 不使用'),
                                                                                                  ('其它产品代替',
                                                                                                   'C. 其它产品代替')))  # todo 如选择c，请备注具体情况：
    non_score_question11 = forms.ChoiceField(widget=forms.RadioSelect(), label='60. 乳液或面霜', choices=(('使用', 'A. 使用'),
                                                                                                     ('不使用', 'B. 不使用'),
                                                                                                     (
                                                                                                     '两个都用', 'C. 两个都用'),
                                                                                                     ('其它产品代替',
                                                                                                      'D. 其它产品代替'),))  # todo 如选择d，请备注具体情况：
    non_score_question12 = forms.ChoiceField(widget=forms.RadioSelect(), label='61. 面膜（非清洁类面膜）',
                                             choices=(('从不使用', 'A. 从不使用'),
                                                      ('1周1次', 'B. 1周1次'),
                                                      ('1周2-3次', 'C. 1周2-3次'),
                                                      ('周3-5次或以上', 'D. 周3-5次或以上'),
                                                      ('想起来就用，不固定', 'E. 想起来就用，不固定')))
    non_score_question13 = forms.ChoiceField(widget=forms.RadioSelect(), label='62. 去角质清洁面膜（去角质啫喱，泥面膜或其它清洁面膜）的频次',
                                             choices=(('从不使用', 'A. 从不使用'),
                                                      ('1周1次', 'B. 1周1次'),
                                                      ('2-3周1次', 'C. 2-3周1次'),
                                                      ('1月1次', 'D. 1月1次'),
                                                      ('想起来就用，不固定', 'E. 想起来就用，不固定')))
    non_score_question14 = forms.ChoiceField(widget=forms.RadioSelect(), label='63. 您是否去有定期去美容院或医美机构做皮肤护理的习惯？',
                                             choices=(('有', 'A. 有'),
                                                      ('没有', 'B. 没有')))

    optional_fields = ['']

    class Meta:
        model = Answer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SurveyFillForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field_name not in self.optional_fields:
                field.required = True
