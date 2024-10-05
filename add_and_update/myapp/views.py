from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import shop 

from .forms import ShopForm

# Create your views here.



def demo(request):

    product = shop.objects.all()

    return render(request,"home.html",{'products':product})


def details(request,shop_id):
    product1 = shop.objects.get(id = shop_id)
    return render(request,'detail.html',{'product':product1})


def add_product(request):

    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']
        price = int(price)
        s = shop(name = name,desc = desc,img = img,price = price)
        s.save()
        print("Product added successfully")
    return render(request,"add_product.html")






def update(request, id):
    obj = get_object_or_404(shop, id=id)  # Use get_object_or_404 for better error handling
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ShopForm(instance=obj)
    
    return render(request, "edit.html", {'form': form})





def delete(request, id):
    obj = get_object_or_404(shop, id=id)  # Use get_object_or_404 for better error handling
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    
    return render(request, "delete.html", {'object': obj})