'''
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
print("1! : ", factorial (1))
print("2! : ", factorial (2))
print("3! : ", factorial (3))
print("4! : ", factorial (4))
print("5! : ", factorial (5))
'''
'''
def f(x):
    return 2*x +1
print(f(10))
'''
'''
def mul(*values):
    total = 1
    for value in values:
         total *= value
    
    return total
print(mul(5, 7, 9, 10))
'''
'''
def function(*values, valueA, valueB):
    pass
print(function(1, 2, 3, 4, 5))
'''
'''
def function(*values, valueA=10, valueB = 20):
    pass
print(function(1, 2, 3, 4, 5))
'''
'''
def aaa(a=20,b,c):


aaa(c=20, b=10
'''
'''
def   factorial (n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1! :", factorial(1))
print("2! :", factorial(2))
print("3! :", factorial(3))
print("4! :", factorial(4))
print("5! :", factorial(5))
'''
'''
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
'''
'''
def factorial (n): 
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)


print("5!:", factorial(5))
'''

'''
def  fibonacci (n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)

print("fibonacci (1):", fibonacci(1))
print("fibonacci (2):", fibonacci(2))
print("fibonacci (3):", fibonacci(3))
print("fibonacci (4):", fibonacci(4))
print("fibonacci (5):", fibonacci(5))
'''
'''counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다." .format(n))
    global counter
    counter += 1

    if n == 1:'''
'''
tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
'''
'''
[ a, b] = [10, 20]
( c, d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
'''
'''
tuple_test = 10, 20, 30, 40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

a, b, c = 10, 20, 30
print("#괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
'''
'''
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

a, b = b, a

print("#교환 후 값")
print("a:", a)
print("b:", b)
print()
'''
'''
def test():
    return (10, 20)
a, b = test()

print("a:", a)
print("b:", b)
'''
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

















