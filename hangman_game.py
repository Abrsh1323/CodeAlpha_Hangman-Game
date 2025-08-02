import random
import os
import time

class HangmanGame:
    """A professional implementation of the classic Hangman word guessing game."""
    
    def __init__(self):
        """Initialize the game with default settings and word list."""
        self.words = [
            "PYTHON", 
            "CODING", 
            "ALGORITHM", 
            "DEVELOPER", 
            "COMPUTER"
        ]
        self.max_incorrect = 6
        self.reset_game()
    
    def reset_game(self):
        """Reset the game state for a new round."""
        self.target_word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.game_over = False
        self.game_won = False
    
    def clear_screen(self):
        """Clear the console screen for better visual presentation."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_title(self):
        """Display the game title with decorative ASCII art."""
        print(r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
        """)
        print("="*50)
        print("       WELCOME TO PROFESSIONAL HANGMAN")
        print("="*50)
        print("Guess the word by entering one letter at a time.")
        print(f"You can make up to {self.max_incorrect} incorrect guesses.\n")
    
    def display_hangman(self):
        """Display the hangman ASCII art based on current incorrect guesses."""
        stages = [
            # Final state: game over
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # 5 incorrect
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # 4 incorrect
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # 3 incorrect
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # 2 incorrect
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # 1 incorrect
            """
               --------
               |      |
               |      O
               |      
               |      
               |     
               -
            """,
            # Initial empty state
            """
               --------
               |      |
               |      
               |      
               |      
               |     
               -
            """
        ]
        print(stages[self.max_incorrect - self.incorrect_guesses])
    
    def display_word(self):
        """Display the current state of the word with guessed letters revealed."""
        display = ""
        for letter in self.target_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display
    
    def display_game_status(self):
        """Display the current game status including hangman, word, and statistics."""
        self.clear_screen()
        self.display_title()
        
        print("Word to guess:", self.display_word())
        print("\nIncorrect guesses:", self.incorrect_guesses, "/", self.max_incorrect)
        
        if self.guessed_letters:
            print("Guessed letters:", " ".join(sorted(self.guessed_letters)))
        
        self.display_hangman()
    
    def get_valid_guess(self):
        """Get and validate a letter guess from the user."""
        while True:
            guess = input("Enter a letter: ").strip().upper()
            
            if not guess:
                print("⚠️  Please enter a letter.")
                continue
                
            if len(guess) != 1:
                print("⚠️  Please enter exactly one letter.")
                continue
                
            if not guess.isalpha():
                print("⚠️  Please enter a letter from A-Z.")
                continue
                
            if guess in self.guessed_letters:
                print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
                continue
                
            return guess
    
    def process_guess(self, guess):
        """Process the player's guess and update game state."""
        self.guessed_letters.append(guess)
        
        if guess in self.target_word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            # Check if player has won
            if all(letter in self.guessed_letters for letter in self.target_word):
                self.game_won = True
                self.game_over = True
        else:
            self.incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is not in the word.")
            # Check if player has lost
            if self.incorrect_guesses >= self.max_incorrect:
                self.game_over = True
    
    def display_game_result(self):
        """Display the final game result with win/loss message."""
        self.clear_screen()
        self.display_title()
        self.display_hangman()
        
        if self.game_won:
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"\nYou guessed the word: {self.target_word}")
            print(f"You had {self.max_incorrect - self.incorrect_guesses} incorrect guesses remaining.")
        else:
            print("💀 GAME OVER! Better luck next time! 💀")
            print(f"\nThe word was: {self.target_word}")
    
    def play_again(self):
        """Ask the player if they want to play again."""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def run(self):
        """Main game loop."""
        while True:
            self.reset_game()
            
            # Main game loop
            while not self.game_over:
                self.display_game_status()
                guess = self.get_valid_guess()
                self.process_guess(guess)
                time.sleep(1)  # Brief pause for better UX
            
            # Show final result
            self.display_game_result()
            
            # Ask to play again
            if not self.play_again():
                break
        
        print("\nThanks for playing Professional Hangman!")
        print("This project was created for the CodeAlpha Python Internship Program.")

def main():
    """Entry point of the program."""
    game = HangmanGame()
    game.run()

if __name__ == "__main__":
    main()
