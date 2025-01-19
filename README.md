# tetris

Welcome to High Score, automation that supports without taking over. 

We the creators of High Score are taking on the NAV-Canada challenge, designing an automation system that helps a human player achieve the highest possible Tetris score. The automation has limitations that require the human to step in and make key decisions, ensuring the human remains meaningfully involved and accountable for the result.

High Score looks at the current board state, as well as the next piece to be dropped, and determines whether it can make any moves which will be flush with the 'ground.' If it finds more than one, it will pick the spot lowest on the board. After finding this ideal spot, it will automatically move the piece there, saving the player from having to concentrate (and potentially make cruicial mistakes) on the easy move. It will do this as long as it can determine an easy move; whenever it can't, the player has to step back in. To make sure the player gets ample time to think of their move, High Score will also warn the player when they have an upcoming move, as well as display how the board will look once they have to step back in, reducing the mental energy needed to determine a good move down the line.

Within this framework, the player is still definitely engaged in their Tetris game, but doesn't need to try quite as hard as normal to get a high score. This same idea applies to the real world use case of the principles of High Score; saving air traffic controllers from having to work themselves so hard while keeping aviators safe.
