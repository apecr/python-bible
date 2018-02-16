def about(name='Ziyad', age=23, likes='Python'):
    return "Mett {}! They are {} years old and they like {}".format(name, age, likes)


print(about('Jack', 23, 'Python'))
print(about(age=23, name='Jack', likes='Python'))
print(about('Jack', 23))
print(about('Jack', 23, 'Football'))
print(about('Jack', 29, 'Football'))
print(about())