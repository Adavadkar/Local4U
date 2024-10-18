L1 = [5,-10,30,40,9.9]
try:
    for i in range(len(L1)):
        item = i ** 2
        print(f"Index : {i}, Item : {item}")
except Exception as e:
    print(e)



# for i,d in enumerate(L1):
#     try:
#         var1 = L1.index(i)
#         var2 = var1 * var1
#         print(i, d)
#         print(var1, var2)
#     except ValueError as er1:
#         print(er1)


