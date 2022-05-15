# Product.py
import time
import request_barrage as ec
import generate_gwcloud as gw
import request_comments as rc
import requests
import json
import easygui as g
headers={
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0"
}
bvNum = g.enterbox(msg='请输入视频的BV号,b站页面以BV开头的字符串', title='B站爬取弹幕和评论。 Author@halsen')
BUrl = 'https://api.bilibili.com/x/player/pagelist?bvid=' + bvNum + '&jsonp=jsonp'
response = requests.get(url = BUrl, headers = headers)
d = json.loads(response.text)
print(d)
cid = d['data'][0]['cid'] #0 数组元素的位置
print(cid)
cd = str(cid)
AidUrl = 'https://api.bilibili.com/x/web-interface/view?cid='+cd+'&bvid='+bvNum+''
response = requests.get(url = AidUrl, headers = headers)
e = json.loads(response.text)
print(e)
aid = e['data']['aid'] #e json数据 data的value值类型是集合
print(aid)
ad = str(aid)
d = g.enterbox(msg='请在此输入文件名，以保存该视频cid,aid和弹幕。')
# file_name = ''+d+'_demo'
file_path = d
h = g.enterbox(msg='爬取弹幕输入1，爬取评论输入2.')
n = int(h)
if n == 1:
    ec.request_barrage(file_path, cid)
 
    f = g.enterbox(msg='您是否要生成弹幕词云图，1生成，2不生成。')
    g = int(f)
    if g == 1:
        gw.generate_wordlcloud(file_path, d)
    elif g == 2:
        print("好的")
elif n == 2:
    e = 0
    page = 1
    while e == 0:
        url = "https://api.bilibili.com/x/v2/reply?pn=" + str(page) + '&type=1&oid=' + ad + '&sort=2'
        try:
            print()
 
            # print(url)
            content = rc.get_content(url)
            print("page:", page)
            rc.Out2File(content,file_path)
            page = page + 1
            # 为了降低被封ip的风险，每爬20页便歇5秒。
            if page % 10 == 0:
                time.sleep(5)
        except:
            e = 1
else:
    print("输入错误")
 
 