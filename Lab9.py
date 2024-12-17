#Task 1

def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = find_second_largest(numbers)
print(f"The second largest number is: {result}")


#/////////////////////////////////////////////////////

#Task 2

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")


#/////////////////////////////////////////////////////

#Task 3

def validate_password(password):
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    is_long_enough = len(password) >= 8
    return has_upper and has_digit and is_long_enough

password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")

#/////////////////////////////////////////////////////

#Task 4

def is_palindrome(string):
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#//////////////////////////////////////////////////////////

#Task 5

def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = max(numbers)
missing_number = find_missing_number(numbers, n)
print(f"The missing number is: {missing_number}")

#/////////////////////////////////////////////////////////////

#Task 6

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#//////////////////////////////////////////////////////////////

#Bonus Task: 

def word_frequency(sentence):
    words = sentence.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

sentence = input("Enter a sentence: ")
frequencies = word_frequency(sentence)
print("Word frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
