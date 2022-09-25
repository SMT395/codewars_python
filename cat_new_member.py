def open_or_senior(data):
    output =[]
    for member in data:
        if member[0]>=55 and member[1]>7:
            output.append("Senior")
        else:
            output.append("Open")
         
    return output