import gevent
from gevent import socket

hosts = ['www.google.com', 'www.yahoo.co.jp', 'www.google.co.jp']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
