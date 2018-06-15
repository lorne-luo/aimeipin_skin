# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-15 04:26
from __future__ import unicode_literals

import apps.survey.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20180512_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='reportproductadvice',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reportproductadvice',
            name='report',
        ),
        migrations.RemoveField(
            model_name='reportproductanalysis',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reportproductanalysis',
            name='report',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='allergy',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='level',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='purpose',
        ),
        migrations.AddField(
            model_name='answer',
            name='birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='6. 您的出生日期？'),
        ),
        migrations.AddField(
            model_name='answer',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cosmetics',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='answer', verbose_name='5. 现阶段使用护肤品合集'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question1',
            field=models.TextField(blank=True, max_length=255, verbose_name='65. 如果有出现严重的皮肤问题，请详细描述具体情况)：'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question10',
            field=models.TextField(blank=True, help_text='提示：如没有，请填写无', max_length=255, verbose_name='74、您使用哪些成分或护肤品会过敏？如果有请描述过敏的现象。'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question2',
            field=models.TextField(blank=True, max_length=255, verbose_name='66、目前正在使用的卸妆类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question3',
            field=models.TextField(blank=True, max_length=255, verbose_name='67、目前正在使用的洁面乳/洁面霜/洁面油类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question4',
            field=models.TextField(blank=True, max_length=255, verbose_name='68、目前正在使用的化妆水类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question5',
            field=models.TextField(blank=True, max_length=255, verbose_name='69、目前正在使用的精华类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question6',
            field=models.TextField(blank=True, max_length=255, verbose_name='70、目前正在使用的乳液/面霜类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question7',
            field=models.TextField(blank=True, max_length=255, verbose_name='71、目前正在使用的去角质类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question8',
            field=models.TextField(blank=True, max_length=255, verbose_name='72、目前正在使用的面膜类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='fill_blank_question9',
            field=models.TextField(blank=True, max_length=255, verbose_name='73、目前正在使用的防晒类的护肤品名称'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question1',
            field=models.CharField(blank=True, max_length=255, verbose_name='50. 排便是否正常?'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question10',
            field=models.CharField(blank=True, max_length=255, verbose_name='59. 精华'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question11',
            field=models.CharField(blank=True, max_length=255, verbose_name='60. 乳液或面霜'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question12',
            field=models.CharField(blank=True, max_length=255, verbose_name='61. 面膜（非清洁类面膜）'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question13',
            field=models.CharField(blank=True, max_length=255, verbose_name='62. 去角质清洁面膜（去角质啫喱，泥面膜或其它清洁面膜）的频次'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question14',
            field=models.CharField(blank=True, max_length=255, verbose_name='63. 您是否去有定期去美容院或医美机构做皮肤护理的习惯？'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question15',
            field=models.CharField(blank=True, max_length=255, verbose_name='64. 近半年内您是否有出现过严重的皮肤问题(例如：大面积的痤疮. 湿疹. 皮肤过敏)：'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question2',
            field=models.CharField(blank=True, max_length=255, verbose_name='51. 洁面'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question3',
            field=models.CharField(blank=True, max_length=255, verbose_name='52. 化妆水'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question4',
            field=models.CharField(blank=True, max_length=255, verbose_name='53. 精华'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question5',
            field=models.CharField(blank=True, max_length=255, verbose_name='54. 乳液或面霜'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question6',
            field=models.CharField(blank=True, max_length=255, verbose_name='55. 防晒'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question7',
            field=models.CharField(blank=True, max_length=255, verbose_name='56. 卸妆'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question8',
            field=models.CharField(blank=True, max_length=255, verbose_name='57. 洁面'),
        ),
        migrations.AddField(
            model_name='answer',
            name='non_score_question9',
            field=models.CharField(blank=True, max_length=255, verbose_name='58. 化妆水'),
        ),
        migrations.AddField(
            model_name='answer',
            name='portrait',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='answer', verbose_name='3. 无PS、无滤镜、清晰纯素颜照片一张'),
        ),
        migrations.AddField(
            model_name='answer',
            name='portrait_part',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='answer', verbose_name='4. 如需重点关注部位可在此上传无PS、无滤镜、清晰的纯素颜照片'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='7. 您的身高'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='job',
            field=models.CharField(blank=True, max_length=64, verbose_name='8. 您目前从事的职业?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, verbose_name='11. 您的手机号？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='monthly_income',
            field=models.CharField(blank=True, choices=[('0-5000', '0-5000'), ('5001-10000', '5001-10000'), ('10001-20000', '10001-20000'), ('20000+', '20000+'), ('全职太太/先生', '全职太太/先生')], max_length=50, verbose_name='9. 月收入水平？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='1. 您的姓名？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='12. 在照片上，你的皮肤看起来油光发亮？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question10',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='21. 你会长粉刺. 闭口或痘痘等吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question11',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='22. 你的面部会出现泛红的情况（点状或片状）吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question12',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='23. 护肤产品（包括洁面产品. 水. 精华. 乳液/面霜等）会使你的面部出现发红. 发痒. 刺痛. 灼热的感觉吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question13',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='24. 你曾经被诊断过有痤疮. 玫瑰痤疮. 遗传性皮炎. 湿疹. 接触性皮炎吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question14',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='25. 你会对金属首饰过敏吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question15',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='26. 你喝酒后经常脸红吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question16',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='27. 防晒产品会使你的皮肤过敏（发红. 发痒. 刺痛. 灼热. 起疹子的感觉）吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question17',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='28. 你的直系亲属中有几位被诊断为过敏体质（如：遗传过敏性皮炎. 湿疹. 哮喘. 过敏症）？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question18',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='29. 如果皮肤接触含香味的洗衣剂或柔顺剂，你会出现什么反应？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question19',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='30. 在长时间运动后，或情绪波动较大的情况下，你的脸部或颈部会变红吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='13. 在干燥的环境中，如果不使用面霜. 乳液或者防晒霜，你的面部皮肤会？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question20',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='31. 你在吃完辣的或是烫的食物后皮肤会发红吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question21',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='32. 你脸上哪些部位有红血丝？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question22',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='33. 在你长粉刺. 闭口. 痘痘之后，愈合处会出现棕色或黑色的印吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question23',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='34. 皮肤划伤后，愈合后的深色（不是粉色）痕迹会保持多久？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question24',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='35. 如果几个月没被长时间（2小时以上）日晒过，当你第一次被长时间日晒时，你的皮肤会变黑变暗吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question25',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='36. 你是否被诊断过脸上有斑（表现为浅褐色. 深褐色或灰色斑）？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question26',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='37. 当你在太阳下长时间日晒（2小时以上）后，你脸上的斑点会变得更明显吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question27',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='38. 你的脸上. 胸上. 背部或胳膊上，是否有或者曾经有过斑点？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question28',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='39. 连续长时间日晒（2小时以上）几天后，你的皮肤会出现下列哪种情况？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question29',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='40. 在你的面部有斑（点状或片状都算）吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='14. 使用面霜或乳液后2-3小时你的面部会？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question30',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='41. 你头发的自然色是？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question31',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='42. 你的脸上有皱纹吗？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question32',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='43. 日常生活中，你曾经在每年或不到一年中经历过多于两周的长时间日晒（2小时以上）吗？（包括暑假在内）如果是，多长时间一次？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question33',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='44. 你认为自己看上去有多大年龄？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question34',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='45. 过去五年里，你有意或者无意通过户外活动或者其他方式晒黑，大概多久一次？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question35',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='46. 根据你所居住的地方，你每天受日照的时间是多少？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question36',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='47. 在你的生活中，你共抽过多少烟（或者二手烟）？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question37',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='48. 请描述你居住地的空气污染状况：'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question38',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='49. 你的母亲面部皮肤年龄看上去多大？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question4',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='15. 早上正常护肤后，中午到下午会大量出油？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question5',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='16. 在使用粉底液. BB霜或者隔离霜，但不涂粉饼或散粉的情况下，2~3小时后，你的妆容会？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question6',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='17. 你的脸部哪些部位有毛孔粗大问题？ '),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question7',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='18. 你会怎样描述你的脸部肌肤的干油性？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question8',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='19. 当你使用肥皂泡沫. 泡沫乳. 泡沫丰富的洁面产品洁面时，你的面部皮肤会？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question9',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='20. 在当前季节里，如果不使用面霜或乳液，你的脸部会？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='sex',
            field=models.CharField(blank=True, choices=[('女', '女'), ('男', '男')], max_length=30, null=True, verbose_name='2. 您的性别？'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='weixin_id',
            field=models.CharField(blank=True, help_text='提示：微信号不是昵称', max_length=128, verbose_name='10. 您的微信号？'),
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='ReportProductAdvice',
        ),
        migrations.DeleteModel(
            name='ReportProductAnalysis',
        ),
    ]
