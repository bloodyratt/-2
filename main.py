Завдання 1:


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False



Завдання 2:


def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count



Завдання 3:


def factorial(number):
    result = 1
    if number < 0:
        return "Факторіал невід'ємного числа не може бути обчислений."
    elif number == 0:
        return result
    else:
        for i in range(1, number + 1):
            result *= i
        return result

