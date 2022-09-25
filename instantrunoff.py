def runoff(voters):
    from collections import Counter

    count = Counter([ballot[0] for ballot in voters]).most_common()

    
    if len(count)>1 and len({vote[1] for vote in count}) in (0,1):
        return None
    elif count[0][1]>len(voters)*0.5 and len([ballot[0] for ballot in count if ballot[1]==count[0][1]])==1:
        return count[0][0]  
    else:
        least_common = [x[0] for x in count if x[1]==count[-1][1]]
        new_voters = [[vote for vote in ballots if vote in 
                      [x[0] for x in count if x[0] not in least_common]] 
                      for ballots in voters]
        return runoff(new_voters)