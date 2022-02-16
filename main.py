
# allowedSymbols='ABCHEKMTO'
# if c in '1234567890':
#     print('Это цифра')
# else:
#     print('Это буква')

# c='asdadas'
# flagError = 0
# for i in range(len(c)):
#     if not c[i] in 'ABCHEKMTO' and i==0:
#         flagError=1
#     if not c[i] in '0123456789' and i==1:
#         flagError=1
#     if not c[i] in '0123456789' and i==2:
#         flagError=1
# if flagError==1:
#     print('error')
# else:
#     print('ok')

def s(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    a = sorted(set(a))[1:-1]
    if len(a) >= 5:
        a.reverse()
        print(a)
        return a[4]
    else:
        return 0


k = 0
for n in range(460000000, 5600000000):
    if k < 5:
        kk=s(n)
        if kk > 0:
            print(kk)
            k += 1
    else:
        break
a=['1','2','3']
a=[int(b) for b in a]
print(a)
print('crap')








