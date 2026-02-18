from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


def product_list(request):

    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def update_stock(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        new_quantity = int(request.POST.get('quantity'))

        if new_quantity < 0:
            messages.error(request, "Stock cannot be negative")
        else:
            product.quantity = new_quantity
            product.save()
            return redirect('product_list')

    return render(request, 'update_stock.html', {'product': product})
