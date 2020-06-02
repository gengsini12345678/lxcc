from django.conf.urls import url

from . import views

app_name = 'productadminapp'

urlpatterns = [
    url(r'^add_products',views.add_products,name = 'add_products'),

    # 产品详情
    url(r'^(?P<id>\d+)/product_info/$', views.product_info, name="product_info"),

    url(r'^product_list/$', views.product_list, name='product_list'),

    url(r'^(?P<pro_id>\d+)/update_product/$', views.update_product, name='update_product'),

    url(r'^search/$', views.search, name='search'),

    url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),


]