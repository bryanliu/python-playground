# 这里面尝试了几个Python的web服务器以及初步的性能测试

## web.py
### 安装
```shell
pip3 install web.py 
```
### 代码
最简单的Case
```python
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
```
### 测试
```shell
ab -c 10 -n 1000  http://localhost:8080/

Requests per second:    338.90 [#/sec] (mean)
Time per request:       29.508 [ms] (mean)
Time per request:       2.951 [ms] (mean, across all concurrent requests)
Transfer rate:          29.12 [Kbytes/sec] received
```

不过并发稍微大一点，就挂了
```shell
ab -c 50 -n 1000  http://localhost:8080/

Benchmarking localhost (be patient)
apr_socket_recv: Connection reset by peer (54)
Total of 1 requests completed
```

## Django
### 安装
[官网](https://docs.djangoproject.com/zh-hans/3.2/faq/troubleshooting/#troubleshooting-django-admin)
```shell
pip3 install Django
```

### 生成Site
本来想用 
```shell
django-admin startproject mysite
```
来生成站点的，不过遇到pip3 安装路径不在path中，所以找不到。这个问题还没解决。
所以用了workaround
```shell
python -m django startproject mysite
```
### 运行
到mysite 的目录下面
执行
```shell
python manage.py runserver
```
服务就运行起来了

### 性能测试
```shell
ab -c 10 -n 1000  http://localhost:8000/

Server Software:        WSGIServer/0.2
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        10697 bytes

Concurrency Level:      10
Time taken for tests:   3.058 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      10925000 bytes
HTML transferred:       10697000 bytes
Requests per second:    327.04 [#/sec] (mean)
Time per request:       30.578 [ms] (mean)
Time per request:       3.058 [ms] (mean, across all concurrent requests)
Transfer rate:          3489.13 [Kbytes/sec] received
```
并发大一点，50左右，也直接挂了。

## FAST API
似乎是一个异步IO框架，性能确实比上面两个要好太多。
需要安装fast api 和 uvicorn(这个用来运行 fast api)
```shell
pip3 install fastapi
pip3 install uvicorn
```

代码
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'msg':'hello fast API'}
```

### 运行
```shell
python3 -m uvicorn FastAPI:app
```

### 性能测试
```shell
ab -c 10 -n 1000  http://localhost:8000/

Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        24 bytes

Concurrency Level:      10
Time taken for tests:   0.913 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      168000 bytes
HTML transferred:       24000 bytes
Requests per second:    1095.11 [#/sec] (mean)
Time per request:       9.132 [ms] (mean)
Time per request:       0.913 [ms] (mean, across all concurrent requests)
Transfer rate:          179.67 [Kbytes/sec] received
```

50个并发也没问题
```shell
ab -c 50 -n 1000  http://localhost:8000/

Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        24 bytes

Concurrency Level:      50
Time taken for tests:   0.793 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      168000 bytes
HTML transferred:       24000 bytes
Requests per second:    1261.64 [#/sec] (mean)
Time per request:       39.631 [ms] (mean)
Time per request:       0.793 [ms] (mean, across all concurrent requests)
Transfer rate:          206.99 [Kbytes/sec] received

```
100个并发问题也不大，不过每个请求时间变长了。
```shell
ab -c 100 -n 1000  http://localhost:8000/

Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        24 bytes

Concurrency Level:      100
Time taken for tests:   0.837 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      168000 bytes
HTML transferred:       24000 bytes
Requests per second:    1194.41 [#/sec] (mean)
Time per request:       83.723 [ms] (mean)
Time per request:       0.837 [ms] (mean, across all concurrent requests)
Transfer rate:          195.96 [Kbytes/sec] received
```