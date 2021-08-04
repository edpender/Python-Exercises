#Write a program that asks a user for a number and then tests whether it is prime or not and prints out “The number is prime” or “The number is not prime”.

num = 29
flag = False
if num >1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
