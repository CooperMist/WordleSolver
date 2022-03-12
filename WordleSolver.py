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
    start = input("Start a game? (y/n): ")

    while True:
        if start.upper() == "N":
            break
        
        #Get words with used letters found
        letter = input("Input a letter that is used.  If there are no more letters to enter hit enter.\n")
        while letter != "":
            if letter[0].isalpha():
                letter = letter[0].upper()
                words = add_words_with_letter(words, letter)
            else:
                print("Invalid Input")
            letter = input("Input a letter that is used.  If there are no more letters to enter hit enter.\n")


        #Remove words with unused letters
        letter2 = input("Input a letter that is not used.  If there are no more letters to enter hit enter.\n")
        while letter2 != "":
            if letter2[0].isalpha():
                letter2 = letter2[0].upper()
                words = remove_words_with_letter(words, letter2)
            else:
                print("Invalid Input")
            letter2 = input("Input a letter that is not used.  If there are no more letters to enter hit enter.\n")


        #Remove words with used letters in wrong positions
        
        res = input("Input a letter that is used, in the wrong position.  If there are no more letters to enter hit enter. (letter, #position)\n")
        while res != "":
            if res[0][0].isalpha() & res[1].isdigit():
                res = res.split()
                words = remove_words_with_letter_at_position(words, res[0][0].upper(), int(res[1]))
            else:
                print("Invalid Input")
            res = input("Input a letter that is used, in the wrong position.  If there are no more letters to enter hit enter. (letter, #position)\n")


        #Remove words without used letters in the right positions
        res = input("Input a letter that is used, in the right position. If there are no more letters to enter hit enter. (letter, #position)\n")
        while res != "":
            if res[0][0].isalpha() & res[1].isdigit():
                res = res.split()
                words = remove_words_with_letter_not_at_position(words, res[0][0].upper(), int(res[1]))
            else:
                print("Invalid Input")
            res = input("Input a letter that is used, in the right position.  If there are no more letters to enter hit enter. (letter, #position)\n")

        #Print Resulting List
        print ("Here is a list of the posible word choices remaining: \n")
        print(words)

        start = input("Do yow want to continue playing the game. (y/n): ")
        #Puts new list in a file
        #write_list_to_file (words)



main()