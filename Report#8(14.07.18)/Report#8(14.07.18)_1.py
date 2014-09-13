#-*- coding: utf-8 -*-
# 게시판에서 작성자 파싱

import urllib
import webbrowser
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://fs.jtbc.joins.com/RSS/newsflash.xml").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

article_name = []
article_link = []

for item in soup.select("title"):
	#큰 branch에서 파싱을 한 다음
	#그 branch의 하위/상위 요소를 선택해서 내가 원하는 데이터만 출력한다

	article_name.append(item.get_text())
	#기사 제목을 리스에 저장합니다.

for item in soup.select("link"):
	article_link.append(item.get_text())
	# authors.append(item.parent.get_text())	# 작성자 태그의 부모요소의 text만 가져오기
	# authors.append(item.findChildren())		# 작성자 태그의 자식요소만 가져오기
	# authors.append(item.children.get_text())

for i in range(0,len(article_name)):
	if i==0:
		print "News Name : %s" %(article_name[i].encode('utf-8'))
	else:
		print "%d.%s" %(i,article_name[i].encode('utf-8'))

print
get_article_number = int(raw_input("보고 싶은 뉴스 번호를 입력하세요.:"))
print "%s" % article_name[get_article_number].encode('utf-8')
print article_link[get_article_number]
webbrowser.open(article_link[get_article_number])
print
