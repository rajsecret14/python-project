# n = 4
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    n = 4
    product = 1
    for i in range(n):
      product = product * (i+1)
    return product
print(factorial_iter(4))