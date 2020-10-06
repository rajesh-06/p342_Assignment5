import mymodule as mm
import math as m
def q1a(x):# Question 1(a)
	f= m.log(x)-m.sin(x)
	return f
	
def q1b(x):#Q.1(b)
	f = -x-m.cos(x)
	return f
	
#printing and storing iteration number and absolute error	
def printing(arr):
	f.write('Iteration number	Absolute Error\n')
	for i in range(len(arr)):
		f.write('\n')
		f.write(str(i+1))
		f.write('	')
		f.write(str(arr[i]))
	f.close()

#Question 1(a)		
print("Question 1(a)")	
print('Give 2 number to bracket the roots')
			
a=float(input('lower bound: '))
b=float(input('upper bound: '))
a,b=mm.bracket(q1a,a,b)#bracketing the roots
print('bracketing to',(a,b))

#bisection
c,arr1 = mm.bisection(q1a,a,b)
f = open('q1a_bisection.txt', 'r+')
printing(arr1)
print('Root between ',a,' and ',b,' is ',c)

#false position
d,arr2=mm.fal_pos(q1a,a,b)
print('Root between ',a,' and ',b,' is ',d)
f = open('q1a_fal_pos.txt', 'r+')
printing(arr2)

#newton raphson
e,arr3=mm.newtraph(q1a,1.5)
print('Root between ',a,' and ',b,' is ',e)
f = open('q1a_newtraph.txt', 'r+')
printing(arr3)

#-------------------------------
#Question 1(b)
print("\nQuestion 1(b)")				
print('Give 2 number to bracket the roots')
a=float(input('Lower bound: '))
b=float(input('Upper bound: '))
a,b=mm.bracket(q1b,a,b)
print('Bracketing to',(a,b))

#bisection
c,arr4 = mm.bisection(q1b,a,b)
print('Root between ',a,' and ',b,' is ',c)
f = open('q1b_bisection.txt', 'r+')
printing(arr4)

#false position
d,arr5=mm.fal_pos(q1b,a,b)
print('Root between ',a,' and ',b,' is ',d)
f = open('q1b_fal_pos.txt', 'r+')
printing(arr5)

#newton raphson
e,arr6=mm.newtraph(q1b,0)
print('Root between ',a,' and ',b,' is ',e)
f = open('q1b_newtraph.txt', 'r+')
printing(arr6)

#-------------------------------
#Question 2
print('\nQuestion 2')
#q2= [1,-3,-7,27,-18]
#coefficient should be in order x^n to x^0
with open('q2.txt', 'r') as f:
	for line in f:
		q2=[float(num) for num in line.split(',')]

print('Roots of the polynomial are: ',mm.root_poly(q2))

