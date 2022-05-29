import json
import random
import time

import requests  # 导入requests包
from datetime import datetime, timedelta

# ql配置文件路径
path = 'aa.txt'
# ql要修改行的行数
line = int(1)
# 获取json数据  并转换成字典
arrays = []

def get_ip():
    """
    爬取的IP池地址
    :return:
    """
    # 清空字典内容，确保每次运行字典都是空的
    arrays.clear()
    # print("字典清空")
    # 获取网站数据
    url = 'https://uu-proxy.com/api/free'
    strhtml = requests.get(url).text
    data = json.loads(strhtml)

    for i in range(len(data['free']['proxies'])):

        # 下面是 地址、端口号、协议、支持HTTPS
        ip = data['free']['proxies'][i]['ip']
        port = data['free']['proxies'][i]['port']
        protocol = data['free']['proxies'][i]['scheme']
        htt = data['free']['proxies'][i]['support_https']

        # 把ip和port转换成字符串,并拼接成 协议://ip:port
        ip_port = str(protocol) + '://' + str(ip) + ':' + str(port)

        # 过滤掉不支持HTTPS的代理
        if htt:
            http_request(ip_port)

    return data

def countdown(data):
    """
    定时任务,和爬取网站基本同步更新数据
    :param data:
    :return:
    """
    a2 = data['free']['next_update_date']
    now = datetime.now()
    # 把时间转换成%Y-%m-%dT%H:%M:%S.%fZ格式
    a1 = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    # 把时间转换成%Y-%m-%dT%H:%M:%S.%fZ格式
    a1 = datetime.strptime(a1, "%Y-%m-%dT%H:%M:%S.%fZ")
    a2 = datetime.strptime(a2, "%Y-%m-%dT%H:%M:%S.%fZ")
    # 修改 a2增加8小时，a2时间慢了8小时
    a2 = a2 + timedelta(hours=8)
    # 计算时间差
    cc = a2 - a1
    # 把分钟转换成秒，比爬取网站更新慢一秒
    cc = cc.seconds + 1
    # print("等待时间", cc)
    time.sleep(cc)


def while_loop():
    """循环任务"""
    while True:
        data = get_ip()
        get_random_ip()
        # 打印字典
        print("字典内容", arrays)
        # 定时任务
        countdown(data)


def http_request(http_ip_port):
    """
    检测节点是否可用
    """
    proxies = {
        'https': http_ip_port,
        'https': http_ip_port
    }
    try:
        # 检测节点是否可用.多次检测，如果可用，就把节点添加到字典中
        output1 = requests.get("https://www.baidu.com/", proxies=proxies)
        output2 = requests.get("https://cn.bing.com/", proxies=proxies)
        output3 = requests.get("https://www.zhihu.com/", proxies=proxies)
        output4 = requests.get("https://www.taobao.com/", proxies=proxies)
        output5 = requests.get("https://www.jd.com/", proxies=proxies)
        # print("节点可用")
        # 修改一行代码
        https_ip_port = 'export ALL_PROXY=' + http_ip_port
        arrays.append(https_ip_port)
        # print(https_ip_port)
    except Exception as e:
        print("节点不可用")


# 获取随机IP
def get_random_ip():
    """
    如果节点都不可以用，就把写入文件空，让ql使用主机IP
    :return:
    """
    try:
        # 获取随机IP
        random_ip = random.choice(arrays)
    except Exception as e:
        random_ip = " "
    # print("本次IP是", random_ip)
    # 修改环境变量
    f = open(path, 'r+')
    flist = f.readlines()
    # ql行数从一开始，python读取从零开始
    flist[line - 1] = '{}\n'.format(random_ip)
    f = open(path, 'w+')
    f.writelines(flist)
    f.close()


if __name__ == '__main__':
    while_loop()
