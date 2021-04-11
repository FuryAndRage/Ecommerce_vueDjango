from django.urls import path, include
from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view(), name='latest_products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name ='product_detail')
]