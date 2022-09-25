def solution(number):
    numbers=range(1,number)
    multiples=set()
    for i in numbers:
        if i%3==0:
            multiples.add(i)
        if i%5==0:
            multiples.add(i)
    return sum(multiples)