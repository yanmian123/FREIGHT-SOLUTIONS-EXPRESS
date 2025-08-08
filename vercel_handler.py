from io import StringIO
from freight_solutions.wsgi import application

def handler(event, context):
    # 手动转换 API Gateway 事件到 WSGI 环境变量
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': '&'.join(
            f"{k}={v}" for k, v in event.get('queryStringParameters', {}).items()
        ),
        'wsgi.input': StringIO(event.get('body', '')),
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '80',
        'wsgi.url_scheme': 'http'
    }
    
    # 响应容器
    response = {
        "statusCode": 200,
        "headers": {},
        "body": ""
    }

    def start_response(status, headers):
        response.update({
            "statusCode": int(status.split()[0]),
            "headers": dict(headers)
        })
        return lambda *args: None  # 兼容 WSGI 规范

    # 执行 Django 应用
    response["body"] = b"".join(
        application(environ, start_response)
    ).decode("utf-8")
    
    return response