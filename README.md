TETRIS by Andrei and Niko

Installation + Run Instructions:
- We ran this on mac osx after pygame installation according to the following guide:
		http://neworg/wiki/macintosh
- to run the program run "python3 tetris.py" in terminal from tetris folder

Comments:
- Proposal.md contains initial proposal of for our tetris game.
- our tetris bot idea came from https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/ and we used the outlined "optimal parameters" discussed on the webpage.

Notes/Bugs:
- There's a bug where if a piece is moved to the right, it gets deactivated. Not sure why this happens
- When demo starts the first block does not get placed optimally, (just falls to the middle)
- sometimes the bot glitches out when it stack blocks very high on the right side

Niko's To Do List:
- read through the comments in Menu.py, make sure they are commented properly
- fix up the info display to tell the player what buttons do what

Done Commenting:
- Display.py 
- Area.py
- tetris.py
- Shapes.py
- Bot.py
- Gameover.py