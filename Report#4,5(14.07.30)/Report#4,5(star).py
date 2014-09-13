print "\n".join("*" * i for i in range(1, 6))
print
print "\n".join(" " *(5-i) + "*" * i for i in range(1,6))
print

for i in range(1,6):
	print "*" * i
print

for i in range(1,6):
	print " " *(5-i) + "*" * i
print

def get_piramid():
	size = input("enter the number of maximum star : ")
	
	if size%2==0:
		for i in range(1,size/2+1):
			division = (size-2*i)/2
			print " "*division + "*"*(2*i) + " "*division
	else:
		for i in range(1,(size+1)/2+1):
			division = (size-(2*i-1))/2
			print " "*division + "*"*(2*i-1) + " "*division
get_piramid()