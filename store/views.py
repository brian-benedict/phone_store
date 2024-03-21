from django.shortcuts import render, redirect
from .models import Phone, Customer, Product
from .forms import CustomerForm
from django.shortcuts import render, redirect
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def phone_details(request, phone_id):
    products = Product.objects.get(id=phone_id)
    return render(request, 'store/phone_details.html', {'products': products})

def contact_us(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'store/contact_us.html', {'form': form})

def about_us(request):
    return render(request, 'store/about_us.html')

# Additional views can be added as needed





# views.py



def product_registration(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = ProductForm()
    return render(request, 'store/product_registration.html', {'form': form})
