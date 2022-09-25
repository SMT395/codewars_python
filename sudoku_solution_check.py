def valid_solution(board):
    print(board)
    
    #Check for 0's: if yes -> return false:
    
    for lists in board:
        for item in lists:
            if item==0:
                return False
            
    # Check for lines horizontally and vertically         
    for lists in board:        
        if len(set(lists))!=9:
            return False
    for lists in list(zip(*board)):
        if len(set(lists))!=9:
            return False
    
    board_3=[]
    random=[]
    # Check 3x3 sub-matrices:
    
    for item in list(zip(*board[:3])):
        random.extend(item)
        if len(random)==9:
            board_3.append(random)
            random=[]
    for item in list(zip(*board[3:6])):
        random.extend(item)
        if len(random)==9:
            board_3.append(random)
            random=[]
    for item in list(zip(*board[6:9])):
        random.extend(item)
        if len(random)==9:
            board_3.append(random)
            random=[]

    for lists in board_3:
        if len(set(lists))!=9:
            return False
        
    # If all the conditions above are satified then the solution must be valid   
    return True