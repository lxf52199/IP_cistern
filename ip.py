from urllib import request

response = request.urlopen('http://ip.tool.lu')
print(response.read().decode())
aa = response.read().decode('utf-8', "ignore")
print(aa)
