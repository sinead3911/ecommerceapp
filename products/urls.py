from django.conf.urls import url, include
from .views import all_products, do_search

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^search/', do_search, name='search')
    
]


