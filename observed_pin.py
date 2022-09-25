def get_pins(observed):
    from itertools import product
    adj_dic={0:[0,8],1:[1,2,4],2:[2,1,3,5],3:[3,2,6],4:[4,1,5,7],5:[5,2,4,6,8],6:[6,3,5,9],7:[7,4,8],8:[8,5,7,9,0],9:[9,8,6]}
    list_cand=[adj_dic.get(x) for x in [int(x) for x in str(observed)] if x in adj_dic.keys()]
    return [''.join(str(c) for c in comb) for comb in product(*list_cand)]