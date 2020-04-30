import random

# Write your code here
print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']

selected_word = random.choice(words)
hint = selected_word[0:3] + "-" * (len(selected_word) - 3)

print(hint)
guess = input('Guess the word:')
if guess == selected_word:
    print('You survived!')
else:
    print('You are hanged!')
