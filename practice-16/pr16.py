import math

def check(text):
	while(True):
		try:
			num = float(input(text))
			assert num > 0
		except (ValueError, AssertionError):
			print('This is not valid option.')
			continue
		else:
			return num
			break
			
def triangle_ineq(func):
	def inner(*args, **kwargs):
		while (True):
			try:
				a = check('Enter the first side: ')
				b = check('Enter the second side: ')
				c = check('Enter the third side: ')
				assert a + b > c
				assert a + c > b
				assert b + c > a
			except AssertionError:
				print('This sides is not valid for triangle')
				continue
			else:
				print(f'Area of a thiangle : {func(a, b, c)}')
				break
	return inner
	
@triangle_ineq	
def area_calculation(a = None, b = None, c = None):
	p = round((a + b + c) / 2, 2)
	return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)

area_calculation()
