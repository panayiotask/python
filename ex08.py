# 1
def double_it(number):
    return number*2

print(double_it(7))
print(double_it(4.76))
print(double_it('hi'))

# 2
def calc_hypo(a,b): # function calculating the hypotenuse
    hypo=(a**2+b**2)**1/2
    return hypo

print(calc_hypo(3,4)) # checking the function

# 3, Adding checks to the function
def calc_hypo(a,b): 
    if type(a) not in (float, int) or type(b) not in (float, int):
        print('Bad argument')
        return False
    if a < 0 or b < 0:
        print('Bad argument')
        return False
    hypo=(a**2+b**2)**1/2
    return hypo

print(calc_hypo(-4,5)) # checking whether the checks work
print(calc_hypo('hi',4))
print(calc_hypo(3,4))

