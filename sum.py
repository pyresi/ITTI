
# sum = 0
# for number in a:
#     sum += number
# print(sum)

def sum(a):
    if len(a) == 0:
      return 0
    return a[0] + sum(a[1:])

a = ([1, 3, 4, 5, 7])
print(sum(a))

