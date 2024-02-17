from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

from cart.views import cart_id
from django.http import HttpResponse
from cart.models import CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def store(request, category_slug=None):
    
    categories = None
    
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        print(categories)
        products = Product.objects.filter(category=categories, is_available=True)
        count = products.count()
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        print(products)
    
    else:
        products=Product.objects.all().filter(is_available=True).order_by('id')
        count = products.count()
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)

    
    context = {
        'products': paged_products, 
        'count': count
        }
    
    return render(request, 'store.html', context)


def product_detail(request,category_slug, product_slug):
    try:
        one_product= Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=cart_id(request),product=one_product).exists()

    except Exception as e:
        raise e
    context={'one_product': one_product,'in_cart': in_cart}
    return render(request, 'product-detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
            count = products.count()
    context={
        'products': products,
        'count':count
    }
    return render(request, 'store.html',context)