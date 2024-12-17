a = 58461554855184
import time
def iterative (znach):
    start = time.time()
    l1 = 0.0
    l2 = float(znach)
    while ((abs(((l2 + l1)/2.0)**2 - znach)) >= 10**(-6) and (((l2 + l1)/2.0 )**2)!= znach ):

        if (((l2 + l1)/2)**2 > znach):
            l2 = (l2 + l1) / 2
        elif (((l2 + l1)/2)**2 < znach):
            l1 = (l2 + l1) / 2

    print(l2)
    time.sleep(1)
    end = time.time()
    delt = end - start
    print ('Work time', delt )




iterative (a)




start = time.time()
def recursive(low, peak, znach, epsi = 10**(-6)):
    mid = (low + peak)/2
    mid2= mid ** 2

    if (abs(mid2 - znach) <= epsi):
        return mid, print (mid)
    elif mid2 > znach:
        return recursive(low, mid, znach, epsi = 10**(-6))
    elif mid2 < znach:
        return recursive(mid, peak, znach, epsi = 10**(-6))
time.sleep(1)
end = time.time()
delt = end - start


def squarerooot(a):
    return recursive(0, a, a)
otv = squarerooot(a)
print('Work time', delt)






