def print_numbers(n):
    numbers=range(n)
    for number in numbers:
        print(number)
def print_even_numbers(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(number)
def odd_or_even(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
def check_divisibility(n):
    numbers=range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is divisible by 2")
        elif number%3==0:
            print(f"{number} is divisible by 3")
        elif number%5==0:
            print(f"{number} is divisible by 5")
        elif number%7==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisible by 2,3,5,7")
def count_down(n):
    while n>0:
        print(n)
        n-=1

def count_down_to_5(n):
    while n>0:
        print(n)
        if n==5:
            break
        n-=1
def divisible_by_seven(n):
    x=1
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(x) 
# //Using else,if, elif create function called fizzbuzz that accepts a number and generates a range of numbers 
        # from 0 to n.For numbers divisible by 3 print fizz,
        # for numbers divisble by 5 print buzz
        # For other numbers, it prints fizzbuzz

def fizzbuzz(n):
     numbers=range(n)
     for num in numbers:
         if num%3==0:
             print("fizz")
         elif num%5==0:
            print("buzz")
         else:
             print("fizzbuzz")



# Using while and continue, create a function to print all the even numbers 
        # from 0-50
def print_even_numberz(n):
    x=1
    while x<=n:
        x+=1
        if x%2!=0:
            continue
        print(x)

num = int(input("Enter number: "))
result = 1
for i in range(1, num + 1):
    result = result * i

print(result)
