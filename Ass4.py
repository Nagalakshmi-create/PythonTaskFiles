#create four list containig string and combine every element from each list in a single tuple

list_1 = ["a", "e", "i"]
list_2 = ["b", "f", "j"]
list_3 = ["c", "g", "k"]
list_4 = ["d", "h", "l"]

print(list(zip(list_1, list_2, list_3, list_4)))