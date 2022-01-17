from collections import Counter
def anagram():
    a,b=input().split()
    # dic={}
    # dica={}
    # for i in a:
    #     if i not in dic:
    #         dic[i]=1
    #     elif i in dic:
    #         dic[i]+=1
    # for j in b:
    #     if j not in dica:
    #         dica[j]=1
    #     elif j in dica:
    #         dica[j]+=1
    # if dic==dica:
    #     print("true")
    # else:
    #     print("false")
    #     print(dic,dica)



    #return Counter(a)==Counter(b)

    if len(a)!=len(b):
        return False
    dicA={}
    dicB={}
    for i in range(len(a)):
        dicA[a[i]] = 1 + dicA.get(a[i],0)
        dicB[b[i]] = 1 + dicB.get(b[i],0)
    for c in dicA:
        if dicA[c] == dicB.get(c,0):
            return True
    return False

print(anagram())