def dates_compare(a, b):
    left = a.split()
    right = b.split()

    if int(left[2]) > int(right[2]):
        return True
    elif int(left[2]) < int(right[2]):
        return False

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i, j in enumerate(months):
        if left[1] == j:
            left_month = i
        if right[1] == j:
            right_month = i
    if left_month > right_month:
        return True
    elif left_month < right_month:
        return False

    if int(left[0]) > int(right[0]):
        return True
    elif int(left[0]) < int(right[0]):
        return False

    if int(left[3].split(':')[0]) > int(right[3].split(':')[0]):
        return True
    elif int(left[3].split(':')[0]) < int(right[3].split(':')[0]):
        return False

    if int(left[3].split(':')[1]) > int(right[3].split(':')[1]):
        return True
    elif int(left[3].split(':')[1]) < int(right[3].split(':')[1]):
        return False

    return False


N = int(input())
dates = []
for i in range(N):
    dates += [input()]

for i in range(N-1):
    for j in range(N-i-1):
        if dates_compare(dates[j], dates[j+1]):
            dates[j], dates[j+1] = dates[j+1], dates[j]

print(*dates, sep='\n')
