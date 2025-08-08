import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freight_solutions.settings")
application = get_wsgi_application()  # 变量名必须为 application