import requests
from bs4 import BeautifulSoup
import pandas as pd

#URLの取得
url = 'https://news.goo.ne.jp/topstories/today/'
res = requests.get(url)

#HTMLの解析
soup = BeautifulSoup(res.text, 'html.parser')

#ニュースリストの取得
todayNewsLists = soup.find_all('ul', attrs={'responsive-margin-bottom'})
todayNewsList = todayNewsLists[0]
listTitleNewsList = soup.find_all('p', attrs={'list-title-news'})

#リスト、辞書の準備
details = {}
data=[]

#dataframeの作成準備
for i,listTitleNews in enumerate(listTitleNewsList):
    details[i] = listTitleNews.text.replace('\u3000','')
data.append(details)

#dataframeの作成
df = pd.DataFrame(data)
df = df.T

#CSV出力
df.to_csv('goo今日のニュース.csv', index=False)
print('出力完了')