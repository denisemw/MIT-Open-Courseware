def test(n, tup):
    for a in range(0, 200):
        for b in range(0,200):
            for c in range(0,200):
                if tup[0]*a+tup[1]*b+tup[2]*c==n:
                    return True
    return False
            

def consecutive(num, tup):
    count = 0
    for i in range(num,num+6):
        if test(i, tup):
            count+=1
    return count==6

n = 1
largest = n
t = (3, 18, 22)
while True:
    if test(n, t) == False:
        largest = n
    if consecutive(n, t):
        break
    n+=1

