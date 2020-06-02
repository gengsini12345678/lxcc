from django.shortcuts import render, redirect

from django.urls import reverse

from django.contrib.auth.hashers import make_password, check_password

from  django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.core.cache import cache

from django.core.serializers import serialize

from django.http import HttpResponse

from . import models


# Create your views here.


def index(request):
    '''
    首页函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'userapp/index.html', {})


def register_user(request):
    '''
    注册视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'userapp/register_user.html', {})
    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        re_userpass = request.POST['re_userpass']
        realname = request.POST['realname']

        # 验证数据
        if len(username) < 6:
            return render(request, "userapp/register_user.html",
                          {"error_msg": "用户名不能小于六位"})
        if len(userpass) < 6:
            return render(request, "userapp/register_user.html",
                          {"error_msg": "密码不能小于六位"})
        if re_userpass != userpass:
            return render(request, "userapp/register_user.html",
                          {"error_msg": "两次的密码不一致"})
        # 保存数据
        try:
            user = User.objects.get(username=username)
            return render(request, 'userapp/register_user.html',
                          {"error_msg": "改用户名已存在，请重新注册"})
        except:
            # 创建用户注册
            # 对密码进行加密
            userpass = make_password(userpass)
            # print(userpass)
            user = User(username=username, password=userpass)

            user.save()
            usertable = models.UserTable(realname=realname, user=user)
            usertable.save()
            return render(request, "userapp/login_user.html", {"error_msg": "注册成功"})


def login_user(request):
    '''
    登录视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'userapp/login_user.html', {})
    elif request.method == 'POST':
        # 获取数据
        # 获取用户名和密码
        username = request.POST['username']
        userpass = request.POST['userpass']

        # 获取usertable对象
        user = User.objects.get(username=username)

        # 判断用户名或密码是否正确
        if check_password(userpass, user.password):
            request.session['login_user'] = user
            return redirect(reverse('userapp:index'))
        else:
            return render(request, 'userapp/login_user.html', {'error_msg': '用户名或者密码错误'})


def logout(request):
    '''
    退出系统视图函数
    :param request:
    :return:
    '''

    try:
        del request.session['login_user']
        return render(request, 'userapp/login.html', {})
    except:
        return redirect(reverse('userapp:index'))
