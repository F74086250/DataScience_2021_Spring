"""
這是用來處理係數或是次方的值要用的，比如係數是1324，那就是1*10^3+3*10^2+2*10^1+4*10^0
"""
def power_10(a,b):

	ans=1
	if b==0:
		return 1
	else:
		for i in range(b):
			ans*=a
		return ans
"""
這是用來處理常數項之值的計算
"""	
def constant(list_con):
	#print(list_con)
	temp=[]
	for i in range(1,len(list_con)-1):
		temp.append(list_con[i])
	#print(temp)
	ans=0
	#print(temp)
	for i in range(len(temp)):
		ans+=int(temp[i])*power_10(10,len(temp)-(i+1))
	return ans
"""
這是用來處理未知數之次方的計算
"""
def pow_of_alpha(start,end,lst):
	#print("1")
	temp=[]
	for i in range(start,end):
		temp.append(lst[i])

	ans=0
	for i in range(len(temp)):
		ans+=int(temp[i])*power_10(10,len(temp)-(i+1))
	return ans

"""
這是用來處理兩個項相乘的副程式，一次傳入兩個字串，先處理正負號，再處理含有未知數項的係數，這裡的概念就是針對傳入的兩個字串都個別設一個list，為27格，包含第一格的係數
與後面26格，後面就是每個大寫英文字母的次方，最後再設一個mult_ans的list，用來存兩字串相乘之結果，也是27格，第一格係數為前面兩個list第一格之乘積，後面的次方數為前面兩個
list同位置之相加
"""

def multiply(list1,list2):
	mult_ans=[]
	mult_1=[]
	mult_2=[]
	for i in range(27):
		mult_1.append(0)
		mult_2.append(0)
		mult_ans.append(0)
	
	if list1[0]=='+'and list2[0]=='+':
		sign=1
	if list1[0]=='+'and list2[0]=='-':
		sign=-1
	if list1[0]=='-'and list2[0]=='+':
		sign=-1
	if list1[0]=='-'and list2[0]=='-':
		sign=1
	judge=0
	for i in range(len(list1)):
		if 65<=ord(list1[i])<=90:
			judge=1
	if judge==0:
		mult_1[0]=constant(list1)
	else:
		temp_coe1=[]

		for i in range(1,len(list1)):
			if 65<=ord(list1[i])<=90:
				break
			else:
				temp_coe1.append(int(list1[i]))
		total=0
		for i in range(len(temp_coe1)):
			total+=temp_coe1[i]*power_10(10,len(temp_coe1)-(i+1))
		mult_1[0]=total

	judge=0
	for i in range(len(list2)):
		if 65<=ord(list2[i])<=90:
			judge=1
	if judge==0:
		mult_2[0]=constant(list2)
	else:

		temp_coe2=[]

		for i in range(1,len(list2)):
			if 65<=ord(list2[i])<=90:
				break
			else:
				temp_coe2.append(int(list2[i]))
		total=0
		for i in range(len(temp_coe2)):
			total+=temp_coe2[i]*power_10(10,len(temp_coe2)-(i+1))
		mult_2[0]=total



	mult_ans[0]=sign*mult_1[0]*mult_2[0]
	for i in range(len(list1)):
		if 65<=ord(list1[i])<=90:
			start=i+1
			end=start
			#print("start one=",start)
			while (not 65<=ord(list1[end])<=90) :
				if list1[end]!='$':
					end+=1
				else:
					break
			#	print("end one=",end)
			mult_1[ord(list1[i])-64]=pow_of_alpha(start,end,list1)

	for i in range(len(list2)):
		if 65<=ord(list2[i])<=90:
			start=i+1
			end=start
			#print("start two=",start)
			while not 65<=ord(list2[end])<=90 :
				if list2[end]!='$':
					end+=1
				else:
					break
			#	print("end two=",end)
			mult_2[ord(list2[i])-64]=pow_of_alpha(start,end,list2)

	for i in range(1,len(mult_ans)):
		mult_ans[i]=mult_1[i]+mult_2[i]
	if mult_ans[0]>0:
		rtn="+"+str(mult_ans[0])
	else:
		rtn=str(mult_ans[0])
	for i in range(1,len(mult_ans)):
		#if i==0:
		#	print(mult_ans[i],"*",end='')
		#else:

		#	if mult_ans[i]!=0:
		#		print(chr(i+64),"^",mult_ans[i],end='')
		if mult_ans[i]!=0:
			rtn+=str(chr(i+64))+str(mult_ans[i])

	rtn+="$"
	#if 48<=ord(rtn[len(rtn)-2])<=57:
	#	rtn=rtn[:len(rtn)-2]+"$"
	#print("1")
#	print(list1,"*",list2,"=",rtn)

	return rtn

"""
主程式的設計思路就是先把讀入的字串split成許多個相乘項並且將相乘項的格式統一化，比如(XY)*(Y+Z)就把他統一成(1*X^1Y^1)*(1*Y^1+1*Z^1)，如此一來傳入multiply時就比較好做
最後再Output時只要去掉一些為了格式統一化而多補的字元就好了
跟原本的程式寫法只差在標準格式化問題的一些細節處理
"""
inp=input("Input the polynomials:")
first=inp.find('(')
last=inp.rfind(')')
inp=inp[first+1:last]
inplist=inp.split(")(")
length=len(inplist)
#print(length)
#print(inplist)

for i in range(length):
	inplist[i]=inplist[i].replace("+"," +").replace("-"," -").split(" ")
	if inplist[i][0]=="":
		del inplist[i][0]
#for i in range(len(inplist)):
	

for i in range(len(inplist)):
	for j in range(len(inplist[i])):
		inplist[i][j]+="$"
		if inplist[i][j][0]!='-' and inplist[i][j][0]!='+':
			inplist[i][j]='+'+inplist[i][j]

		if 65<=ord(inplist[i][j][1])<=90:
			inplist[i][j]=inplist[i][j][0:1]+"1"+inplist[i][j][1:]
		for k in range(len(inplist[i][j])):
			if 65<=ord(inplist[i][j][k])<=90 and 65<=ord(inplist[i][j][k+1])<=90 or 65<=ord(inplist[i][j][k])<=90 and inplist[i][j][k+1]=="$":
				inplist[i][j]=inplist[i][j][:k+1]+"1"+inplist[i][j][k+1:]
#print(inplist)

i=0
while i<(length-1):
	temp=[]
	for j in range(len(inplist[i])):
		for k in range(len(inplist[i+1])):
		#	print("1")
			temp.append(multiply(inplist[i][j],inplist[i+1][k]))
	#print(temp)
	inplist[i+1]=temp
	i+=1
#print(inplist[length-1])
ip=inplist[length-1]
for i in range(len(ip)):
	for j in range(len(ip[i])):
		if 65<=ord(ip[i][j])<=90:
			ip[i]=ip[i][:j]+"*"+ip[i][j:]
			break
#print(ip)

const=[]
non_rep=[]
count=0
for i in range(len(ip)):
	judge=0
	#print(len(ip[i]))
	for j in range(len(ip[i])):
		#print(ip[i],end='')

		if 65<=ord(ip[i][j])<=90:
			judge=1

	if judge==0:
		const.append(ip[i][:len(ip[i])-1])
	else:
		ip[i]=ip[i].split("*")
		#print("ip[i][1]=",ip[i][1])
		ip[i][1]=ip[i][1][:len(ip[i][1])-1]
		if ip[i][1]  not in non_rep:
			non_rep.append(ip[i][1])
		#	#print(non_rep)

"""
if non_rep[1]==non_rep[2]:
	print("Y")
else:
	print("N")
"""
#print(const)
#print(non_rep)
#print(len(ip))
#print(len(non_rep))
ans=""
for i in range(len(non_rep)):
	count=0
	for j in range(len(ip)):
		if non_rep[i]==ip[j][1]:
			count+=int(ip[j][0])
	
	#ans.append(str(count))
	if count!=0:
		ans+=(str(count)+non_rep[i]+"+")
	#ans.append("*").append(non_rep[i]).append("+")
#print(ans,end='')
#print(ans,end='')

count=0
for i in range(len(const)):
	count+=int(const[i])
ans+=str(count)
ans=ans.replace("+-","-").replace("-+","-").replace("+1","+").replace("-1","-").replace("+0","$").replace("1","")
for i in range(2,len(ans)):
	if ans[i:i+1]=="1" and 65<=ord(ans[i+1])<=90:
		ans=ans[0:i]+ans[i+1:]
	if ans[i:i+1]=="1" and ans[i+1]=="+":
		ans=ans[0:i]+ans[i+1:]
	if ans[i:i+1]=="1" and ans[i+1]=="-":
		ans=ans[0:i]+ans[i+1:]
	if ans[i:i+1]=="1" and ans[i+1]=="$":
		ans=ans[:i]
if ans[len(ans)-1]=="$":
	ans=ans[:len(ans)-1]
print(ans)
"""
for i in range(length):
	
	for j in range(len(inplist[i])):

		
		
		
		
		
		
		if inplist[i][j][0]=='+' and 65<=ord(inplist[i][j][1])<=90:
			inplist[i][j]=inplist[i][j][0]+"1*"+inplist[i][j][1:]
		if inplist[i][j][0]=='-' and 65<=ord(inplist[i][j][1])<=90:
			inplist[i][j]=inplist[i][j][0]+"1*"+inplist[i][j][1:]
		if 65<=ord(inplist[i][j][0])<=90:
			inplist[i][j]="+1*"+inplist[i][j]
		
		if 48<=ord(inplist[i][j][0])<=57:
			inplist[i][j]="+"+inplist[i][j]
		leng=(len(inplist[i][j]))
		
		#print(leng)
		
		if 65<=ord(inplist[i][j][leng-1])<=90:
			inplist[i][j]=inplist[i][j][0:leng]+"^1"
		inplist[i][j]+="$"
		for k in range(len(inplist[i][j])):

			if 65<=ord(inplist[i][j][k])<=90 and 65<=ord(inplist[i][j][k+1])<=90:
				inplist[i][j]=inplist[i][j][:k+1]+"^1"+inplist[i][j][k+1:]

#print(inplist)
	for i in range(len(inplist)):
		for j in range(len(inplist[i])):
			#print(len(inplist[i]))
			if (50<=ord(inplist[i][j][1])<=57) or (ord(inplist[i][j][2])>90 or ord(inplist[i][j][2])<65):

			#	is_alpha=0
				for k in range(len(inplist[i][j])):
					if 65<=ord(inplist[i][j][k])<=90:
						#print("1")

						#print(inplist[i][j][k])
						inplist[i][j]=inplist[i][j][:k]+"*"+inplist[i][j][k:]
						print(inplist[i][j])
						print(len(inplist[i][j]))
						break
print(inplist)



	for i in range(len(inplist)):
		for j in range(len(inplist[i])):
			for k in range(len(inplist[i][j])):
				print(inplist[i][j][k])
				if 65<=ord(inplist[i][j][k])<=90 and 50<=ord(inplist[i][j][k+1])<=57:
					inplist[i][j]=inplist[i][j][0:k+1]+"^"+inplist[i][j][k+1:]

	
		
print(inplist)
"""

#(X+2Y)(2X2-Y2+Z)
#(2X+3Y+4Z)(XY2+X2Y+Z2)
#(A+2B2)(B+3C3)(2A+B+C)