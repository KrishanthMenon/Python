#continue ==> skips the current iteration of the loop & heads back to the top of the loop
'''
p = "python"
for i in p:
    print(i)

    if i == 't':
        continue

'''

p = "python"
i = 1
while i<=5:
    print(p)

    i+=1
    if i == 4:
        continue
    elif i == 5:
        break
