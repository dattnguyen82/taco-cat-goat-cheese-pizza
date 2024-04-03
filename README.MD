# Taco Cat Goat Cheese Pizza

## Summary

This python application is variation of the card game: *Taco Cat Goat Cheese Pizza*.  This game is very popular amongst my kids and their friends.  This variation of the game involves typing rather than slapping a deck.   I created this simple app because my kids wanted to create their own variations of the game.  This variation has a bomb card rather than the special cards of the original game.

### Game Objective
The objective of this game is to focus on on typing the words: *Taco*, *Cat*, *Goat*, *Cheese*, *Pizza* in sequential order no matter what card is chosen from the deck. The cards from the deck are chosen at random and meant to confuse the players.  
 
 For example, the deck might show a *Pizza* card for the first card but the player must still type *Taco*
 
 ```
 PIZZA: Taco
```

The next card might be *Goat* but the player must still type *Cat*

 ```
 GOAT: Cat
```

One the player types an incorrect word (or mispells the word), the game will end and show the player their score.  A player gets 1 point for every word they type correctly:

```
!!!!!!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!!
===============GAME STATS================
Player: Benji
Score: 5
=========================================
```

**The BOMB card**

The bomb card is a special card that will appear at random.  If the bomb card appears, the player must type the disarm phrase: *DISARM!* within the bomb detonation time (3 seconds) or the game is over.

 ```
 BOMB: DISARM!
```

### Files
This package includes 4 files

* player.py - This is the Player class that stores information about the player
* function_timer.py - This is a generic function timer decorator used to time the runtime of ta function
* game.py - This is the main game engine class
* main.py - This is the main file which invokes the game engine

#### How to run
This application was developed using Python 3.7.  The simplest way to run the application is to create a 3.7 virtual environment.  Instructions can be found here: https://docs.python.org/3/library/venv.html

To run the application, activate the virtual environment:

```
source <virtual_environment_name>/bin/activate
```

Then run the main.py file

```
python main.py
```
