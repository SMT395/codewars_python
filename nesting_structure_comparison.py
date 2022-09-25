def same_structure_as(original,other):
    # Filter by data type and list length.    
    if type(original)!=list or type(other)!=list or len(original) != len(other):
        return False
    
    #data to compare
    index_original=[] # index of each nested list at level 1
    len_or=[] # length of those lists 
    sub_idx_or=[] # sub_index for nested lists at level 2
    sub_len_or=[] # length of those lists 
    
    original_list=[index_original, len_or, sub_idx_or, sub_len_or]
    #batch those list together.
    ######
    
    index_other=[] #Same as above
    len_ot=[] 
    sub_idx_ot=[]
    sub_len_ot=[]
    
    other_list=[index_other, len_ot, sub_idx_ot, sub_len_ot]
    ######
    
    # Looping through each list returning the index of a nested list and its length.
    # For original list 
    for idx_1, num_1 in enumerate(original):
        if isinstance(num_1, list)==True:
            index_original.append(idx_1)
            len_or.append(len(num_1))
            for idx, num in enumerate(num_1):
                if isinstance(num, list)==True:
                    sub_idx_or.append(idx)
                    sub_len_or.append(len(num))
    # For other list        
    for idx_2, num_2 in enumerate(other):
        if isinstance(num_2, list)==True: 
            index_other.append(idx_2)
            len_ot.append(len(num_2))
            for idx, num in enumerate(num_2):
                if isinstance(num, list)==True:
                    sub_idx_ot.append(idx)
                    sub_len_ot.append(len(num))
    
    
    #Checking if things match
    if original_list==other_list:
        return True
    else:
        return False
    
    
    #to add all possible index list option, return into index item a list of indexes where 
               
