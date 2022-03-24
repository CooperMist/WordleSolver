#Created by Cooper Mistishin on 3/10/2022
#The list of 12478 Words in "WordDictionary.txt" were retrieved from "https://www.bestwordlist.com/5letterwords.htm"

#Creates a list from the "WordDictionary.txt" file.
def create_list() :
    words = []
    with open("WordDictionary.txt") as f:
        line = f.readline()
        words = line.split(" ")
    f.close()
    return words

#Creates a list of words that have a given letter, using the given list.
def add_words_with_letter(words, letter):
    new_words = [x for x in words if letter in x]
    return new_words

#Creates a list of words that do not have a given letter, using the given list.
def remove_words_with_letter(words, letter):
    new_words = [x for x in words if letter not in x]
    #print(words)
    #for word in words:
        #if letter in word :
            #word
        #else :
            #new_words.append(word)
    #print(new_words)
    return new_words

#Creates a list of words that do not have a given letter, at the given position, using the given list.
def remove_words_with_letter_at_position (words, letter, position):
    new_words = []
    for word in words:
        if word[position-1] == letter :
            word = " "
        else :
            new_words.append(word)
    return new_words

#Creates a list of words that have a given letter, at the given position, using the given list.
def remove_words_with_letter_not_at_position (words, letter, position):
    new_words = []
    for word in words:
        if word[position-1] == letter :
            new_words.append(word)            
    return new_words

#Writes the give list to the "word_of_the_day.txt" file.
def write_list_to_file (words):
    f = open("word_of_the_day.txt", "w")
    for word in words :
        f.write(word + " ")
    f.close()

def main ():
    #Create Word list
    words = create_list()   
    used_letters = []  
    start = input("Start a game? (y/n): ")
    restart = "N"

    while True:
        if start.upper() == "N":
            break

        if restart.upper() == "Y":
            words = create_list()   
            used_letters = [] 

        #Get words with used letters found
        #TODO Need to make a list of used letters and make sure they are not inputed as unused letters
        letter = input("Input a letter that is used.  If there are no more letters to enter hit enter.\n")
        while letter != "":
            if len(letter.strip()) == 1:
                if letter.isalpha():
                    letter = letter.upper()
                    used_letters.append(letter)
                    words = add_words_with_letter(words, letter)
                else:
                    print("Invalid Input, input is not a letter")
            else:
                print("Invalid Input, only one letter accepted at a time")
            letter = input("Input a letter that is used.  If there are no more letters to enter hit enter.\n")


        #Remove words with unused letters
        letter2 = input("Input a letter that is not used.  If there are no more letters to enter hit enter.\n")
        while letter2 != "":
            if len(letter2.strip()) == 1:
                if letter2.isalpha():
                    letter2 = letter2.upper()
                    if letter2 not in used_letters:                        
                        words = remove_words_with_letter(words, letter2)
                    else:
                        print("Invalid Input, the letter inputed is a used letter.")
                else:
                    print("Invalid Input, input is not a letter.")
            else:
                print("Invalid Input, only one letter accepted at a time.")
            letter2 = input("Input a letter that is not used.  If there are no more letters to enter hit enter.\n")


        #Remove words with used letters in wrong positions
        
        res = input("Input a letter that is used, in the wrong position.  If there are no more letters to enter hit enter. (letter, position#)\n")
        while res != "":
            if res.find(", ") != -1 and len(res) == 4:
                res = res.strip().split()
                if res[0][0].isalpha() and res[1].isdigit():
                    if int(res[1]) >= 1 and int(res[1]) <= 5:               
                        words = remove_words_with_letter_at_position(words, res[0][0].upper(), int(res[1]))
                    else:
                        print("Invalid Input, the position inputed is not valid. Valid positions are 1, 2, 3, 4, & 5")
                else:
                    if res[0][0].isalpha():
                        print("Invalid Input, the letter is not a letter")
                    if res[1].isdigit():
                        print("Invalid Input, the position is not a number")
            else:
                    print("Invalid Input, the input is not in the correct format example: a, 5")
            res = input("Input a letter that is used, in the wrong position.  If there are no more letters to enter hit enter. (letter, position#)\n")


        #Remove words without used letters in the right positions
        res = input("Input a letter that is used, in the right position. If there are no more letters to enter hit enter. (letter, #position)\n")
        while res != "":
            if res.find(", ") != -1 and len(res) == 4:
                res = res.strip().split()
                if res[0][0].isalpha() and res[1].isdigit():  
                    if int(res[1]) >= 1 and int(res[1]) <= 5:               
                        words = remove_words_with_letter_not_at_position(words, res[0][0].upper(), int(res[1]))
                    else:
                        print("Invalid Input, the position inputed is not valid. Valid positions are 1, 2, 3, 4, & 5")
                else:
                    if res[0][0].isalpha():
                        print("Invalid Input, the letter is not a letter")
                    if res[1].isdigit():
                        print("Invalid Input, the position is not a number")
            else:
                    print("Invalid Input, the input is not in the correct format example: a, 5")
            res = input("Input a letter that is used, in the right position.  If there are no more letters to enter hit enter. (letter, #position)\n")

        #Print Resulting List
        print ("Here is a list of the posible word choices remaining: \n")
        print(words)

        start = input("Do you want to continue playing the game. (y/n): ")
        if start.upper() == "N":
            break
        
        restart = input("Do you want to start a new game. (y/n): ")
        #Puts new list in a file
        #write_list_to_file (words)



main()