import random
import os

def number_of_attempts_left(attempts, flag):
    
        
    if flag==False:
        
        attempts = attempts- 1 
    print(f"Attempts remaining: {attempts}")       
    return attempts


def check_letter(letter, word):
    flag = False
    if letter not in word:
        print(f"{letter} is not in the word!")
        flag = False
    else:
        print(f"{letter} is in the word!")
        flag = True
        
    return flag


#if the guess is true flag is True and we should reveal the letter
def reveal_letter(letter, flag, crypted_word, word):
    if flag==True:
        for i in range(len(word)):
            if crypted_word[i] == "*":
                if word[i] == letter:
                    crypted_word[i] = letter
            
    return crypted_word



def previous_guess(letter, guesses):
    if letter is not None:
        if letter not in guesses:
            guesses.append(letter)
            print("Previous Guesses : ", *guesses, sep= ' ')
        else:
            print(f"{letter} has been guessed before!")
        
    return guesses
    

def open_word_file():
     #opening the file with words
    PATH =  r"."
    file_name = os.path.join(PATH, "working_file.txt")
    fp = open(file_name, 'r')
    return fp

def start_game():
    flag0 = True

    while(flag0==True):
        print("Enter the number of incorrect attempts you want. [1-25]")
        attempts = input()
        try:
            attempts = int(attempts)
            flag0=False
        except:
            print(f"Sorry, {attempts} is not a number.")
            flag0=True
            continue

    flag0 = True
    
    while(flag0 == True):
        print("How long do you want the word to be?[1-18]")
        wordlength = input()
        try:
            wordlength = int(wordlength)
            flag0 = False
        except:
            print(f"Sorry, {wordlength} is not a number.")
            flag0 = True
            continue
        print("Selecting a word....")
    
    return attempts, wordlength






def main():
   
    attempts, wordlength = start_game()
    fp = open_word_file()

   
    
    #we need the word of the given length
    #so we have to filter them out
    words = list()
   
    for line in fp:
        if len(line.rstrip()) == wordlength:    #\n in the word; and searching for the word of given length
            words.append(line.rstrip())
    
    rand_word = random.randint(0, len(words))  #take a random word of len given      
    word = words[rand_word].rstrip()
    crypted_word = "*" * len(word)      #encryt the word
    print("Word:",crypted_word)
    attempts = number_of_attempts_left(attempts, flag=True)

    #guesses is the list of previous guesses
    guesses = list()
    guesses = previous_guess(letter=None, guesses=guesses)
    print("Choose the next letter:")
    letter = input()
    flag = check_letter(letter, word)
    flag = check_letter(letter, word)
    if flag==True:
        crypted_word = reveal_letter(letter, flag, list(crypted_word), word)
        print(*crypted_word)        
    attempts = number_of_attempts_left(attempts, flag=flag)
    while(attempts > 0):
        
        
        guesses = previous_guess(letter, guesses)
        print("Choose the next letter:")
        letter = input()
        flag = check_letter(letter, word)
        if flag==True:
            crypted_word = reveal_letter(letter, flag, list(crypted_word), word)
            print(*crypted_word)
        attempts = number_of_attempts_left(attempts, flag=flag)
        if ''.join(crypted_word) == word:
            print("You are really good!\n Good guesses!!\n Congratulations, you won!!\n")
            break
        
    


if __name__ == '__main__':
    main()