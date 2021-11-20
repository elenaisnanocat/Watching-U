import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watchingu.settings")

import django
django.setup()

from movies.models import Movie
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request as req

from konlpy.tag import Okt
from wordcloud import WordCloud, STOPWORDS
import collections
from matplotlib import font_manager, rc
import matplotlib.pylab as plt


movies = Movie.objects.all()

for movie in movies:
    title = movie.title

    # # 드라이버 경로지정 => 해당 코드가 실행되면서 브라우저 열림
    # driver = webdriver.Chrome("./chromedriver.exe")

    # url = 'https://movie.naver.com/'
    # driver.get(url)

    # # 검색창에 영화 제목 검색 : 검색 버튼 클릭 -> 영화 상세 정보 클릭
    # element=driver.find_element_by_id('ipt_tx_srch')
    # element.send_keys(title)
    # driver.implicitly_wait(2)
    # try:
    #     driver.find_element_by_class_name('btn_srch').click()
    # except NoSuchElementException:
    #     continue
    # try:
    #     driver.find_element_by_class_name('result_thumb').click()
    # except NoSuchElementException:
    #     continue

    # # 현재 페이지에서 원하는 리뷰 요소 값 가져오기
    # reviews = []
    # driver.find_element_by_class_name('tab05').click()
    # res=req.urlopen(driver.current_url)
    # soup=BeautifulSoup(res,'html.parser')

    # # 전문가 평점
    # for i in soup.find_all('div', {"class":"score_reple"}):
    #     reviews.append(i.find('p').text)  
    # # 전문가 리뷰
    # for i in soup.find_all('p', {"class":"tx_report"}):
    #     reviews.append(i.text)


    # f = open('./files_crawling/' + title + '.txt', 'w', encoding='utf-8')
    # for review in reviews:
    #     f.write(review)
    # f.close()
    
    # driver.quit()



    # ---------------------------------------------------------
    ## 워드클라우드
    f = open('./files_crawling/' + title + '.txt', 'r', encoding='utf-8')
    data = f.read()

    if len(data) == 0: 
        continue
        # pass
    okt = Okt()
    noun_data = okt.nouns(data)
            
    # 불용어 제거
    stopword=[]
    word=[i for i in noun_data if i not in stopword]
    word=[i for i in word if len(i)>1]  

    data_cnt=collections.Counter(noun_data) 

    # font_name=font_manager.FontProperties(fname="C:/USERS/USER/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/A옛날사진관3.TTF"). get_name()
    font_name=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf"). get_name()
    rc('font', family=font_name)

    # wc=WordCloud(font_path="C:/USERS/USER/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/A옛날사진관3.TTF", width=900, height=500, colormap = 'RdPu', background_color='white', max_words=100, stopwords=STOPWORDS).generate_from_frequencies(data_cnt)
    wc=WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", width=600, height=900, colormap = 'Purples', background_color='white', max_words=100, stopwords=STOPWORDS).generate_from_frequencies(data_cnt)
    # wordcloud.recolor(color_func = "colorbrewer.diverging.Spectral_11")
    wc.to_file('static/'+ title +'.png')
    plt.figure(figsize=(10,10))
    plt.imshow(wc)
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.3)
    plt.close()