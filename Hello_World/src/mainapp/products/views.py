from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product


# Create your views here.
def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    form = ProductForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})


def delete(request, pk):
    # pk = primary key
    pk = int(pk)
    # retrieve item from db with pk & store in item
    item = get_object_or_404(Product, pk=pk)
    # if item exists and the request posts, run delete
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    # pass the item we are working with to our delete page
    context = {"item": item, }
    return render(request, "products/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # create form instance & bind data to it
        form = ProductForm(request.POST or None)
        if form.is_valid():
            # if form is valid delete record
            form.delete()
            return redirect('admin_console')
        else:
            return redirect('admin_console')


def createRecord(request):
    # open product form and store in in form
    form = ProductForm(request.POST or None)
    # is valid check, if valid save form
    if form.is_valid():
        form.save()
        # pass back to admin console page
        return redirect('admin_console')
    else:  # if not valid print errors on screen
        print(form.errors)
        form = ProductForm()
    context = {'form': form, }
    return render(request, 'products/createRecord.html', context)
