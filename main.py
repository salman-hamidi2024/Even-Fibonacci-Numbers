# fibonacci
nterms =40000
n1,n2 = 1,2
count = 0
list_ = []
for i in range(200):
    if count < nterms:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count += 1
    if n1 >= 4000000:
            break
    if n1 % 2 == 0:
            list_.append(n1)
print(list_)
print(sum(list_))