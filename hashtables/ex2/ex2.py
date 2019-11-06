#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    # each ticket is a class
    # source represents the starting airport
    # destination represents the next airport
    # first flight has source of none
    # last flight has a destination of none
    # output should be an array of strings with the destination 

    for i in tickets:
        hash_table_insert(ht, i.source, i.destination)

    loc = hash_table_retrieve(ht ,"NONE")

    for i in range(0, length):
        route[i] = loc
        loc = hash_table_retrieve(ht , loc)        
    
    return route
