# coding:utf-8
FEMALE = u'女'
MALE = u'男'

SEX_CHOICES = (
    (FEMALE, FEMALE),
    (MALE, MALE)
)
INCOME_TIER_5000 = '0-5000'
INCOME_TIER_10000 = '5001-10000'
INCOME_TIER_20000 = '10001-20000'
INCOME_TIER_20000_PLUS = '20000+'
INCOME_TIER_HOUSEWIFE = u'全职太太/先生'

INCOME_CHOICES = (
    (INCOME_TIER_5000, 'A. ' + INCOME_TIER_5000),
    (INCOME_TIER_10000, 'B. ' + INCOME_TIER_10000),
    (INCOME_TIER_20000, 'C. ' + INCOME_TIER_20000),
    (INCOME_TIER_20000_PLUS, 'D. ' + INCOME_TIER_20000_PLUS),
    (INCOME_TIER_HOUSEWIFE, 'E. ' + INCOME_TIER_HOUSEWIFE)
)

PURPOSE_CHOICES = (
    (u'急镇定', u'急镇定'),
    (u'抗轻衰', u'抗轻衰'),
    (u'收毛孔', u'收毛孔'),
    (u'清痘痘', u'清痘痘'),
    (u'祛暗沉', u'祛暗沉'),
    (u'调水油', u'调水油'),
    (u'种草', u'种草'),
)

SKIN_TYPE_DIMENSION_CHOICES = (
    (u'油性or干性', u'油性or干性'),
    (u'敏感or耐受', u'敏感or耐受'),
    (u'色素or非色素', u'色素or非色素'),
    (u'易皱纹or紧致', u'易皱纹or紧致'),
)
SKIN_TYPE_CHOICES = (
    (u'干性肌肤', u'干性肌肤'),
    (u'油性肌肤', u'油性肌肤'),
)

SKIN_OILY_TYPE_CHOICES = (
    (u'重度油性', u'重度油性'),
    (u'轻度油性', u'轻度油性'),
    (u'轻度干性', u'轻度干性'),
    (u'重度干性', u'重度干性'),
)
SKIN_SENSITIVE_TYPE_CHOICES = (
    (u'重度敏感性', u'重度敏感性'),
    (u'轻度敏感性', u'轻度敏感性'),
    (u'轻度耐受性', u'轻度耐受性'),
    (u'耐受性', u'耐受性'),
)
SKIN_PIGMENT_TYPE_CHOICES = (
    (u'色素性', u'色素性'),
    (u'非色素性', u'非色素性'),
)
SKIN_LOOSE_TYPE_CHOICES = (
    (u'非紧致性', u'非紧致性'),
    (u'紧致性', u'紧致性'),
)

PREMIUM_PRODUCT_ADVICE_TYPE_CHOICES = (
    (u'日间', u'日间'),
    (u'夜间', u'夜间'),
    (u'面膜', u'面膜'),
)

SURVEY_LEVEL_CHOICES = (
    ('9.9', '9.9'),
    ('98', '98'),
)

SURVEY_STATUS_CHOICES = (
    ('CREATED', '新建'),
    ('FILLED', '回答完毕'),
    ('FINISHED', '完成'),
)

ANSWER_PRODUCT_TYPE_CHOICES = (
    ('卸妆', '卸妆'),
    ('洁面', '洁面'),
    ('化妆', '化妆'),
    ('面霜', '面霜'),
    ('精华', '精华'),
    ('去角质', '去角质'),
    ('面膜', '面膜'),
    ('防晒', '防晒'),
)

PRODUCT_CATEGORY_CHOICES = (
    (u'卸妆', u'卸妆'),
    (u'洁面', u'洁面'),
    (u'化妆水', u'化妆水'),
    (u'乳液/面霜', u'乳液/面霜'),
    (u'精华', u'精华'),
    (u'去角质', u'去角质'),
    (u'面膜', u'面膜'),
    (u'防晒', u'防晒'),
)
