tot = 0.0
numbers = 0.0
minimum = None
maximum = None

while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except ValueError:
        print('INVALID INPUT')
        continue
    if minimum is None or fval < minimum:
        minimum = fval
    if maximum is None or fval > maximum:
        maximum = fval

    numbers += 1
    tot += fval

# print('ALL DONE')
if numbers > 0:
    print(tot, numbers, tot/numbers)
    print(minimum)
    print(maximum)