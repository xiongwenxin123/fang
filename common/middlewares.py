"""
自定义中间件
"""
import hashlib

from django.core.cache import cache
from django.http import JsonResponse

SHA1_GEN_PROTO = hashlib.sha1()


def check_user_sign(get_response):

    def middleware(request):
        if request.path.startswith('/api'):
            data = request.GET if request.method == 'GET' else request.data
            try:
                user_id = data['user_id']
                user_token = cache.get(f'fang:user:{user_id}')
                user_sign = data['user_sign']
                hasher = SHA1_GEN_PROTO.copy()
                hasher.update(f'{user_id}:{user_token}'.encode('utf-8'))
                if hasher.hexdigest() == user_sign:
                    return get_response(request)
            except KeyError:
                pass
            return JsonResponse({'msg': '身份验证失败拒绝访问'})
        else:
            return get_response(request)

    return middleware
