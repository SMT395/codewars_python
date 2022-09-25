def tribonacci(signature, n):
    output=[]
    for x in range(0,n-3):
        output=signature
        index=len(output)-3
        output.append(sum(output[index:]))    
    if n<4:
        output=signature[:n]
        
    return output
    
