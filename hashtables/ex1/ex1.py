#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # gets two items whose sum of weights equal the weight limit
    # should return tuple answer (zero, one)
    # each element represents the item weights of the two packages
    # the higher value should be in zeroth index and smaller should be placed in first index
    # if a pair doesn't exist return none

    # loop through weights
    for i in range(0, length):
        # store each weight as keys with the value being the index in the list
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length): 
        res = hash_table_retrieve(ht, limit - weights[i])
        answer = ""
        # check if hash table contains entry for limit - weight
        if res is not None:
            # if yes we found the items whos weights sum to the limit
            if res > i:
                answer = (res, i)
            else:
                answer = (i, res)
            return answer
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
