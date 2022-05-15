# generate_gwcloud.py
from stylecloud import gen_stylecloud
import jieba
import re
 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def generate_wordlcloud(file_name,png_name):
    with open('./'+file_name+'.txt', 'r', encoding='utf-8') as f:
        data = f.read()
 
    # 文本预处理  去除一些无用的字符   只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = " ".join(new_data)
 
    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=False)
 
    result_list = []
    with open('./unknow.txt', 'w+', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()
        for i in con:
            i = i.replace("\n", "")  # 去掉读取每一行数据的\n
            stop_words.add(i)
 
    for word in seg_list_exact:
        # 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    print(result_list)
 
    # stylecloud绘制词图
    gen_stylecloud(
        text=' '.join(result_list),  # 输入文本
        size=600,  # 词图大小
        collocations=False,  # 词语搭配
        font_path='C:/Windows/Fonts/msyh.ttc',  #C:\Windows\Fonts目录下有诸多字体可选择，可自行替换。
        output_name=''+png_name+'.png',  #输出文本名
        icon_name='fas fa-apple-alt',  # 蒙版图片，暂不清楚能否替换
        palette='cartocolors.qualitative.Bold_5'  # palettable调色
    )
 
    I = mpimg.imread('./'+png_name+'.png')
    plt.axis('off')
    plt.imshow(I)
    plt.show()