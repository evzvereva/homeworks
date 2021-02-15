from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    elif sort == 'min_price':
        phones = phones.order_by('price')

    context = {'phones': phones.all()}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug).first()
    context = {'ph': phones}
    return render(request, template, context)
