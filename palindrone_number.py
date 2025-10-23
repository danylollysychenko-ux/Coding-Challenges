def check_palidrone_number(n):
    """My solution of turning the number into string and then checking if it's a number"""
    n = str(n)
    reversed_string = n[::-1]
    print(reversed_string)

    return reversed_string == n

print(check_palidrone_number(121))
print(check_palidrone_number(-121))
print(check_palidrone_number(10))
print(check_palidrone_number(99))
print(check_palidrone_number(67))
print(check_palidrone_number(-67))

print("-" * 15)

def is_palindrome(num):
    """AI solution which is longer by I guess reversing it using equations and then putting it back together
    One thing that I like is that it immediately returns False if a number is a negative"""
    if num < 0:
        return False  # negative numbers can't be palindromes

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10 # get last digit
        print(digit)             
        reversed_num = reversed_num * 10 + digit # build reversed number
        print(reversed_num)  
        num = num // 10 # remove last digit
        print(num)  

    return original == reversed_num

print(is_palindrome(121))
print(is_palindrome(10))
print(is_palindrome(-121))