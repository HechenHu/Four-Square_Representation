from sympy import *
import random
t = symbols('t')

def gaussian_gcd(a, b):
    a, b = map(sympify, (a, b))
    if abs(a) < abs(b):
        a, b = b, a
    cr, ci = (a/b).as_real_imag()
    if cr.is_integer and ci.is_integer:
        return -b if b.could_extract_minus_sign() else b
    c = int(round(cr)) + I*int(round(ci))
    return gaussian_gcd(a - expand_mul(b*c), b)

def multiplicity_of_Two(n):
	if n % 2 == 1:
		return 0
	else:
		return multiplicity_of_Two(n/2)+1

def prime_into_Two_Squares(p,m):
	if (p-1)% 4 != 0:
		return None
	u = 0
	k = (p-1)/4
	try:
		for x in xrange(1,m):
			b = random.randint(0, p-1)
			u = -1*(gcd((t-b)**2 + 1,t**(2*k)-1, modulus = p)-t+b)
			if ((u**2 +1) % p == 0) and (abs(u)<p):
				u1=abs(u)
				result = list(gaussian_gcd(u1+I, p).atoms(Number))
				if len(result) == 2:
					map(lambda a: abs(a), result)
					return result
				else:
					return None	
			else:
				pass
	except:
		return None	
	
def n_Odd_Case(n):
	result = abs_list(two_times_2kPlus1_Case(2 * n))
	odd = filter(lambda a: a % 2 ==1, result)
	x = odd[0]
	y = odd[1]
	even = filter(lambda a: a % 2 ==0, result)
	z = even[0]
	w = even[1]
	temp = [(x+y)/2,(x-y)/2,(w+z)/2,(w-z)/2]
	map(lambda a: abs(a), temp)
	return temp
	
def two_times_2kPlus1_Case(n):
	result = None
	x=0
	y=0
	while result == None:
		x = random.randint(0,floor(sqrt(n)))
		y = random.randint(0,floor(sqrt(n)))
		if n - x**2 - y**2 > 0:
			if n - x**2 - y**2 == 2:
				return [x,y,1,1]
			else :
				result = prime_into_Two_Squares( n - x**2 - y**2 ,2)
				if result != None:
					if ((x ** 2) + (y ** 2) + (result[0] ** 2) + (result[1] ** 2)) == n:
						result.append(x)
						result.append(y)
						return result
					else:
						result = None
			
		
def four_Square(n):
	if n % 2 == 1:
		return n_Odd_Case(n)
	else:
		d = multiplicity_of_Two(n)
		if d % 2 ==1:
			s = 2 ** (d-1)
			result = [i * int(sqrt(s)) for i in two_times_2kPlus1_Case(n/s)]
			return result
		else:
			temp = four_Square(2*n)
			map(lambda a: abs(a), temp)
			if len(filter(lambda a: a % 2 ==1, temp))!=0 and len(filter(lambda a: a % 2 ==1, temp))!=4:
				odd = filter(lambda a: a % 2 ==1, temp)
				even = filter(lambda a: a % 2 ==0, temp)
				x = odd[0]
				y = odd[1]

				z = even[0]
				w = even[1]
				return [(x+y)/2,(x-y)/2,(w+z)/2,(w-z)/2]
			else:
				x = temp[0]
				y = temp[1]
				z = temp[2]
				w = temp[3]
				return [(x+y)/2,(x-y)/2,(w+z)/2,(w-z)/2]


print four_Square(71382)

