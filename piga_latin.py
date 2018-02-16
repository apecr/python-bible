# get sentences from user

original = input('Sentence: ').strip().lower()
# split sentence into words

words = original.split()
print(words)

# loop thorugh words and convert to pig latin

new_words = []

# if starts wth vowel, just add "yay"

for word in words:
    if word[0] in "aeiou":
        print('Vocal', word)
        new_words.append(word + "yay")
    elif word[0] in "bcdfghijklmnñpqrstvwxyz":
        print('Consonant', word)
        first_vowel = 0
        for letter in word:
            if letter not in "aeiou":
                first_vowel += 1
            else:
                break
        new_words.append(word[first_vowel:]+word[:first_vowel].title()+"ay")

# Otherwise, move the first consonant cluster to end, and add "ay

# stick words back together

# output the final string
print(' '.join(new_words))