from django.conf.urls import url

from . import views

app_name = 'productsaleapp'

urlpatterns = [
    url(r'^add_product_sale/$', views.add_product_sale, name='add_product_sale'),

    url(r'^sale_list/$', views.sale_list, name='sale_list'),

    url(r'^(?P<pro_id>\d+)/delete/$', views.delete, name='delete'),

    url(r'^search_sale/$', views.search_sale, name='search_sale'),
]
