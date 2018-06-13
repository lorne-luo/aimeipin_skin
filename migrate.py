from apps.premium_product.models import PremiumProduct
from apps.product.models import Product
from apps.survey.models import Answer

for p in PremiumProduct.objects.all():
    if not p.pic.name.startswith('premium_product'):
        p.pic.name = 'premium_product/' + p.pic.name
        p.save(update_fields=['pic'])

for p in Product.objects.all():
    if p.startswith('upload'):
        p.pic.name = p.pic.name.replace('upload', 'product')
        p.save(update_fields=['pic'])

for a in Answer.objects.all():
    if a.portrait.name.startswith('/upload'):
        a.portrait.name = a.portrait.name.replace('/upload', 'answer')
    if a.portrait_part.name.startswith('/upload'):
        a.portrait_part.name = a.portrait_part.name.replace('/upload', 'answer')
    if a.cosmetics.name.startswith('/upload'):
        a.cosmetics.name = a.cosmetics.name.replace('/upload', 'answer')
    a.save(update_fields=['portrait', 'portrait_part', 'cosmetics'])


# python manage.py rendervariations 'app_name.model_name.field_name' [--replace] [-i/--ignore-missing]
