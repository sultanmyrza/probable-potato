from django.conf import settings

def shop_context(request):
    context_data = dict()
    context_data['SHOP_NAME'] = settings.SHOP_NAME
    return context_data