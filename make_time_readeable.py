def make_readable(seconds):
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    res = str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)
    return res