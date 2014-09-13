#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)
#html과 같은 트리구조로 바꿔주는 함수

# print data
# print data['data']
# print data['data'][0]
# print data['data'][0]['age']
# print len(data['data'])

MEM_CODE_list=[]
MEM_NUM_list=[]
age_list=[]
job_list=[]
for i in range(0,len(data['data'])):
	MEM_CODE_list.append(data['data'][i]['MEM_CODE'])
	MEM_NUM_list.append(data['data'][i]['MEM_NUM'])
	age_list.append(data['data'][i]['age'])
	job_list.append(data['data'][i]['job'])
# print MEM_CODE_list
# print MEM_NUM_list
# print age_list

etc_list=[]
for i in range(0,len(age_list)):
	if age_list[i]>=50:
		etc_list.append("Old")
	else:
		etc_list.append("")
# print job_list
print "MEM_NUM  	Age  	MEM_CODE  		Job  			 etc"

for i in range(0,len(data['data'])):
	if i<10:
		if job_list[i].encode('utf-8') == "Businessman" or "Programmer":
			print"%d    	 	%d  	%d  	%s  	  %s"%(MEM_NUM_list[i],age_list[i],MEM_CODE_list[i],job_list[i].encode('utf-8'),etc_list[i])
		else:
			print"%d    	 	%d  	%d  	%s  			  %s"%(MEM_NUM_list[i],age_list[i],MEM_CODE_list[i],job_list[i].encode('utf-8'),etc_list[i])
	else:
		if job_list[i].encode('utf-8') == "Businessman" or "Programmer": 
			print"%d    	 	%d  	%d  	%s  	    %s"%(MEM_NUM_list[i],age_list[i],MEM_CODE_list[i],job_list[i].encode('utf-8'),etc_list[i])
		else:
			print"%d    	 	%d  	%d  	%s  			  %s"%(MEM_NUM_list[i],age_list[i],MEM_CODE_list[i],job_list[i].encode('utf-8'),etc_list[i])
# data_print = json.dumps(data, sort_keys=True, indent=4)
# print data_print	# 단순 보기 좋게 출력하기 위함
# print

# element = data['address']
# print element
# print
# etc = element['etc']
# dong = element['dong']
# #실행 시켜보면 address 라는 dictionary 변수 안에서 key 값에 따른 value들을 보는 것과 같다.
# #JSON이 dictionary와 비슷한 구조를 지니고 있다는사실을 알 수 있다.

# print etc
# print dong