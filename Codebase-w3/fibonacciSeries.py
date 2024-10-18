# implementing the fibonacci series with loop and recursion

# using for loop

num1 = 0
num2 = 1

print(num1)
print(num2)

for fibo in range(18):
    newfibo = num1 + num2
    print(newfibo)
    num1 = num2
    num2 = newfibo


# using the recursion
print("-------")
print(0)
print(1)
count = 2


def fibonacci(number1, number2):
    global count
    if count <= 19:
        newFibo = number1 + number2
        print(newFibo)
        number1 = number2
        number2 = newFibo
        count += 1
        fibonacci(number1, number2)
    else:
        return


fibonacci(0, 1)


# finding the nth fibonacci number using recursion
# nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number n:
# F(n)=F(n−1)+F(n−2)

print("--------------new--------------")


def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)


print(F(3))
