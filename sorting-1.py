from random import randint
import time


# Monkeysort, an extremely inefficient algorithm to sort a list! Randomly arrange the elements (list of integers),
# then check if it is sorted. If it is, then stop. If it isn't, repeat. Then, it compares it to Timsort, a popular algorithm used by languages like Java and Python.
# I wrote this to be able to appreciate efficient algorithms. :)

# Use Fisher-Yates Algorithm (Algorithm is not mine, code is written by me.)
def shuffleList(lst: list):
   length = len(lst)
   for num in range(length - 1, 0, -1):
       rand = randint(0, num)
       lst[num], lst[rand] = lst[rand], lst[num]


def checkIsSorted(lst: list) -> bool:
   for i in range(len(lst) - 1):
       if lst[i] > lst[i + 1]:
           return False
       else:
           continue
   return True


def generateRandom(length, maxnum):
   lst = []
   for i in range(length):
       lst.append(randint(0,maxnum))
   return lst


MINIMUM = 32

def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r


def insert(lst, left, right):
    for i in range(left + 1, right + 1):
        ele = lst[i]
        j = i - 1
        while ele < lst[j] and j >= left:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = ele
    return lst


def merge(lst, l, m, r):
    len1 = m - l + 1
    len2 = r - m
    left = []
    right = []
    for i in range(0, len1):
        left.append(lst[l + i])
    for i in range(0, len2):
        right.append(lst[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < len2 and i < len1:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1

        else:
            lst[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        lst[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        lst[k] = right[j]
        k += 1
        j += 1


def sort(lst):
    n = len(lst)
    min = find_minrun(n)

    for i in range(0, n, min):
        end = min(i + min - 1, n - 1)
        insert(lst, i, end)

    size = min
    while size < n:
        for j in range(0, n, 2 * size):
            mid = min(n - 1, j + size - 1)
            right = min((j + 2 * size - 1), (n - 1))
            merge(lst, j, mid, right)

        size = 2 * size


if __name__ == "__main__":
   mode = input(
       "What mode do you want? Input \"user\" for user input or \"random\" for a random input of set length\n")

   if mode == "random":
       n = int(input("Length of random list: "))
       maxnum = int(input("Biggest number able to be generated: "))

       lst1 = generateRandom(n, maxnum)
       lst2 = lst1.copy()

       start = time.time()
       end = 0
       while True:
           if checkIsSorted(lst1):
               end = time.time()
               print("MonkeySort: Took me " + str(end - start) + " seconds to finish!")
               break
           shuffleList(lst1)
           print("PARSED: " + str(lst1))
       timStart = time.time()
       lst2.sort()
       timEnd = time.time()
       print("TimSort (Python Implementation): Took me " + str(timEnd - timStart) + " seconds to finish!")

   elif mode != "random" and mode!= "user":
       print("Please input a valid mode. Exiting.")
       exit(1)

   else:
       sortList = list(map(int, input("Input a space-separated list of integers \n").split()))
       secondList = sortList.copy()

       start = time.time()
       end = 0
       while True:
           if checkIsSorted(sortList):
               end = time.time()
               print("MonkeySort: Took me " + str(end - start) + " seconds to finish!")
               break
           shuffleList(sortList)

       timStart = time.time()
       sort(secondList)
       timEnd = time.time()
       print("TimSort (My Implementation): Took me " + str(timEnd - timStart) + " seconds to finish!")
