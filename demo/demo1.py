from urllib import request, parse


login_data = parse.urlencode([
  
])

req = request.Request('https://kyfw.12306.cn/otn/queryOrder/queryOrderWaitTime?random=1517813722522')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))