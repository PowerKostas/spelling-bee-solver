import os

wordlist_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atleast_four_wordlist.txt')
with open(wordlist_path, 'r', encoding='utf-8') as file:
    words = file.readlines()


letters = list(input("Input today's letters (no spaces, first one is the center one): ").lower())
backup_letters = letters[:]
max_word_length = 0
valid_word_array = []

for i in range(len(words)):
    letters = backup_letters[:]
    word = words[i].strip().lower()
    valid_word = True

    for j in range(len(word)):
        if word[j] in backup_letters: # Using backup because original will get modified
            try:
                letters.remove(word[j]) # The goal is to have an empty array, because this word will have all the available characters (pangram)
            except ValueError: # To not show an error when trying to remove available, but already removed from the array, characters
                pass

        else:
            valid_word = False
            break


    if valid_word:
        if backup_letters[0] in letters: # Remove words that don't include the center letter
            continue

        valid_word_array.append(words[i].strip()) # words[i] instead of words, because when printing I want the first character to be capital

        if len(word) > max_word_length:
            max_word_length = len(word)

        if len(letters) == 0:
            print('Pangram!', words[i].strip())


for i in range(len(valid_word_array)):
    if len(valid_word_array[i]) == max_word_length:
        print('Biggest word (' + str(max_word_length) + ' chars):', valid_word_array[i], '\n')


print('Number of valid words:', len(valid_word_array))
input('\nEnter any key to exit the program... ')
