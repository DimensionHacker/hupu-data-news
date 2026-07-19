# 本脚本的作用：
# 利用 jieba包 对 标题文本.txt 进行关键词提取。
# 根据关键词权重生成词云图。

import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



# 读取文本
with open("标题文本.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 自定义停用词
jieba.analyse.set_stop_words("stopwords.txt")

# 自定义词典
# jieba.load_userdict("dict.txt")

# 关键词提取
keywords = jieba.analyse.extract_tags(
    text, # 要分析的文本
    topK=10000, # 返回前多少个关键词
    withWeight= True, # 是否返回关键词权重
    allowPOS=('n','nr','ns',"nt","nz") # 指定允许的词性
)
# for word, weight in keywords:
#     print(f"{word:<10}{weight:.4f}")

word_dict = dict(keywords)

mask = np.array(Image.open("basketball.png"))

# 创建词云对象
wc = WordCloud(
    mask=mask,
    font_path="simhei.ttf",      # 黑体
    background_color="white",    #背景色
    width=1600,
    height=1000,
    max_words=100,
    max_font_size=220,
    min_font_size=10,
    relative_scaling=0.5
)

# 根据权重生成词云
wc.generate_from_frequencies(word_dict)

# 显示
plt.imshow(wc)
plt.axis("off")
plt.show()

# 保存
# wc.to_file("关键词词云.png")
