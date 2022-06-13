# Hangman - Word Game
In this task, you should create a word game - Hangman. Initial template of the code is provided and it should be
extended as described bellow.
## The Game
Hangman is a famous word game. Given the hidden word, players should try and guess it. The player says the
character and if it is part of the word, all occurrences of it should be revealed, otherwise, a piece of a hanged man is
drawn.

Rules of Hangman:
```
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
```
You can find more about the game in the web.
### Structure of the gameplay
```python
def hangman():
while True:
displayIntro()
result = play()
displayEnd(result)
# TODO
if __name__ == "__main__":
hangman()
```
The game starts from <code>hangman()</code> function. Currently, the game loop <code>while True: </code> is infinite. At the end of the loop,
you should ask the user yes/no question - if he/she wants to play again and if not you should end the loop with <code>break</code>
or <code>return</code> . Everything else must remain unchanged in this function. In while loop game is divided in 3 functions:
<code>displayIntro</code>, <code>play</code> and <code>displayEnd</code> . You should implement these 3 main functions and several helper functions
described below.

### Display Intro
<code>displayIntro</code> is a simple function that should print the welcome screen and game rules in the terminal. You can use
ASCII art and rules from examples and <strong><i>hangman-ascii.txt</i></strong> or you can come up with your own.

### Display End
<code>displayEnd</code> is another simple function that takes one argument <code>result</code> and if it is true function should print winning
text, if not, print that player lost the game and reveal the hidden word.

### Helper Functions
Before we continue to 3rd main function, we need to implement several helper functions.

<code>displayHangman</code> function gets one argument - number of lives left. The Player has 5 lives at the beginning and it
decreases if the player says the wrong letter. <code>displayHangman</code> function should draw the gallow and hanging man. If a
user has all 5 lives only gallows should be drawn. If a player has 4 lives left draw gallows and the head of the man. On
3 lives add neck of the man and so on. When the player has zero lives left draw gallows and full man.<br>

<code>getWord</code> This function should choose the word, which the user has to guess and return it. At first write a function that
always returns the same word, 'moon' for example. This is not worth any points, but might be useful in the beginning.
After that, you can improve function, so that it returns random word from an already predefined list of words: Create
a list of words Ex: <i>['moon','dog','horse','sun','river']</i>, select a random index and return the word which is on
this index in the list. To select a random integer you can use python randint function. Ex: <code>randint(1, 5)</code> randomly
returns integer numbers from 1 to 5. You can find more information about it <a href="https://www.w3schools.com/python/ref_random_randint.asp">here</a>. 
Now <code>getWord</code> is a bit less boring, but we can make it even better. Instead of choosing a word from an already predefined list, choose
words from <strong><i>hangman-words.txt</i></strong>. Each line contains one word, so you can read the file line by line and store it in the
list. After that, you can select words randomly exactly like before.<br>

<code>valid</code> function gets one argument - user's input. It should return true if the input is valid and false otherwise. Input is
valid only if it is a single English lowercase letter.

### Play
The main part of the gameplay is written in <code>play</code> function, but already created helper functions will make it a bit
easier. It should act in the following way:
<ol>
<li>At the beginning of the game, you should choose the a random word from the <strong><i>hangman-words.txt</i></strong> to play with.
<code>getWord</code> helper function should be used for this.
</li>
  <li>After that, the game starts. The player begins with 5 lives. It means that a player can make at most 5 mistakes
until he/she losses the game.
    <ol>
      <li> At each step, you should draw a hanged man, based on the number of lives left. When the player loses, the
drawing should be finished. <code>displayHangman</code> should be used for drawing.
      </li>
      <li>At each step, you should display the current word. Guessed characters should be visible, while others
should be hidden and replaced by <i>('_','#','*')</i> or something else.
      </li>
    </ol>
  </li>
<li>You should ask the player to enter the character.
  <ol>
  <li>Input should be validated. If it is not a single lower case English character, ask again for it. Use proper
helper function.
    </li>
    <li>If a given character appears in the word reveal hidden letters and display during the next turn.
</li>
    <li>If the given character does not appear in the word, the player loses a life and ASCII art should be
updated.
    </li>
  </ol>
</li>
<li>If the player guesses the word or if all lives are lost, the game should end. play function should return
True if the game was won or False otherwise.</li>
</ol>  

### Examples:
#### Welcome screen
```
_______________________________________________
 _
| |
| |__ __ _ _ __ __ _ _ __ ___ __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   __ / |
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
_______________________________________________
```
#### In case of wrong guess a piece of man is drawn
```
    ._______.
    |/      |
    |      (_) 
    |
    |
    |
    |
____|___
Guess the word: ____
Enter the letter:
> c
    ._______.
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
____|___
Guess the word: ____
Enter the letter:
```
#### In case of correct guess appropriate letters are revealed
```
    ._______.
    |/
    |
    |
    |
    |
    |
____|___
Guess the word: m___
Enter the letter:
> o
    ._______.
    |/
    |
    |
    |
    | 
    |
____|___
Guess the word: moo_
Enter the letter:
```
#### Winning screen
```
    ._______.
    |/      |
    |
    |
    |
    |
    |
____|___
Guess the word: moo_
Enter the letter:
> n
Hidden word was: moon
________________________________________________________________________
          _                    _
         (_)                    (_)
__      ___ _ __ _ __ ___ _ __ __ __ _ _ __ _ __ ___ _ __
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|
 \ V V / | | | | | | | |  __/ | \ V V /| | | | | | | | __/ |
  \_/\_/ |_|_| |_|_| |_|\___|_| \_/\_/ |_|_| |_|_| |_|\___|_|
| | (_) | | | (_)
___| |__ _ ___| | _____ _ __ __| |_ _ __ _ __ ___ _ __
/ __| '_ \| |/ __| |/ / _ \ '_ \ / _` | | '_ \| '_ \ / _ \ '__|
| (__| | | | | (__| < __/ | | | | (_| | | | | | | | | __/ |
\___|_| |_|_|\___|_|\_\___|_| |_| \__,_|_|_| |_|_| |_|\___|_|
________________________________________________________________________
Do you want to play again? (yes/no)






