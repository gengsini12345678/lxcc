from django.shortcuts import render, redirect

from django.urls import reverse

from django.contrib.auth.decorators import  login_required

from . import models

import userapp


# Create your views here.

@login_required
def add_products(request):
    '''
    添加产品
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'productadminapp/add_products.html', {'error_msg': '用户名或者密码错误'})
    elif request.method == 'POST':
        # 获取数据
        pro_name = request.POST.get('pro_name')
        pro_code = request.POST.get('pro_code')
        product_type = request.POST.get('product_type')
        pro_price = request.POST.get('pro_price')
        pro_kuwei = request.POST.get('pro_kuwei')
        content = request.POST.get('content')

        # 获取当前用户
        user = request.session['login_user']
        usertable = userapp.models.UserTable.objects.get(user_id=user.id)

        productadmin = models.ProductAdmin(pro_code=pro_code, pro_kuwei=pro_kuwei, pro_name=pro_name,
                                           pro_price=pro_price, pro_type=product_type, pro_intro=content,
                                           usertable=usertable)
        productadmin.save()
        request.session['productadmin'] = productadmin
        return redirect(reverse("productadminapp:product_info", kwargs={'id': productadmin.id}))
        # return render(request,'userapp/index.html')

@login_required
def product_info(request, id):
    '''
    产品详情页面
    :param request:
    :param id:
    :return:
    '''
    product = models.ProductAdmin.objects.get(pk=id)
    # 跳转到产品详情页面
    return render(request, 'productadminapp/project_info.html', {"product": product})


@login_required
def product_list(request):
    '''
    查看所有的产品
    :param request:
    :return:
    '''
    if request.method == "GET":
        # alist = models.Wanda.objects.all()
        # 获取当前用户
        user = request.session['login_user']
        # print(user.id)
        usertable = userapp.models.UserTable.objects.get(user_id=user.id)
        # 查询当前用户添加的产品
        pro_admin = models.ProductAdmin.objects.filter(usertable_id=usertable.id).order_by("-id")
        # print(pro_admin)
        return render(request, 'productadminapp/product_list.html', {'pro_admin': pro_admin})


@login_required
def update_product(request, pro_id):
    '''
    修改产品
    :param request:
    :param pro_id:
    :return:
    '''
    if request.method == 'GET':
        product = models.ProductAdmin.objects.get(pk=pro_id)
        print(product.pro_name)
        print("---", pro_id)
        print(type(pro_id))
        return render(request, "productadminapp/update_product.html", {"product": product})
    elif request.method == 'POST':
        # 获取数据
        pro_name = request.POST.get('pro_name')
        pro_code = request.POST.get('pro_code')
        product_type = request.POST.get('product_type')
        pro_price = request.POST.get('pro_price')
        pro_kuwei = request.POST.get('pro_kuwei')
        content = request.POST.get('content')

        # 获取产品对象
        product = models.ProductAdmin.objects.get(pk=pro_id)
        product.pro_name = pro_name
        product.pro_code = pro_code
        product.product_type = product_type
        product.pro_price = pro_price
        product.pro_kuwei = pro_kuwei
        product.content = content
        # 修改数据并且保存到数据库中
        product.save()
        return redirect(reverse("productadminapp:product_list", kwargs={}))


@login_required
def search(request):
    '''
    查找视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'POST':

        # 获取产品的名称和类别
        pro_name_list = []
        pro_type_list = ['精品', '轮胎', '耗材']
        pro = models.ProductAdmin.objects.all()
        for name in pro:
            pro_name_list.append(name.pro_name)
        # print(pro_name_list)

        # 获取搜索框的数据
        name = request.POST['search']
        if name:
            for type in pro_type_list:
                # 判断搜索框的值是否等于 产品类型
                if name == type:
                    pro_admin = models.ProductAdmin.objects.filter(pro_type=name)
                    return render(request, 'productadminapp/product_list.html', {'pro_admin': pro_admin})
            for item in pro_name_list:
                # 判断搜索框的值是否等于 产品名称
                if name == item:
                    pro_admin = models.ProductAdmin.objects.filter(pro_name=name)
                    return render(request, 'productadminapp/product_list.html', {'pro_admin': pro_admin})
        else:
            # 重定向到产品列表页面
            return redirect(reverse('productadminapp:product_list', kwargs={}))


def delete(request, id):
    '''
    删除产品视图处理函数
    :param request:
    :param id:
    :return:
    '''
    # 通过id 来获取产品
    product = models.ProductAdmin.objects.get(pk=id)
    product.delete()
    return redirect(reverse("productadminapp:product_list", kwargs={}))
