from django.shortcuts import render, redirect

from django.urls import reverse

import productadminapp

from . import models


# Create your views here.

def add_product_sale(request):
    '''
    添加产品销售
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'productsaleapp/add_product_sale.html')
    elif request.method == 'POST':
        # 获取数据
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        sale_price = request.POST.get('sale_price')
        sale_number = request.POST.get('sale_number')
        total_money = request.POST.get('total_money')
        pro_info = request.POST.get('pro_info')

        produc = request.session['productadmin']

        print('-===================-', produc.id)
        # pro = productadminapp.models.ProductAdmin.objects.filter(pk=produc.id)

        # produc = request.session['productadmin']

        product_sale = models.ProductSale(name=name, phone_number=phone_number, sale_price=sale_price,
                                          sale_number=sale_number, total_money=total_money, pro_info=pro_info,
                                          product=produc)

        product_sale.save()
        return render(request, 'userapp/index.html', {})


def sale_list(request):
    '''
    产品销售视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        pro_sale = models.ProductSale.objects.all()
        return render(request, 'productsaleapp/sale_list.html', {'pro_sale': pro_sale})


def delete(request, pro_id):
    '''
    删除
    :param request:
    :param pro_id:
    :return:
    '''
    pro_sale = models.ProductSale.objects.get(pk=pro_id)
    pro_sale.delete()
    return redirect(reverse("productsaleapp:sale_list", kwargs={}))


def search_sale(request):
    '''
    搜索
    :param request:
    :return:
    '''
    if request.method == 'POST':

        # 获取搜索框的数据
        name = request.POST['search']
        pro_sale_list = []

        pro_sale = models.ProductSale.objects.all()
        for pro_name in pro_sale:
            pro_sale_list.append(pro_name.name)
        print(pro_sale_list)
        if name:
            for item in pro_sale_list:
                if name == item:
                    p_sale = models.ProductSale.objects.filter(name=name)
                    return render(request, 'productsaleapp/sale_list.html', {'pro_sale': p_sale})
        else:
            return redirect(reverse("productsaleapp:sale_list", kwargs={}))
