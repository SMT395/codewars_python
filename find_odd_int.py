def find_it(seq):
    memory={}
    for number in seq:
        if number not in memory:
            memory[number]=1
        else:
            memory[number]=memory.get(number)+1
    for k,v in memory.items():
        if v%2!=0:
            return k
