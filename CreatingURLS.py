#Creating URLS:
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]
  
 # Creating Models:
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    
    #Register models into admin :
    from django.contrib import admin
from .models import *


admin.site.register(Product)

#Creating views for displaying product :
from django.shortcuts import render
from .models import *

def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})
  
  #Creaqting URLs for product:
  from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.products, name='products'),

]
#Creating template:
{% for product in productss %}
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="{{ product.image }}" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">{{ product.productname }}</h5>
    <p class="card-text">{{ product.description }}</p>
    <p class="card-text">Price - {{ product.price }}</p>
    <a href="#" class="btn btn-primary">Buy Now</a>
  </div>
</div>
{% endfor %}

Makemigrations and Migrate –
python manage.py makemigrations
python manage.py migrate

Creating superuser
django-admin createsuperuser

Run the app:
  python manage.py runserver
