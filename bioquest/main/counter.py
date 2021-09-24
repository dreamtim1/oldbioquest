def counter2(user_answer, right_answer):
    s = 'абвгд'
    bin = ''
    n = 0
    for el in s:
        if (el in user_answer) and (el in right_answer):
            n+=1
            bin += '1'
        elif (el not in user_answer) and (el not in right_answer):
            n+=1
            bin += '1'
        else:
            bin += '0'
            continue
    norm = float(n / 2)
    progr = 0
    if n == 5:
        progr = 2.5
    if n == 4:
        progr = 1.5
    if n == 3:
        progr = float(1)
    return norm, progr, bin


a, b, c = counter2('абвг', 'абв')
print(a, b, c)