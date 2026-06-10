import random

words = ["project" , "internship" , "college" , "laptop" , "python"]

print("=====HANGMAN GAME=====")
player_name = input("enter your name: ")

score = 0

while True:
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print(f"\nGood luck,{player_name}!")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_"

        print("\nword:", display_word)

        if "_" not in display_word:
            print("\n🎉 congratulations!")
            print("you guessed the word:",word)        
            score += 10
            print("🏆score:",score)
            break

        guess = input("enter the letter: ").lower()    

        if len(guess) != 1 or not guess.isalpha():
             print("⚠ Please enter only one letter.")
             continue

        if guess in guessed_letters:
            print("you have already guessed this letter.")     
            continue

        guessed_letters.append(guess)    

        if guess in word:
            print("✅ Correct Guess!")
        else:
            attempts -= 1
            print("❌ wrong guess!")    
            print("Remaining Attempts:", attempts)

        if attempts == 0:
            print("\n💀 Game Over!")    
            print("The word was:",word)
            print("🏆 Final score",score)

    choice = input("\ndo you want to play again? (yes/no): ").lower()    

    if choice != "yes":
        print("\nThank you for playing!")
        print(f"Final score of{player_name}:{score}")
        break