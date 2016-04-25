flag=0
flag1=0
list1=['a','b']
list2=['1','2']
#list2=[]
list3=['x','y','z']
#list3=[]
for i in list1:
	s=""
	s=s+i
	for j in list2:
		s=s+","+j
		flag=1
		for k in list3:
			flag1=1
			s=s+","+k
			print s
			s=i+","+j
		if(flag1==0):
			s+=",Unknown"
			print s
		s=i
	if(flag==0):
		for k in list3:
			s=s+",Unknown,"+k
			print s
			s=i
	

	
	
	
