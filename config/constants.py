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
    (INCOME_TIER_5000, INCOME_TIER_5000),
    (INCOME_TIER_10000, INCOME_TIER_10000),
    (INCOME_TIER_20000, INCOME_TIER_20000),
    (INCOME_TIER_20000_PLUS, INCOME_TIER_20000_PLUS),
    (INCOME_TIER_HOUSEWIFE, INCOME_TIER_HOUSEWIFE)
)

PRODUCT_CATEGORY_CHOICES = (
    (u'乳液/面霜', u'乳液/面霜'),
    (u'卸妆', u'卸妆'),
    (u'去角质', u'去角质'),
    (u'化妆水', u'化妆水'),
    (u'洁面', u'洁面'),
    (u'精华', u'精华'),
    (u'防晒', u'防晒'),
    (u'面膜', u'面膜'),
)

PURPOSE_CHOICES = (
    (u'急镇定', u'急镇定'),
    (u'抗轻衰', u'抗轻衰'),
    (u'收毛孔', u'收毛孔'),
    (u'清痘痘', u'清痘痘'),
    (u'祛暗沉', u'祛暗沉'),
    (u'调水油', u'调水油'),
)

SKIN_TYPE_CHOICES = (
    (u'干性肌肤', u'干性肌肤'),
    (u'油性肌肤', u'油性肌肤'),
)
