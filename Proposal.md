Exercise 5 Project Proposal
---------------------------

Names: Andrei and Niko (TR Section)
---------------------------

Project: Tetris
---------------------------

Summary: For the final project we have the idea of recreating the game tetris with the use of pygame. The final 
demonstration should be a playable tetris game in a window with the use of arrow keys and space bar.
---------------------------


Milestones 1 (March 23):
---------------------------
For the first milestone we are going to work on a simple framework of the window as well as the tetris pieces and 
their first-appearance locations.

- Framework: this is the passive environment of the game where the we will split the screen into three sections as 
shown below. Left section will be where the actual game is going to be played. Top right section is going to be where 
the upcoming block is going to displayed. Bottom right section is going to display the score and the number of lines 
cleared. Score is going to be calculated by adding each successful clear (#ofLinesCleared^2 * SpeedOfLevel).
-------------
[	X	| X ]	<-- Next Block
[		|___]
[		| S ]	<-- Score
[		| L ]	<-- Lines Cleared
-------------

- Basic Pieces are going to be created: square, L, line, T, S and reverse S
- Each block piece is going to have to be made from a single little block then pieced together, so when they line up, 
we can sum up the # of blocks and if that's the max for the line, we clear it.
- Implement the Initial Start of the game where the top piece is displayed as well as the upcoming piece.
- Create the names for the Score and Lines Cleared, and set them to zero.
- Spinning of the block with up and down arrows

Demo: Framework with a spinnable randomly generated shape somewhere in the window left window. The upcoming shape 
should also be generated in the correct location. Score = 0, Lines Cleared = 0.

Milestone 2 (March 30):
---------------------------
Second milestone is going to focus mainly on the dynamic aspect of tetris where the falling of the blocks happens, 
how they interact with each other and the borders of the window. This is probably going to be the hardest part 
because the program is going to have to recognize if the line is full or not. If the line is full, it's going to have 
to be cleared and the blocks above would fall to on top of the others.

- Implement the key commands for moving of the block left or right arrows and instantly dropping with spacebar.
- Also making sure that if the block is next to an edge and a spin happens that it is not spun out of the window.
- Implement a base falling speed which can be adjusted to increase or decrease the difficulty in the game.
- Implement random block generator to make sure that random block are dropped, not same ones.

Demo: The Blocks should fall from middle, be spinnable, and have collision with objects. Might be glitchy. Blocks 
should be stacking when they reach the bottom or another block. No line clears yet.

Milestone 3 (April 6):
---------------------------
Third milestone is going to focus on working out the kinks in line-clear implementation, block collision and proper 
score and lines-cleared display. At this point the game should be playable once loaded. Ontop of that we are going to 
try and create a start menu before the game starts running and after it finishes.

- Testing and fine-tuning the program to run smoothly.
- Integrate an automatic difficulty scaling after a set number of blocks have been dropped.
- Link the score and the number of lines cleared, and make sure that they are working properly.
- Start menu should load on game start, 
- The game should register when you loose and give you a screen where the user acknowledges the loss and returns him 
to start menu
- One reaching new level, user is notified of the increase in difficulty

Demo: Full lines should be cleared. Proper block interraction with environment. Score should be shown properly, as 
well as the lines cleared. Start menu, level up display, and end game menu should be displayed correctly given the 
corresponding event.

Milestone 4 (April 6):
---------------------------
Final milestone is the cleaning phase.

- Clean the code.
- Comment the uncommented code.
- Readme for getting the game up and running on a new machine
- More testing, fine combing the code for presentability and readability.

Demo: Final Product. Properly functioning Tetris game. 6 types of block. Five keyboard inputs for spinning, moving 
and dropping the blocks instantly. Proper score and lines-cleared display. Interaction between objects in game should 
be smooth. Menus should be properly overlaid over the framework and give a few options such as starting a new game, 
and exiting.







