# 青龙使用代理池来避免黑IP问题
使用的库
```
pip3 install requests
pip3 install datetime
pip3 install time
pip3 install random
pip3 install json
```
### 在脚本的第9行改成自己的配置文件地址，一般青龙目录都是这个
path = '/root/ql/config/config.sh'
### 在脚本的第10改成代理添加的行数，
line = int(134)
我的之前134行之前使用其他http代理，使用更改的是134行，请查看config.sh配置文件查看自己需要添加哪一行
<br>
<img src="./img/htt.jpg" alt="">

代理脚本会根据抓取的代理池更新而延迟一秒钟更新，代理池大部分代理可用请放心使用
运行脚本
线程守护运行脚本
```
nohup python3 ip_broker.py &
```

