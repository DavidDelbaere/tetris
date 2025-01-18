def findPerfectMoves(board, piece):
    
    #determine height of first filled tile in the leftmost column of a block
    #e.g.
    # []
    # []
    # [] []
    # would return 0  
    # []
    # [] []
    #    []
    # would return 1
    firstLeftTile = 0
    for height in range(len(piece)):
        if(piece[0][height] == 1):
            firstLeftTile = height
            break

    #initialize variables
    valid = True
    validPosList = {}

    #iterate through each column of the board
    for x in range(len(board[0])):
        
        #determine the distance between the top of the board and the end of
        #the filled tiles starting from the bottom of the board
        #(only considers consecutive tiles from bottom)
        y = len(board)
        while(board[y-1][x] == 1):
            y-=1
        
        #determines whether there are floating blocks in that column
        #(above the previously determined 'y')
        for floating in range(y-1):
            if(board[floating][0] == 1):
                valid = False
                break
        
        #iterates through the columns in a block
        for w in range(len(piece[0])):
            
            #determines whether the right side of a block would lie outside
            #the play area in a potential position
            if(x + w > len(board[0])):
                valid = False
                break
            else:

                #iterates through the rows in a block
                for h in range(len(piece)):

                    #determines whether the bottom of a block would lie beneath
                    #the play area in a potential position
                    if((y + firstLeftTile)>len(board)):
                        valid = False
                        break

                    #determines whether a tile on the board(that is filled) would be intersected
                    #by a potential block placement
                    elif((board[y-h-1][x+w] == 1) and (piece[h][w] == 1)):
                        valid = False
                        break

                    #determines whether the selected tile on a block would leave a hole beneath it
                    #(relative to the board) in a potential block placement
                    if(y != len(board)):
                        if(((board[y-h][x+w] == 0) and (piece[w][h] == 1))):
                            
                            #if this is the bottom row of the block
                            if(h == 0):
                                valid = False
                                break

                            #determines whether there is a tile within the block beneath the currently selected block tile
                            elif((piece[h][w] == 1) and (piece[w][h-1] == 0)):
                                valid = False
                                break

        if(valid):
            validPosList.append(x)
    
    #returns a list of all columns in which the leftmost column of the block could 'perfectly' be placed
    return validPosList
