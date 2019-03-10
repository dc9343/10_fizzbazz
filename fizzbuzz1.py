# $ python app.py
# 1つの自然数を入れてね: 1
# 1
# $ python app.py
# 1つの自然数を入れてね: 3
# Fizz
#
# $ python app.py
# 1つの自然数を入れてね: 5
# Buzz
#
# $ python app.py
# 1つの自然数を入れてね: 15
# FizzBuzz

number = int(input("1つの自然数を入れてね: "))

if number % 3 == 0 and number % 5 == 0 :
    print("FizzBuzz")

# 15の倍数で作るほうがシンプル　if number % 15 == 0:

elif number % 3 == 0 :
    print("Fizz")

elif number % 5 == 0 :
    print("Buzz")

else:
    print(number)

