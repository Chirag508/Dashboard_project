from django.shortcuts import render,redirect
from .forms import product_form,userreggistarationform,loginform
from .models import product
from django.contrib.auth import login,logout
# Create your views here.
def show_dashbord(request):
    return render(request,'base_dashbord.html')

def show_home(request):
    return render(request,'dashboard.html')

def show_intro(request):
    return render(request,'intro.html')

def show_product_form(request):
    products = product.objects.all()
    # print(products)   #this line will print the product data into terminal.....
    if request.method=='POST':
        form = product_form(request.POST)
        if form.is_valid():
            print("Form is valid, saving data...")
            form.save()
            return redirect('product')
        else:
            print("Form errors:",form.errror)
    else:
        form = product_form()
    
    return render(request,'product_data.html',{'products':products,'form':form})

def delete_product_data(request,id):
    del_product = product.objects.get(id = id)
    print(f"{del_product} deleting this")
    del_product.delete()
    return redirect('product')

def update_product_data(request,id):
    products = product.objects.all()
    upd_product = product.objects.get(id = id)
    form = product_form(instance=upd_product)
    if request.method=='POST':
        form = product_form(request.POST,instance=upd_product)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        return render(request,'product_data.html',{'products':products,'form':form})

def show_registration_form(request):
    if request.method=='POST':
        form = userreggistarationform(request.POST)
        if form.is_valid():
            print("Form is valid, saving data...")
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = userreggistarationform()
    return render(request,'register.html',{'form':form})

# def shoe_login_page(request):
#     form = loginform()
#     return render(request,'login.html',{'form':form})