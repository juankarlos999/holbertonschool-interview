
def minimumBribes(q):
    copy = sorted(q)
    jumpG = 0
    index1 = 0
    num = 0
    numero = 1
    while num != len(q) - 1:
        jump = 0
        if q[num] > numero:
            index1 = copy.index(q[num])
            jump = index1 - num
            jumpG += jump
            if jump > 2:
                return print("Too chaotic")
            else:
                copy.remove(q[num])
                del q[num]
                continue
        numero += 1
        num += 1
    print(jumpG)


#q = list(map(int, input().rstrip().split()))

q = [1, 2, 5, 3, 7, 8, 6, 4]
q2 = [2, 5, 1, 3, 4]
#minimumBribes(q2)


def rotLeft(a, d):
    # Write your code here
    aux = 0
    for i in range(d):
        aux = a[0]
        a.append(aux)
        del a[0]
    return print(a)


a = [1, 2, 3, 4, 5]
#rotLeft(a, 4)

def commonChild(s1, s2):
    a = list(set(s1.upper()))
    b = list(set(s2.upper()))
    a.sort()
    b.sort()
    print(a)
    print(b)
    match = 0
    for i in a:
        if i in b:
            match += 1
    
    return print(match)


a = "OUDFRMYMAW"
b = "AWHYFCCMQX"

commonChild(a, b)
