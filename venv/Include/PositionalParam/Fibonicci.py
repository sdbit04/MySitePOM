
def febonicci(n):
    curr=0
    prev=1
    count=0
    while count < n:
        yield curr
        yield curr
        prev, curr = curr, curr+prev
        count=count+1

gen1=febonicci(9)
print(type(gen1))

for val in gen1:
    print(str(val))
