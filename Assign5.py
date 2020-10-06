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

'''
Question 1(a)
Give 2 number to bracket the roots
lower bound: 1
upper bound: 2.5
bracketing to (1.0, 2.5)
SR.No.  Absolute error
1       0.375
2       0.1875
3       0.09375
4       0.046875
5       0.0234375
6       0.01171875
7       0.005859375
8       0.0029296875
9       0.00146484375
10       0.000732421875
11       0.0003662109375
12       0.00018310546875
13       9.1552734375e-05
14       4.57763671875e-05
15       2.288818359375e-05
16       1.1444091796875e-05
17       5.7220458984375e-06
18       2.86102294921875e-06
19       1.430511474609375e-06
20       7.152557373046875e-07
Root between  1.0  and  2.5  is  2.219106912612915
SR.No.  Absolute error
1       0.12083139147655109
2       0.00885021070524905
3       0.0006054850873797868
4       4.12134570089151e-05
5       2.804290035296475e-06
Root between  1.0  and  2.5  is  2.2191069441750955SR.No.  Absolute error
1       0.258681675945311
2       0.015599262240227674
3       6.802249489634704e-05
4       1.2987579900425317e-09
Root between  1.0  and  2.5  is  2.219107148913746

Question 1(b)
Give 2 number to bracket the roots
Lower bound: -1
Upper bound: 0
Bracketing to (-1.0, 0.0)
SR.No.  Absolute error
1       0.25
2       0.125
3       0.0625
4       0.03125
5       0.015625
6       0.0078125
7       0.00390625
8       0.001953125
9       0.0009765625
10       0.00048828125
11       0.000244140625
12       0.0001220703125
13       6.103515625e-05
14       3.0517578125e-05
15       1.52587890625e-05
16       7.62939453125e-06
17       3.814697265625e-06
18       1.9073486328125e-06
19       9.5367431640625e-07
Root between  -1.0  and  0.0  is  -0.7390851974487305
SR.No.  Absolute error
1       0.0512256402876089
2       0.002646358352059175
3       0.00013277491431251676
4       6.651568897342308e-06
Root between  -1.0  and  0.0  is  -0.7390847824489231
SR.No.  Absolute error
1       0.24963615117193894
2       0.011250958770036013
3       2.7756674668144576e-05
4       1.6825085769056614e-10
Root between  -1.0  and  0.0  is  -0.7390851332151607

Question 2
Roots of the polynomial are:  [3.0003874103093633, 1.999989427522515, 0.9994320364690461, -2.999808874300924]

[Program finished]'''
