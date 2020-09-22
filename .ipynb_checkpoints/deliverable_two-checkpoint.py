import random 

words = [
    'beethoven',
    'Mozart',
    'Rachmaninov',
    'Mahler',
    'Chopin'
]



def hangman (lst):
    guess = []
    random_word = random.choice(lst)
    random_word1 = random_word.upper()
    random_list = list(random_word1)
    underscore = '_' * len(random_word1)
    result = ' '.join(list(underscore))
    print(result)
    guess_letter = []
    secret_word = []
    guess_left = 7

    while guess_left >= 2:
        guess_input = input('Guess a Letter: ').upper()
        guess.append(guess_input)
        print('letters you have guessed already', guess)
        print("Amount of guesses you have left", guess_left)
        if guess_input in random_list:
            print("Great!, the word has the letter: " + guess_input)
            index = random_list.index(guess_input)
            underscore = print_letter(index, random_list, underscore)
            random_list = change_letter(index, random_list)
            check_list = (random_list)
        else:
            guess_left -= 1
            print('Sorry that letter was incorrect')
            if guess_left < 7:
                print(('''
       ______
      |      | 
      |      O
      |
      |
    |'''))
                if guess_left < 6:
                    print(('''
       ______
      |      | 
      |      O
      |      |
      |
    |'''))
                    if guess_left < 5:
                        print(('''
       ______
      |      | 
      |      O
      |      |-
      |
    |'''))
                        if guess_left < 4:
                            print(('''
       ______
      |      | 
      |      O
      |     -|-
      |
    |'''))
                            if guess_left < 3:
                                print(('''
       ______
      |      | 
      |      O
      |     -|-
      |      /
    |'''))
                                if guess_left < 2:
                                    print(('''
       ______
      |      | 
      |      O
      |     -|-
      |     /|
    |'''))


def print_letter(idx, word, underscore):
    result = list(underscore)
    # print('RESULT',result)
    for i in range(len(word)):
        if i == idx:
            result[i] = word[i]
    underscore = ''.join(result)
    res = ' '.join(list(underscore)) 
    print(res)
    # print(underscore)
    return underscore 

def change_letter(index, lst):
    for i in range(len(lst)):
        if i == index:
            lst[i] = '.'
    return lst 

def check_list(random_list):
    ele = random_list[0]
    check = True
    for item in random_list:
        if ele != item:
            check = False
            break
    if (check == True):
        # print('YOU WIN')
        quit()




hangman(words)


    

