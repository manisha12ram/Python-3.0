# Sample code demonstrating the use of for loops in Python
# without using class or function definitions

result = []
# print all numbers from 1 to 10 using a for loop
result = [x for x in range(1, 11)]
print(result)

# print numbers from 10 down to 1 in reverse order
result = [x for x in range(10, 0, -1)]
print(result)

# Print all even numbers between 1 and 100
result = [x for x in range(2, 101, 2)]
print(result)

# Print all odd numbers between 1 and 100
result = [x for x in range(1, 101, 2)]
print(result)

# Print the multiplication table of a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ---------------------------------------------------- 
# with using class or function definitions

class NumberPrinter:
    def __init__(self):
        self.result = []
        self.num= int(input("Enter a number: "))
    def print_1_to_10(self):
        self.result = [x for x in range(1, 11)]
        print(self.result)

    def print_10_to_1(self):
        self.result = [x for x in range(10, 0, -1)]
        print(self.result)

    def print_even_numbers(self):
        self.result = [x for x in range(2, 101, 2)]
        print(self.result)

    def print_odd_numbers(self):
        self.result = [x for x in range(1, 101, 2)]
        print(self.result)

    def multiplication_table(self):
        for i in range(1, 11):
            print(f"{self.num} x {i} = {self.num * i}")


# Example usage
if __name__ == "__main__":
    printer = NumberPrinter()
    printer.print_1_to_10()
    printer.print_10_to_1()
    printer.print_even_numbers()
    printer.print_odd_numbers()
    printer.multiplication_table()


# Calculate and print the factorial of a given number
def factorial_loop(n):  
    if n < 0:
        return "Undefined for negative numbers"  
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
fnum = int(input("Enter a number: "))
print(factorial_loop(fnum))  

# Calculate and print the factorial of every number from 1 to n.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(f"Factorial of {i}: {factorial_loop(i)}")


# Print all prime numbers between 1 and 100.
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print("Prime numbers between 1 and 100:")
print(primes)

# Check whether the given number is a prime number.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Print the Fibonacci series up to the required number of terms.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print(f"{b} is a sum of fibinoci series")
# Find and print the sum of the Fibonacci series.
# n = int(input("Enter the number of terms: "))
