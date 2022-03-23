from ArrayList import ArrayList
from LinkedList import LinkedList
from Node import Node
import time
from random import *

if __name__ == '__main__':
    linked_list = LinkedList()
    array_list = ArrayList()

    randomList = []


    for i in range(10000):
        randomList.append(randint(0,10))

    for i in randomList:
        linked_list.insert(Node(i))
    for i in randomList:
        array_list.insert(i)

    start = time.time()
    linked_list.sortASC()
    ende = time.time()

    print("Die Zeit die, die LinkedListe zum sortieren brauchte war: \n")
    print('{:5.3f}s'.format(ende - start))

    start = time.time()
    array_list.sortAsc()
    ende = time.time()

    print("Die Zeit die, die ArrayListe zum sortieren brauchte war: \n")
    print('{:5.3f}s'.format(ende - start))


