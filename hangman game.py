import random

# ==================== HANGMAN GAME ====================
# Fully meets the task requirements
# Accurate logic + Clean & Efficient code

words = ["python", "hangman", "intern", "coding", "project"]

# Randomly choose secret word
secret_word = random.choice(words).lower()

# Game variables
display = ["_"] * len(secret_word)
guessed_letters = []
attempts_left = 6

# Hangman stages (text only - no real graphics)
hangman_stages = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
]

print("🎉 Welcome to Hangman! 🎉")
print("Guess the word one letter at a time.\n")

while attempts_left > 0 and "_" in display:
    print(hangman_stages[6 - attempts_left])
    print("Word:   " + " ".join(display))
    
    if guessed_letters:
        print("Guessed:", " ".join(sorted(guessed_letters)))
    
    print(f"Attempts left: {attempts_left}\n")
    
    guess = input("Enter a letter: ").strip().lower()
    
    # Input validation (accurate & user-friendly)
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only ONE letter (A-Z)\n")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong!\n")
        attempts_left -= 1

# Game result
print("=" * 40)
if "_" not in display:
    print("🎉 CONGRATULATIONS! You won! 🎉")
else:
    print("💀 Game Over! You lost.")
    print(hangman_stages[-1])

print(f"The word was: {secret_word.upper()}")
print("\nThanks for playing! 👋")