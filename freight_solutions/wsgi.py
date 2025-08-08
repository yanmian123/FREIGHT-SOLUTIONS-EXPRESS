"""
WSGI config for freight_solutions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freight_solutions.settings")

# application = get_wsgi_application()

# handler = application



import os
from django.core.wsgi import get_wsgi_application
from werkzeug.wrappers import Request
from werkzeug.wsgi import get_current_url

# 初始化Django WSGI应用
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freight_solutions.settings")
django_app = get_wsgi_application()

# Vercel适配层：将Django WSGI应用转换为Vercel可识别的格式
class VercelWSGIHandler:
    def __call__(self, environ, start_response):
        # 处理静态文件路径（可选，根据实际情况调整）
        path = environ.get('PATH_INFO', '')
        if path.startswith('/static/'):
            # 静态文件由Vercel路由直接处理，这里仅作兼容
            pass
        # 转发请求给Django应用
        return django_app(environ, start_response)

# 暴露Vercel要求的handler变量
handler = VercelWSGIHandler()