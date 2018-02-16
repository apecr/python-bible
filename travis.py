known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Enma', 'Fred', 'Georgie', 'Harry']

print(len(known_users))

while True:
    print('Hi! My name is Travis')
    name = input('What is your name?: ')

    if name in known_users:
        print('name recognised')
    else:
        print('name NOT recognised')