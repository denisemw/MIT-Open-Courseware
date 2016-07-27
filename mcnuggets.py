def test(n):
    for a in range(0, 150,1):
        for b in range(0,150,1):
            for c in range(0,150,1):
                if 6*a+9*b+20*c==n:
                    return True
    return False
            

def consecutive(num):
    count = 0
    for i in range(num,num+6):
        if test(i):
            count+=1
    return count==6

n = 1
largest = n

while True:
    if test(n) == False:
        largest = n
    if consecutive(n):
        break
    n+=1

