import re

from django.core.cache import caches
from django.http import Http404, JsonResponse

MOBILE_CODE_URL = '/api/mobile_code/'
TEL_PATTERN = re.compile(r'%s(?P<tel>1[3-9]\d{9})' % MOBILE_CODE_URL)
SMS_BLOCK_INTERVAL = 60


def block_sms_middleware(get_response):
    """阻止60秒以内重复获取手机验证码的中间件"""

    def middleware(request):
        try:
            if request.path.startswith(MOBILE_CODE_URL):
                matcher = TEL_PATTERN.match(request.path)
                tel = matcher.group('tel')
                if caches['code'].get(tel):
                    result = {
                        'code': 401,
                        'msg': f'请不要在{SMS_BLOCK_INTERVAL}秒内重复提交'
                    }
                    return JsonResponse(result)
            return get_response(request)
        except Exception:
            raise Http404('无效的请求')

    return middleware
