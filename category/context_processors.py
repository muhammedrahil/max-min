
from category.models import Category


def product_category(request):
    return{
        'product_category': Category.objects.all().filter(is_active=True),
    }



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


