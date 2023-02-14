def factorial(num):
	x = 1
	for i in range(num,0,-1):
		if num != 0:
			x = i * x
			print(i)
	return x
print(factorial(3))		



