# numbers_set = {1, 2, 3, 4, 4} duplicate values removed
# numbers_set = {1, 2, 3, 4, [5, 6]} cannnot use mutable data types
# numbers_set = {1, 2, 3, 4, (5, 6)} tuples are immutable, ok to use
# print(numbers_set)

words_set = {"alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
    print(abcd)
    if "Alpha" in words_set:
        print("Alpha is in set")
else:
    print("Alpha not in set")
words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)
