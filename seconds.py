import time
def many_nymbers(max):
    t1= time.time()
    for x in range(0, max):
        print(x)
        t2= time.time()
        print('i print all for %s seconds'%(t2-t1))
        many_nymbers(1000)
