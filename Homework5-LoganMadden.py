# author: Logan Madden
# date: 11/25/2025
# testing different hash functions
# approach 2: adding the ASCII values of the letters within the chosen title/quote followed by multiplying them by the length of the string
# and SImply checking the next bucket if initial bucket is full until an open bucket is found

import time

class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]
        pass
# adding the ASCII values of the letters within the string before multiplying them by the length of the string
def hashFunction(stringData):
     key = 0
     for i in range(0, len(stringData)):
          if key != 0:
               key = ord(stringData[i]) + key
     key = key * len(stringData)
     return key
#Using the basic function of moving ot the next open slot if the initial bucket is full.
def insertKey(hashTable, movie, key, size):
     collisions = 0
     while hashTable[key] != None:
          if key >= size - 1:
               key = 0
          else: 
               key += 1
               collisions += 1
     hashTable[key] = movie
     return hashTable, collisions
# finding the number of slots which still have None within them
def emptySlots(hashTable):
     empty = 0
     for i in range(len(hashTable)):
          if hashTable[i] == None:
               empty += 1
     return empty
import csv

# create empty hash tables
size = 10000 
hashTitleTable = [None] * size
hashQuoteTable = [None] * size
# creating the two hash tables
file = "MOCK_DATA.csv"
counter = 0
start = time.time()
with open(file, 'r', newline='',  encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if counter == 0:
               counter += 1
               continue
            movie = DataItem(row)
            titleKey = hashFunction(movie.movie_name)
            quoteKey = hashFunction(movie.quote)
            #removed % size as the keys aren't as large in this approach and shouldn't pass 10000 (in theory)
            hashTitleTable, titleCollisions = insertKey(hashTitleTable, movie, titleKey , size)
            hashQuoteTable, quoteCollisions = insertKey(hashQuoteTable, movie, quoteKey , size)
            counter += 1
            if counter == 10001: # For some reaosn it would just repeat the last line, this fixed it
                 break
emptyTitle = emptySlots(hashTitleTable)
emptyQuote = emptySlots(hashQuoteTable)
print(f"the title hash table had {emptyTitle} empty slots")
print(f"the quote hash table had {emptyQuote} empty slots")
print(f"the title hash table had {titleCollisions} collisions")
print(f"the quote hash table had {quoteCollisions} collisions")
end = time.time()
print("attempy 2:Adding the ASCII values and multiplying them by the length and checking next bucket until empty one is found")
print(f"{end-start:0.2f} seconds")
