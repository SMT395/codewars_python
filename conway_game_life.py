### FUNCTIONAL 
from random import randrange
from random import randint
from random import choice

def get_generation(input_array, generation):
    from itertools import product, permutations
    generation -=1

    index_poss = list(range(len(input_array))) + list(range(len(input_array[0])))
    tup_index_matrix = set(permutations(index_poss, 2))
    state_dict = {(x,y):bool(item) for x,sub_ls in enumerate(input_array) for y,item in enumerate(sub_ls)}
    adj_matrix = {k:None for k in tup_index_matrix}
    new_array= [[0 for col in range(len(input_array[0]))] for col in range(len(input_array))]

    for k in adj_matrix.keys():
        nghbrs = set(product([k[0]-1,k[0],k[0]+1],[k[1]-1,k[1],k[1]+1]))
        nghbrs.remove(k)
        adj_matrix[k] = list(nghbrs.intersection(tup_index_matrix))  

    for position,neighbours in adj_matrix.items():
        adj_matrix[position] = [state_dict[tuple] for tuple in neighbours]

    for position,alive in state_dict.items(): 
        if alive:
            if len([x for x in adj_matrix[position] if x]) in [2,3]:
                new_array[position[0]][position[1]] = 1
            else:
                new_array[position[0]][position[1]] = 0
        else:
            if len([x for x in adj_matrix[position] if x])==3:
                new_array[position[0]][position[1]] = 1
            else:
                new_array[position[0]][position[1]] = 0
        
    if generation>0:
        get_generation(new_array, generation)
    else:
        return new_array
    

### OTHER ATTEMPT (CLEANER)
    
def get_surrounding_points(t):
    result = []
    dimensions = len(t)

    for i in range(dimensions):
        for offset_x in [-1, 0, 1]:
            for offset_y in [-1, 0, 1]:
                new_point = [t[j] + (offset_x if j == i else 0) + (offset_y if j != i else 0) for j in range(dimensions)]
                result.append(tuple(new_point))

    result = list(set(result))
    result.remove(t)
    return result


def remove_padding(output):

    previous_output = output.copy()
    transposed_output = list(map(list, zip(*output)))

    if all(element == 0 for element in output[0]):
        output = output[1:]
    if all(element == 0 for element in output[len(output)-1]):
        output = output[:-1]
    
    if all(element == 0 for element in transposed_output[0]):
        output = [col[1:] for col in output]
    if all(element == 0 for element in transposed_output[len(transposed_output)-1]):
        output = [col[:-1] for col in output]
    
    if previous_output==output:
       return output
    else:
        return remove_padding(output)
    
def cgol(array):

    activated_cells = [(ix,iy) 
                       for ix, line in enumerate(array) 
                       for iy, y in enumerate(line) if y==1]
    neighbour_index_map = {(x,y):get_surrounding_points((x,y)) 
                           for x in range(len(array)) 
                           for y in range(len(array[0]))}
    area_interest = {k:[x for x in v if x in activated_cells] 
                     for k,v in neighbour_index_map.items()}

    next_cells = [k for k,v in area_interest.items() 
              if (len(v)==3 and not k in activated_cells)
              or (len(v) in [2,3] and k in activated_cells)
              ]
    
    # return activated_cells, neighbour_index_map, area_interest, next_cells
    
    size_array = max(list(set([i for sub in next_cells for i in sub])))+1
    output = [[0 for i in range(size_array)].copy() 
              for _ in range(size_array)]
    
    for activated in next_cells:
        output[activated[0]][activated[1]] = 1

    output = remove_padding(output)

    # return output, activated_cells, neighbour_index_map, area_interest, next_cells

    if array==output:
        return output
    return cgol(output)


def generate_random_array(length, width):
    output = [[0 for i in range(width)] 
              for _ in range(length)]
    for list in output:
        for i in range(len(list)):
            list[i] = choice([0,0,0,1])

    return output

array_one = [
    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0]
]

array_two = []


array_three = []