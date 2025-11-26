# author: Logan Madden
# date: 11/25/2025
# testing different hash functions
# approach 3: multiplying the prime numbers associated with the ASCII values of the letters within chosen string 
# and Smply checking the next bucket if initial bucket is full until an open bucket is found

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
# finding the prime number associated with the ASCII value of each character in the string and multiplying them together. the % 128
# was included to account for outlying characters which may be outside the range set below.
def hashFunction(stringData):
     key = 1
     for i in range(0, len(stringData)):
          primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719]
          prime = primeNumbers[ord(stringData[i]) % 128]
          key = key * prime
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
            hashTitleTable, titleCollisions = insertKey(hashTitleTable, movie, titleKey % size, size)
            hashQuoteTable, quoteCollisions = insertKey(hashQuoteTable, movie, quoteKey % size, size)
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
print("attempy 3: Multiplying the prime numbers associated with the ASCII values of the characters in the selcted string and sorting bucket by bucket.")
print(f"{end-start:0.2f} seconds")
