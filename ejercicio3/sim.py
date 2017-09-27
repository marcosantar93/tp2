import linecache
from random import *
from time import sleep



frec = 5

while (True):
    fo = open('test.txt', 'a')
    temp= random()*60-20
    pres=random()*20+990
    hume=random()*100
    wind=random()*150
    mystr = str(temp) + ' ' + str(pres) + ' ' + str(hume) + ' ' + str(wind) + '\n'
    #print (mystr)
    fo.write(mystr)
    fo.close()
    sleep(frec)
