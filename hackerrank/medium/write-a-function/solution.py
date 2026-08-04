def is_leap(year):
    leap = False
    
    # 400 se divide hone waale saal hamesha leap year hote hain
    if year % 400 == 0:
        leap = True
    # 100 se divide hone waale (par 400 se nahi) leap year nahi hote
    elif year % 100 == 0:
        leap = False
    # Baaki jo 4 se divide hote hain woh leap year hote hain
    elif year % 4 == 0:
        leap = True
        
    return leap
