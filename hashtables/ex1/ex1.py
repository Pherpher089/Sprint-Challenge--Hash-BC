#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        w2 = hash_table_retrieve(ht, limit-weights[i])
        if w2 != None:
            # idealy at this point our two index should be
            # i and w2
            if i > w2:
                return (i, w2)
            else:
                return (w2, i)

    return None


# My brute force XD
# def get_indices_of_item_weights(weights, length, limit):
#     ht = HashTable(16)
#     w3 = ()
#     for i in range(length):
#         hash_table_insert(ht, i, weights[i])

#     for i in range(length):
#         w1 = hash_table_retrieve(ht, i)
#         for j in range(length):
#             if j != i:
#                 w2 = hash_table_retrieve(ht, j)
#                 if w2 + w1 == limit:
#                     if w2 > w1:
#                         w3 += (j, i)
#                         return w3
#                     elif w2 == w1:
#                         if i < j:
#                             return (j, i)
#                         else:
#                             return (i, j)
#                     else:
#                         w3 += (i, j)
#                         return w3
#     return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
limit = 7
length = 9

print(get_indices_of_item_weights(weights, length, limit))
