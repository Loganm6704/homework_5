# author: Logan Madden
# date: 11/25/2025
# testing different hash functions
# approach 5: multiplying the ASCII values of the letters within the chosen title/quote 
# and create a list if the initial bucket is full

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
# simply multiplying the ASCII values of the letters within the chosen string
def hashFunction(stringData):
     key = 0
     for i in range(0, len(stringData)):
          if key != 0:
               key = ord(stringData[i]) * key
          else:
               key = ord(stringData[i])
     return key
# Appending any colliding items to a list in the bucket
def insertKey(hashTable, movie, key, size, collisions):
     if hashTable[key] == None:
          hashTable[key] = [movie]
     else: 
          hashTable[key].append(movie)
          collisions += 1
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
titleCollisions = 0
quoteCollisions = 0
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
            hashTitleTable, titleCollisions = insertKey(hashTitleTable, movie, titleKey % size, size, titleCollisions)
            hashQuoteTable, quoteCollisions = insertKey(hashQuoteTable, movie, quoteKey % size, size, quoteCollisions)
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
print("multiplying ASCII values and simply creating a list if initial bucket has something in it.")
print(f"{end-start:0.2f} seconds")
