def gen_fullname(first,last):
    if len(first)==0:
        raise ValueError("You are missing a first name")
    if len(last)==0:
        raise ValueError("You are missing a last name")
    for x in first:
        if x.isdigit():
            raise ValueError("All characters in first name must be a letter")
            break
    for x in last:
        if x.isdigit():
            raise ValueError("All characters in last name must be a letter")
            break
    fullname = first + ' ' + last
    return fullname

#print(gen_fullname("Timothy","Nguyen"))