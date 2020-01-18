import urllib.request as ur
url = "https://google.co.jp"

conn = ur.urlopen(url)
print(conn)

data = conn.read()
print(data)

print(conn.status)

print(conn.getheader('Content-Type'))

for key, value in conn.getheaders():
    print(key, value)