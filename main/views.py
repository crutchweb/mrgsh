from django.shortcuts import render
from main.models import News, Category, Product


def IndexView(request):
    return render(request, 'index.html', {})


def ContactsView(request):
    return render(request, 'contact_us.html', {})


def CatalogView(request, category):
    cat = Category.objects.all().filter(slug=category)    
    sub_categories = Category.objects.all().filter(parent=cat[0].id)
    products = Product.objects.all().filter(category__in=sub_categories)    
    return render(request, 'catalog.html', {'sub_categories': sub_categories, 'category': cat[0], 'products': products})
    

def CatalogView_detail(request, category, subcategory):
    cat = Category.objects.all().filter(slug=subcategory)
    parent_cat = Category.objects.all().filter(slug=category)    
    products = Product.objects.all().filter(category__in=cat)    
    return render(request, 'subcategory.html', {'parent_category': parent_cat[0], 'category': cat[0], 'products': products})


def ProductView(request, category, subcategory, product_slug):
    cat = Category.objects.all().filter(slug=subcategory)
    parent_cat = Category.objects.all().filter(slug=category)
    prod = Product.objects.all().filter(slug=product_slug)
    print(cat)
    return render(request, 'product.html', {'parent_category': parent_cat[0], 'category': cat[0], 'product': prod[0]})


def NewsView(request):
    items = News.objects.all().order_by('-created')
    return render(request, 'news.html', {'items': items})


def NewsView_detail(request, slug):
    item = News.objects.all().filter(slug=slug)
    items = News.objects.all().order_by('-created')
    return render(request, 'news-deep.html', {'item': item[0], 'items': items})