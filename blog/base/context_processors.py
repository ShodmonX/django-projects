from . import models

def cat_list(request):
    cat_menu = models.Category.objects.all()
    return {'cat_menu': cat_menu}

def previous_link(request):
    previous_url = request.META.get('HTTP_REFERER')
    return {'previous_url': previous_url}