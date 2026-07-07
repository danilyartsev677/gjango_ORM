from django.shortcuts import render, get_object_or_404
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    # Получаем параметр сортировки из GET-запроса, по умолчанию сортируем по имени
    sort_by = request.GET.get('sort', 'name')

    # Выбираем порядок сортировки в зависимости от параметра
    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    context = {
        'phones': phones,
        'sort_by': sort_by,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # Получаем объект телефона по его slug или возвращаем 404, если не найден
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)