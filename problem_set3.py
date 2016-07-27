from string import *

def countSubStringMatch(target,key):
    count = 0
    j=0
    for i in range(0,len(target)):
        j = find(target, key, j)
        if j < 0:
            break
        else:
            count+=1
        j+=1
    return count

        
def countSubStringMatchRecursive (target, key):
    def recurse(j):
        if j==len(target)-len(key):
            return 1 if target[j:]==key else 0
        j = find(target,key,j)
        if j >= 0:
            return 1 + recurse(j+1)
        return 0
    return recurse(0)
    
def subStringMatchExact(target,key):  
    count = ()
    j=0
    for i in range(0,len(target)):
        j = find(target, key, j)
        if j < 0:
            break
        else:
            count = count + (j,)
        j+=1
    return count
