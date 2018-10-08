"""
自定义实现缓存和权限验证的装饰器(暂时没有用上)
"""
# from pickle import dumps
# from pickle import loads
# from functools import wraps
#
# from django.core.cache import cache
# from django.shortcuts import render
#
# PAGE_CACHE_KEY = 'fang:pagecache:%s'
# MODEL_CACHE_KEY = 'fang:modelcache:%s'
#
#
# def my_model_cache(key: str, timeout: int=None):
#     """自定义实现模型缓存的装饰器"""
#
#     def wrapper1(func):
#
#         def wrapper2(*args, **kwargs):
#             real_key = '%s:%s' % (MODEL_CACHE_KEY % key, ':'.join(map(str, args)))
#             serialized_data = cache.get(real_key)
#             if serialized_data:
#                 data = loads(serialized_data)
#             else:
#                 data = func(*args, **kwargs)
#                 cache.set(real_key, dumps(data), timeout=timeout)
#             return data
#
#         return wrapper2
#
#     return wrapper1
#
#
# def my_page_cache(timeout: int):
#     """自定义实现页面缓存的装饰器"""
#
#     def wrapper1(view_func):
#
#         def wrapper2(request):
#             if request.method == 'GET':
#                 key = PAGE_CACHE_KEY % request.get_full_path()
#                 response = cache.get(key)
#                 if not response:
#                     response = view_func(request)
#                     cache.set(key, response, timeout)
#             else:
#                 response = view_func(request)
#             return response
#
#         return wrapper2
#
#     return wrapper1
#
#
# def my_login_required(view_func):
#     """自定义检查用户是否登录的装饰器"""
#
#     @wraps(view_func)
#     def wrapper(request):
#         try:
#             if request.session['user_id']:
#                 return view_func(request)
#         except KeyError:
#             pass
#         return render(request, 'login.html', {'hint': '请先登录'})
#
#     return wrapper
#
#
# def check_perm(perm_name):
#     """自定义检查用户是否具有操作权限的装饰器"""
#
#     def wrapper1(view_func):
#
#         def wrapper2(request):
#             user = request.session['user_id']
#
#             if user.has_perm(perm_name):
#                 return view_func(request)
#             else:
#                 return render(request, '403.html')
#         return wrapper2
#
#     return wrapper1
