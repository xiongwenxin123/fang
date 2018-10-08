"""
视图函数
"""
from django.http import HttpResponse

from common.captcha import Captcha
from common.utils import gen_captcha_text


def get_captcha(request):
    captcha_text = gen_captcha_text()
    image_bytes = Captcha.instance().generate(captcha_text)
    request.session['captcha'] = captcha_text.lower()
    # MIME类型 - Multipurpose Internet Mail Extension
    resp = HttpResponse(image_bytes, content_type='image/png')
    # 通过Content-Disposition设置文件是内联打开还是以附件的形式下载
    # resp['Content-Disposition'] = 'attachment; filename=hello.png'
    return resp
