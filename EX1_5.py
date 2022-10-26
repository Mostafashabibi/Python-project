def EX1_5(age):
    '''
return Age classifier
'''
    if age <= 1:
        return "Intant"
    elif age > 1 and age < 13:
        return "Child"
    elif age >= 13 and age < 20:
        return "Teenager"
    elif age >= 20:
        return "Adult"

