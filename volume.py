def calc_volume(temp):
    if(temp.isnumeric()==False):
        raise ValueError("The length must be a positive integer")
    num = int(temp)
    return num*num*num

#print(calc_volume("4"));
        
            