from random import randint  # Do not delete this line


def displayIntro():
    print("""_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________""")


def displayEnd(result):
    if result:
        print("""________________________________________________________________________
              _                                  _                          
             (_)                                (_)                         
    __      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
     \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
      \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
               | |   (_)    | |                  | (_)                      
            ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
           / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
          | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
           \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
    ________________________________________________________________________""")
    else:
        print("""
     __     __           _           _   _                                    
     \ \   / /          | |         | | | |                                   
      \ \_/ /__  _   _  | | ___  ___| |_| |                                   
       \   / _ \| | | | | |/ _ \/ __| __| |                                   
        | | (_) | |_| | | | (_) \__ \ |_|_|                                   
        |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
            _______ _                                        _ _          _ _ 
           |__   __| |                                      | (_)        | | |
              | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
              | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
              | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
              |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
    __________________________________________________________________________""")


def displayHangman(state):
    if state == 5:
        print("""   
         ._______.   
         |/          
         |           
         |           
         |           
         |           
         |           
     ____|___        
                         """)

    elif state == 4:
        print("""     
         ._______.   
         |/      |   
         |           
         |           
         |           
         |           
         |           
     ____|___        
               """)
    elif state == 3:
        print("""     
         ._______.   
         |/      |   
         |      (_)  
         |           
         |           
         |           
         |           
     ____|___        
                   """)
    elif state == 2:
        print("""    
         ._______.   
         |/      |   
         |      (_)  
         |       |   
         |       |   
         |           
         |           
     ____|___        
                     """)
    elif state == 1:
        print("""  
         ._______.   
         |/      |   
         |      (_)  
         |      \|/  
         |       |   
         |           
         |           
     ____|___        
               """)
    elif state == 0:
        print("""
         ._______.   
         |/      |   
         |      (_)  
         |      \|/  
         |       |   
         |      / \  
         |           
     ____|___      """)


def moveEachLineToList(txtFile):
    myFile2 = open(txtFile)
    resultList = []
    for line in myFile2:
        resultList.append(line.strip())
    myFile2.close()
    return resultList


def numberOfWords(txtFile):
    len = 0
    myFile1 = open(txtFile)
    for line in myFile1:
        len += 1
    myFile1.close()
    return len


def getWord():
    indexOfHiddenWord = randint(0, numberOfWords("C:/Users/Ника/Desktop/hangman-words.txt"))
    hiddenWord = moveEachLineToList("C:/Users/Ника/Desktop/hangman-words.txt")[indexOfHiddenWord]
    return hiddenWord


def valid(c):
    if c.isalpha():
        if c.islower():
            if len(c)==1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def play():
    hiddenWord = getWord()
    guessingWord = ''
    state = 5
    for i in hiddenWord:
        guessingWord = guessingWord + '$'
    while state >= 1:
        displayHangman(state)
        print('Guess the word:',guessingWord)
        usersLetter = input("Enter the letter: ")
        if valid(usersLetter):
            if usersLetter in hiddenWord:
                    for i in range(0,len(hiddenWord)):
                        convertedGuessingWord = list(guessingWord.strip())
                        convertedHiddenWord = list(hiddenWord.strip())
                        if convertedHiddenWord[i]==usersLetter:
                            convertedGuessingWord[i]=usersLetter
                            guessingWord = ''.join(convertedGuessingWord)
                        if hiddenWord == guessingWord:
                            print("Hidden word was:", hiddenWord)
                            return True
            else:
                state-=1
        else:
            print('Incorrect input!')
    displayHangman(0)
    print("Hidden word was:",hiddenWord)
    return False

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        checkTheAnswerOfTheUser = str(input("Do you want to play again? (yes/no)")).lower()
        if checkTheAnswerOfTheUser == "no":
            break
        elif checkTheAnswerOfTheUser == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    hangman()
