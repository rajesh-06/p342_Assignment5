import mymodule as mm
import math as m
def q1a(x):
	f= m.log(x)-m.sin(x)
	return f
	
def q1a1(x):
	f= 1/x-m.cos(x)
	return f
	
def q1b(x):
	f = -x-m.cos(x)
	return f
	
def q1b1(x):
	f = -1+m.sin(x)
	return f	
	
def poly(f,x):
	value=0
	n = len(f)
	for i in range(n):
		value+=f[i]*(x**(n-1-i))
	return value
	
def der1_poly(f,x):
	value=0
	n= len(f)
	for i in range(n-1):
		value+=f[i]*(n-1-i)*(x**(n-i-2))
	return value

def der2_poly(f,x):
	value=0
	n=len(f)
	for i in range(n-2):
		value+=f[i]*(n-1-i)*(n-2-i)*(x**(n-i-3))
	return value

		
print("question 1a")				
a=1
b=2.5
a,b=mm.bracket(q1a,a,b)
print(a,b)

c,arr1 = mm.bisection(q1a,a,b)
f = open('q1a_bisection.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr1)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr1[i]))
f.close()

print(c)

d,arr2=mm.fal_pos(q1a,a,b)
print(d)

f = open('q1a_fal_pos.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr2)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr2[i]))
f.close()


e,arr3=mm.newtraph(q1a,q1a1,1.5)
print(e)
f = open('q1a_newtraph.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr3)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr3[i]))
f.close()
	
print("question 1b")				
a=-1
b=0
a,b=mm.bracket(q1b,a,b)
print(a,b)
c,arr4 = mm.bisection(q1b,a,b)
print(c)
f = open('q1b_bisection.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr4)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr4[i]))
f.close()

d,arr5=mm.fal_pos(q1b,a,b)
print(d)
f = open('q1b_fal_pos.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr5)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr5[i]))
f.close()

e,arr6=mm.newtraph(q1b,q1b1,0)
print(e)
f = open('q1b_newtraph.txt', 'r+')
f.write('Iteration number	Absolute Error\n')
for i in range(len(arr6)):
	f.write('\n')
	f.write(str(i+1))
	f.write('	')
	f.write(str(arr6[i]))
f.close()
