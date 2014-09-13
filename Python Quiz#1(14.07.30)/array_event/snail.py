# -*- coding: utf-8 -*-
snail_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(0)
	snail_array.append(empty_array)

for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print init array
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# change array like this
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9 

######## insert your algorithm here ########
 
v = [0,1]
point = [0,0]
 
for num in range(1,26):
    snail_array[point[0]][point[1]] = num
    next_point = [point[0] + v[0], point[1] + v[1]]
 
    if next_point[0] not in range(5) or next_point[1] not in range(5):
        v = [v[1], -v[0]]
    elif snail_array[next_point[0]][next_point[1]] != 0:
        v = [v[1], -v[0]]
 
    point = [point[0] + v[0], point[1] + v[1]]
 
print
for column in snail_array:
    for num in column:
        print "%2s" % num,
    print
# print result array
# 영어 주석 힘들다.