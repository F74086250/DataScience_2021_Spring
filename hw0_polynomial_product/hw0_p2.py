"""
這個副程式是用來計算演員的revenue平均值的
"""
def calcu_average(act_lis):
	sum=0
	if len(act_lis)==0:
		return 0.0
	else:
		for i in range(len(act_lis)):
			sum+=act_lis[i]
		return sum/len(act_lis)



f=open("IMDB-Movie-Data.csv","r")
print("========================================")
#listmyfile=f.readlines()
list1=[]
for line in f:
	list1.append(line.strip())

for i in range(len(list1)):
	list1[i]=list1[i].split(",")


"""
設計思路:先找出所有2016年電影的rating然後append到一個list最後再印出前三大的
我印出的是擁有前三大的rating的所有電影
"""	
print("Top-3 movies with the highest ratings in 2016:")
print("                                             ")

rat_in_2016=[]
for i in range(len(list1)):
	if list1[i][5]=="2016":
		rat_in_2016.append(list1[i][7])

#print(rat_in_2016)
for i in range(3):
	for j in range(len(list1)):
		if list1[j][5]=="2016" and list1[j][7]==rat_in_2016[i]:
			print(list1[j][1])



print("========================================")
"""
設計思路:先把原始list中之演員欄位的演員split好之後，以不重複之方式建立一個演員list,
接著以演員為主去掃原始list，每個演員皆設一個act_lis去接收每個演員掃到之revenue並傳入副程式計算平均值後直接傳入act_avg_rev裡面，並找大值
我印出的是擁有最大平均revenue的所有演員
"""
print("The actor generating the highest average revenue:")
print("                                             ")

actor=[]
nothing=0
for i in range(1,len(list1)):
	list1[i][4]=list1[i][4].replace("| ","|").split("|")
	for j in range(len(list1[i][4])):
		if list1[i][4][j] in actor:
			nothing+=1
		else:
			actor.append(list1[i][4][j])
#print(nothing)
act_rev_avg=[]
for i in range(len(actor)):
	act_lis=[]
	for j in range(1,len(list1)):
		if actor[i] in list1[j][4]:
			if list1[j][9]=="":
				nothing+=1
			else:
				act_lis.append(float(list1[j][9]))
	#print(act_lis)

	act_rev_avg.append(calcu_average(act_lis))

#print(act_rev_avg)
#print(len(act_rev_avg))



#act_rev_avg=act_rev_avg.sort()
count=0
a=max(act_rev_avg)
for i in range(len(act_rev_avg)):
	if a==act_rev_avg[i]:
		count+=1
		print(actor[i])
print("Total=",count)


		






print("========================================")
"""
先找出Emms Waston演過之電影的所有rating並append進一個list，接著直接傳入副程式算平均
"""
print("The average rating of Emma Watson’s movies:")
print("                                             ")

emma_rat=[]
for i in range(len(list1)):
	if "Emma Watson" in list1[i][4]:
		emma_rat.append(float(list1[i][7]))
print(calcu_average(emma_rat))

#for i in range(len(list1)):



print("========================================")
"""
設計思路:先把原始list中之導演欄位以不重複之方式建立一個導演list,
接著以導演為主去掃原始list，每個導演皆設一個temp_direc去接收每個導演掃到之演員以不重複之方式append進來取len傳入direc_co裡面，並找大值
我印出的是擁有前三多合作演員數量的所有導演
"""
print("Top-3 directors who collaborate with the most actors:")
print("                                             ")

direc=[]
for i in range(1,len(list1)):
	if list1[i][3] not in direc:
		direc.append(list1[i][3])

direc_co=[]
for i in range(len(direc)):
	temp_direc=[]
	for j in range(len(list1)):
		if list1[j][3]==direc[i]:
			for k in range(len(list1[j][4])):
				if list1[j][4][k] not in temp_direc:
					temp_direc.append(list1[j][4][k])
	#if direc[i]=="Ridley Scott":
	#	print(temp_direc)
	#if direc[i]=="M. Night Shyamalan":
	#	print(temp_direc)
	#if direc[i]=="Danny Boyle":
#		print(temp_direc)
#	if direc[i]=="Paul W.S. Anderson":
#		print(temp_direc)


	#print(direc[i],(":"),temp_direc)
	#print(" ")
	direc_co.append(len(temp_direc))

count=0
#print(direc_co)
for i in range(3):
	a=max(direc_co)
	for j in range(len(direc_co)):
		if direc_co[j]==a:
			count+=1
			print(direc[j],(":"),direc_co[j])
			direc_co[j]=min(direc_co)

print("Total=",count)

#print(len(list1))
#print("max=",max(direc_co))
#print(direc_co)
"""
count=0
count1=0
for i in range(len(direc)):
	if direc[i]=="":
		print("1")
		count1+=1
	else:
		print("0")
		count+=1
a=(count1,count)
print("one=%d,zero=%d"%a)
#print(len(direc))

"""
"""
act=[]
for i in range(len(list1)):
	act.append(list1[i][4])
del act[0]
for i in range(len(act)):
	act[i]=act[i].split("|")
	#print(act[i])

#for i in range(len(act)):
#	for j in range(len(act[i])):
#		print(len(act[i]))
#		print(act[i][j])

#print(len(act))

drc=[]
for i in range(len(list1)):
	drc.append(list1[i][3])
del drc[0]
#for i in range(len(drc)):
#	print(drc[i])
#print(len(drc))



direc=[]
direc.append(list1[1][3])

for i in  range(1,len(list1)):
	judge=0
	for j in range(len(direc)):
		if list1[i][3]==direc[j]:
			judge=1
	if judge==0:
		direc.append(list1[i][3])

for i in range(len(direc)):
	for j in range(len(drc)):
		if direc[i]==drc[j]:
			for k in range(len(act[j])):
				jg=0
				for x in (1,len(direc[i])):
					if act[j][k]==direc[i][x]:
						jg=1
				if jg==0:
					direc[i].append(act[k])
for i in range(len(direc)):
	print(direc[i])

#for i in range(len(direc)):


#for i in range(len(direc)):
	#print(direc[i])
#print(len(direc))
"""
print("========================================")
"""
設計思路:先將電影分類以|split開後，演員為主去掃原始list並將電影分類以不重複之方式傳入tmp並將len(tmp)傳入num_of_act_gen並找前兩大值
我是將前兩多的演的電影種類找出並印出所有有這兩個數字的演員
"""
print("Top-2 actors playing in the most genres of movies:")
print("                                             ")

for i in range(len(list1)):
	list1[i][2]=list1[i][2].split("|")

num_of_act_gen=[]
for i in range(len(actor)):
	tmp=[]
	for j in range(len(list1)):

		if actor[i] in list1[j][4]:
			for k in range(len(list1[j][2])):
				if list1[j][2][k] not in tmp:
					tmp.append(list1[j][2][k])
#	print(actor[i],len(tmp),tmp)			
	num_of_act_gen.append(len(tmp))

count=0
for i in range(2):
	a=max(num_of_act_gen)
	for j in range(len(num_of_act_gen)):
		if num_of_act_gen[j]==a:
			count+=1
			print(actor[j],":",num_of_act_gen[j])
			num_of_act_gen[j]=min(num_of_act_gen)

print("Total=",count)
#print(num_of_act_gen)
#print(len(num_of_act_gen))
#print(len(actor))

print("========================================")
print("Top-3 actors whose movies lead to the largest maximum gap of years:")
print("                                             ")
"""
設計思路:先把原始list中之演員欄位的演員split好之後，以不重複之方式建立一個演員list,
接著以演員為主去掃原始list，每個演員皆設一個year去接收每個演員掃到之電影演出年分，計算出差值後append入max_gap後，並找大值
我找出了前三個最大的差值並印出所有有這三個差值的演員
"""
max_gap=[]
for i in range(len(actor)):
	year=[]
	for j in range(len(list1)):
		if actor[i] in list1[j][4]:
			year.append(int(list1[j][5]))
	max_gap.append(max(year)-min(year))
count=0
for i in range(3):
	if count>=3:
		break
	else:
		a=max(max_gap)
		for j in range(len(max_gap)):
			if max_gap[j]==a:
				count+=1
				print(actor[j],":",max_gap[j])
				max_gap[j]=-1
print("Total=",count)
print("========================================")
"""
解題思路:以強尼戴普為中心，找出與他直接合作過的演員，以不重複的方式append進去collaborate_with_JD裡面，接著再以那些直接合作演員為中心去往外擴散，找出所有間接合作演員
迴圈終止條件就是當某次的len(collaborate_with_JD)跟下次迴圈之len(collaborate_with_JD)之差值為0(表以全部找完)，接著印出所有列表內之演員
"""
print("Find all actors who collaborate with Johnny Depp in direct and indirect ways:")
print("                                             ")
collaborate_with_JD=[]
collaborate_with_JD.append("Johnny Depp")

broden=1
while broden>0:
	start=len(collaborate_with_JD)
	for i in range(len(collaborate_with_JD)):
		for j in range(len(list1)):
			if collaborate_with_JD[i] in list1[j][4]:
				for k in range(len(list1[j][4])):
					if list1[j][4][k] not in collaborate_with_JD:
						collaborate_with_JD.append(list1[j][4][k])

		
	final=len(collaborate_with_JD)
	broden=final-start

collaborate_with_JD[0]
for i in range(1,len(collaborate_with_JD)):

	print(collaborate_with_JD[i])
cnt=[]
cnt+=26*[0]
#for i in range(1,len(collaborate_with_JD)):
#	cnt[ord(collaborate_with_JD[i][0])-65]+=1
#ct=0
#for i in range(len(cnt)):
#	print(chr(i+65),":",cnt[i])
#	ct+=cnt[i]
print("Total=",len(collaborate_with_JD)-1)
#print(ct)
print("========================================")
"""
print("A`s ASCII=",ord("A"))
print("Z`s ASCII=",ord("Z"))
print("-`s ASCII=",ord("-"))
"""
f.close()
#print(len(list1))
#print(list1)