import uuid
from random import randint

from django.db import transaction
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone

from user.forms import RegisterForm
from common.models import User
from common.models import LoginLog
from common.utils import to_md5_hex
from common.utils import get_ip_address
from common.utils import gen_mobile_code


@transaction.atomic
def login(request):
    """用户登录"""
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if request.session['captcha'] == request.POST['captcha'].lower():
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                hint = '用户名或密码错误'
            else:
                if user and user.password == to_md5_hex(password):
                    request.session['userid'] = user.userid
                    request.session['realname'] = user.realname
                    delta = timezone.now() - user.lastvisit
                    if delta.days >= 1:
                        user.point += randint(1, 10)
                        user.lastvisit = timezone.now()
                        user.save()
                    ipaddr = get_ip_address(request)
                    log = LoginLog(user=user, ipaddr=ipaddr)
                    log.save()
                    return redirect('/')
                else:
                    hint = '用户名或密码错误'
        else:
            hint = '请输入正确的图片验证码'
    return render(request, 'login.html', {'hint': hint})


def register(request):
    """用户注册"""
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            if request.POST['code'] == request.session['code']:
                form = RegisterForm(request.POST)
                if form.is_valid():
                    del form.cleaned_data['repassword']
                    del form.cleaned_data['code']
                    form.cleaned_data['token'] = uuid.uuid1().hex
                    form.cleaned_data['lastvisit'] = timezone.now()
                    user = User(**form.cleaned_data)
                    user.save(is_insert=True)
                    request.session['code'] = gen_mobile_code()
                    return render(request, 'login.html', {'hint': '注册成功请登录'})
                else:
                    hint = handle_register_errors(form.errors)
            else:
                hint = '请输入正确的手机验证码'
        except KeyError:
            hint = '请先获取手机验证码再完成注册'
    return render(request, 'register.html', {'hint': hint})


def logout(request):
    """用户注销"""
    request.session.flush()
    return redirect('/')


def handle_register_errors(errors):
    if 'username' in errors:
        hint = '无效的用户名或用户名已被注册'
    elif 'password' in errors:
        hint = '无效的用户口令'
    elif 'repassword' in errors:
        hint = errors['repassword'][0]
    elif 'realname' in errors:
        hint = '无效的真实姓名'
    elif 'tel' in errors:
        hint = '无效的手机号码或手机号码已被注册用户绑定'
    elif 'email' in errors:
        hint = '无效的电子邮箱或电子邮箱已被注册用户绑定'
    elif 'code' in errors:
        hint = '无效的验证码'
    else:
        hint = '请检查您的注册信息是否有效'
    return hint
