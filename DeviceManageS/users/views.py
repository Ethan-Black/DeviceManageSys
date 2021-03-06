# _*_encoding:utf-8 _*_
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                user_login = UserProfile.objects.get(username=user_name)
                request.session['username'] = user_name
                request.session['flag'] = user_login.flag
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误!'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class MobileLoginView(View):
    def get(self, request):
        return render(request, 'mobile_login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                user_login = UserProfile.objects.get(username=user_name)
                request.session['username'] = user_name
                request.session['flag'] = user_login.flag
                request.session['user_id'] = user_login.id
                return HttpResponseRedirect('/mobile_index/')
            else:
                return render(request, 'mobile_login.html', {'msg': '用户名或密码错误!'})
        else:
            return render(request, 'mobile_login.html', {'login_form': login_form})


# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '用户名或密码错误！'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('/mobile_login/')


@login_required
def mb_userinfo(request):
    user_id = request.session.get('user_id', '')
    if user_id:
        user = UserProfile.objects.values('username', 'birthday', 'gender', 'mobile', 'email', 'flag', 'image')\
            .get(id=user_id)
        # print(user)
        return render(request, 'mobile_me.html', {'user': user})
    else:
        login_form = '请先登录！'
        return render(request, 'mobile_login.html', {'login_form': login_form})


@login_required
def mb_userinfo_edit(request):
    # name = request.GET.get('username', '')
    user_id = request.session.get('user_id', '')
    user = UserProfile.objects.values('username', 'birthday', 'gender', 'mobile', 'email', 'flag', 'image')\
        .get(id=user_id)
    # print(user)
    return render(request, 'mobile_me_edit.html', {'user': user})


@login_required
def mb_me_edit_success(request):
    user_id = request.session.get('user_id', '')
    username = request.POST.get('username')
    # image = request.POST.get('img')
    image = request.FILES.get('img')
    gender = request.POST.get('gender')
    # flag = request.POST.get('flag')
    birthday = request.POST.get('birthday')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')

    dev = UserProfile.objects.get(id=user_id)
    if dev.username == username and dev.gender == gender and \
            dev.birthday == birthday and dev.mobile == mobile \
            and dev.email == email and dev.image == image:
        pass
    else:
        dev.username = username
        dev.image = image
        dev.gender = gender
        # dev.flag = flag
        dev.birthday = birthday
        dev.mobile = mobile
        dev.email = email
        dev.save()

    user = dev
    # user_flag = request.session.get('flag')
    # categories = DeviceCategory.objects.all()
    return render(request, 'mobile_me.html', {'user': user})


def page_not_found(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
