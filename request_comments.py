# request_comments.py
import requests
import time
import json
def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
 
    r = requests.get(url, timeout=30, headers=headers)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    # print(r.text)
    return r.text
 
 
def get_content(url):
#整理信息，保存到列表变量中。
    comments = []
    # 把需要爬取信息的网页下载到本地
    html = get_html(url)
    try:
        s = json.loads(html)
    except:
        print("jsonload error")
 
    num = len(s['data']['replies'])  # 获取每页评论栏的数量
    # print(num)
    i = 0
    while i < num:
        comment = s['data']['replies'][i]  # 获取每栏评论
 
        InfoDict = {}  # 存储每组信息字典
 
        InfoDict['Uname'] = comment['member']['uname']  # 用户名
        InfoDict['Like'] = comment['like']  # 点赞数
        InfoDict['Content'] = comment['content']['message']  # 评论内容
        InfoDict['Time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))  # ctime格式的特殊处理？不太清楚具体原理
 
        comments.append(InfoDict)
        i = i + 1
    return comments
 
 
def Out2File(dict,path):
 # 爬取文件写到本地，文件名path，相对路径。
    with open(''+path+'.txt', 'a+', encoding='utf-8') as f:
        i = 0
        for comment in dict:
            i = i + 1
            try:
                f.write('姓名：{}\t  点赞数：{}\t \n 评论内容：{}\t  评论时间：{}\t \n '.format(
                    comment['Uname'], comment['Like'], comment['Content'], comment['Time']))
                f.write("-----------------\n")
            except:
                print("out2File error")
        print('当前页面保存完成')