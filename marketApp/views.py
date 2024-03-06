from django.shortcuts import render

from marketApp.models import Product, Category


def main(request):
    return render(request, 'marketApp/main.html')


def catalog(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории Товаров',
    }
    return render(request, 'marketApp/catalog.html', context)


def contacts(request):
    return render(request, 'marketApp/contacts.html')


def product(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': 'Товары',
    }
    return render(request, 'marketApp/product.html', context)


def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        photo = request.POST.get('photo')
        country = request.POST.get('country')
        in_stock = request.POST.get('in_stock')

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

        new_product.save()

    return render(request, 'marketApp/add_product.html', {'categories': categories})


def add_category(request):
    return render(request, 'marketApp/add_category.html')
