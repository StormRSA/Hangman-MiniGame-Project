import random


class HangmanGame:
    def __init__(self):
        # Menu attributes:
        self.game_heading = "Welcome to HANGMAN!"
        self.main_menu = 'Type "play" to play the game, "exit" to quit: '

        # Game attributes:
        self.game_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
        self.players_current_guess = list('-' * len(self.game_word))
        self.game_word_letters = set(self.game_word)
        self.possible_characters = 'abcdefghijklmnopqrstuvwxyz'
        self.game_error_state = None

        # Player attributes:
        self.used_letters = set()
        self.player_tries = 0
        self.player_lives = 8

    def game_initialization(self):
        print(self.game_heading)
        player_menu_input = input(self.main_menu).strip()
        while True:
            if player_menu_input == "play":
                HangmanGame.__init__(self)
                self.game_runtime()
            else:
                print("Thank you for playing!")
                break

    def game_runtime(self):
        while True:
            print()
            print("".join(self.players_current_guess))
            self.player_letter_guess(input("Input a letter: ").strip())
            if "".join(self.players_current_guess) == self.game_word or self.player_tries == self.player_lives:
                print(HangmanGame.end_game_state(self))
                break

    # Manages players guess input:
    def player_letter_guess(self, player_input, ):
        # Set game error state to false to game run:
        self.game_error_state = False

        # Checks for game error states:
        HangmanGame.game_error_check(self, player_input)

        # Checks if input is in the hidden word.
        if player_input not in self.game_word_letters and self.game_error_state == False:
            print("Letter selected is not in the word")
            # when player tries is equal to lives the game will end:
            self.player_tries += 1

        # Check other game functions:
        self.used_letters.add(player_input)
        HangmanGame.save_used_letters(self, player_input)
        HangmanGame.player_guess_update(self, player_input)

    def game_error_check(self, player_input):
        if len(player_input) > 1:
            print("Please choose one letter at a time.")
        elif player_input not in self.possible_characters:
            print("Please only use lower case letters.")
        elif player_input in self.used_letters:
            print("You already typed this letter")

        # Activates game error state if one of the above is true:
        if player_input in self.used_letters or player_input not in self.possible_characters or len(player_input) > 1:
            self.game_error_state = True

    # Saves all used letter:
    def save_used_letters(self, player_input):
        # Store positions for each character of the game word in a list:
        self.characters_index = []
        for characters in range(len(self.game_word)):
            if self.game_word[characters] == player_input:
                self.characters_index.append(characters)
        return self.characters_index

    # Updates guess from  the players input:
    def player_guess_update(self, player_input):
        for index in self.characters_index:
            if index in self.characters_index:
                self.players_current_guess[index] = player_input

    # End game sate to let the player know if they won or not:
    def end_game_state(self):
        if "".join(self.players_current_guess) == self.game_word:
            print()
            print("Well done You guessed the word!")
            print("And saved the man!")
            print()
            print(self.game_initialization())
            return
        else:
            print()
            print("You couldn't save the man in time!")
            print()
            print(self.game_initialization())
            return


# Starts HangmanGame:
start_game = HangmanGame()
start_game.game_initialization()
