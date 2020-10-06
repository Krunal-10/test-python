def f_t(**kwargs):
    if kwargs is not None:
        for k,v in kwargs.items():
            #print(k,v)
            if v == 0:
                print('Please enter Non zero height')
                break
            elif k =='feet' and v > 0:
                i = round(v * 12)
                return i
