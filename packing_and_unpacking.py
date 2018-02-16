print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)


def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add(1,2,3,4,5,6,7,8,9))


def about(name='Ziyad', age=23, likes='Python'):
    return "Mett {}! They are {} years old and they like {}".format(name, age, likes)


dictionary = {
    'age': 24,
    'name': 'Jhon',
    'likes': 'Basketball'
}

print(about(**dictionary))


def foo(**kwargs):
    for key, value in kwargs.items():
        print('{}:{}'.format(key, value))


foo(huda= 'Female', ziyad = 'male')