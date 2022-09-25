def max_sequence(arr):
    
    best_max =0
    curr_max = 0
    length=len(arr)
     
    for item in range(0,length):
        # length better than in arr for the 
        curr_max = max(arr[item], curr_max + arr[item])
        # pick max between item in array and curr_max + item
        # if the item alone is largest sets the sum there
        best_max = max(best_max,curr_max)
        # updates the max between each
         
    return best_max