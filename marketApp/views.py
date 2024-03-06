from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from marketApp.models import Product, Category


def main(request):
    return render(request, 'marketApp/main.html')


def catalog(request):
    object_list = Category.objects.all()
    paginator = Paginator(object_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': 'Категории Товаров',
    }
    return render(request, 'marketApp/catalog.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'marketApp/contacts.html')


def product(request, pk):
    object_list = Product.objects.filter(category_id=pk)
    paginator = Paginator(object_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Товары',
        'page_obj': page_obj,

    }

    return render(request, 'marketApp/product.html', context)


def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, pk=category_id)
        photo = request.FILES.get('photo')
        country = request.POST.get('country')
        in_stock = request.POST.get('in_stock')
        print(f'{name}')

        in_stock = True if in_stock == 'on' else False

        new_product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            photo=photo,
            country=country,
            in_stock=in_stock
        )
        print(new_product)

        new_product.save()

    return render(request, 'marketApp/add_product.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        category = Category.objects.create(
            name=name,
            description=description,
            photo=photo
        )
        category.save()

    return render(request, 'marketApp/add_category.html')
