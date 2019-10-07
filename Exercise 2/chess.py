def kingMoves():
    position = str(input('Enter input: '))                                               #Prompts the user for the position of the knight
    coordinates = [['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'], [1, 2, 3, 4, 5, 6, 7, 8]] #Possible board positions
    board = [                                                                            #Chess board visualization in a list
        ['-'] * 8 for i in range(8)
    ]
    try:                                                                                  
        if len(position) == 2:                                                            #Makes sure the lenght of input is just 2 characters
            xcoordinate = coordinates[0].index(str(position[0].upper()))                  #Converts the input to an actual position in the board
            ycoordinate = coordinates[1].index(int(position[1].upper()))
        else:
            raise ValueError
    except ValueError:                                                                    #Checks if the input is in the correct format
        print('Invalid input')                      

    validmoves = [                                                               #List of possible moves for the knight in a list
        [xcoordinate + 0, ycoordinate - 1],
        [xcoordinate - 1, ycoordinate + 0],
        [xcoordinate + 0, ycoordinate + 1],
        [xcoordinate + 1, ycoordinate + 0]
    ]
    try:
        board[xcoordinate][ycoordinate] = 'o'                                                 #Places the knight on the board according to the input
        for i, j in validmoves:
            try:
                if i >= 0 and i <= 8 and j >= 0 and j <= 8:                               #Prevents unintended possible move placement                      
                    board[i][j] = '*'                                                     #Places possible moves on the board according to -          
            except:                                                                       #-placement of the knight on the board                  
                continue
        for i in range(len(board)):
            print(' '.join(board[i]))
    except:
        None
kingMoves()

