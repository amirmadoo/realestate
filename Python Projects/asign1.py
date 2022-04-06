import random as rdm

def quest():
    words=['mango','apple','strawberry','banana','grapes','orange','kiwi','pomegranate','pear','dragonfruit','watermelon','cherry']
    word=rdm.choice(words)
    guesses=''
    turns = 3
    print("GUESS THE FRUIT NAME:")
    while turns>0:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        failed=0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("-")
                failed+=1
        if failed == 0:
            print("User Wins")
            print("Correct word:",word)
        guess = input("Guess another character:")
        if guess is not word:
            turns -= 1
            print("Wrong Guess")
            print("Incorrect Answer...", + turns, "Attempts left")
        if turns == 0:
            print("User Loose")
quest()