films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

while True:
    choice = input('What film do you want to see?: ').strip().title()
    if choice in films:
        age = int(input('How old are you?: ').strip())

        # Check user age
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print(films)
                films[choice][1] -= 1
                print(films)
            else:
                print('We don\'t have seats for the movie')
            print('Enjoy the film')
        else:
            print('You are not old enough')

    else:
        print('We don\'t have that film...')
