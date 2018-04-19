import random as r

a = "test" + str(5)
x = ''
print(a)
if x:
    print("true")
x3 = [1, 2, 3, "a", "5"]
print(x3)
x3.append("next")
print(x3)
x3.insert(2, "two")
print(x3)
del(x3[2])
print(x3)
x4 = []
x4 = x3.copy()
x5 = [10, 3, 4,55]
x5.sort()
print(x5)
print(x5[1:1])

i = 0
x5.reverse()
for i in range (i, len(x5)):
    print(x5[i])

x6 = []
ix = 0
for ix in range (ix, 5):
    x6.append(r.randrange(ix, 10))
print(x6)

if len(x6) > 5:
    print('> 5')
else:
    print('<= 5')

x7 = list(range(1, 10))
print(len(x7))

x8 = [{ "receiptNumber": "2070000902173", "division": "70", "sellingLocation": "207", "businessDate": "20180219", "membershipNumber": "960000223268", "transactionType": "ASSOCIATION"},{ "receiptNumber": "2070000902173", "division": "70", "sellingLocation": "207", "businessDate": "20180219", "transactionType": "DISASSOCIATION"}]

y = 0
for y in range(0, len(x8)):
    x9 = x8[y]
    print(x9)
    print(x9.items())

