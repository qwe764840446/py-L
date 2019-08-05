def recursion(n):
	result=n
	for i in range(1,n):
		result*=i
	return result
	
number=int(input('intput a integer number\n'))
result =recursion(number)
print('%d factorial is :	%d ' % (number,result))