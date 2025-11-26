# homework_5

Attempt 1: The method of sorting was effective in reducing the amount of empty buckets, with 0 remaining for both table, but it definitely could have had less collisions, with the title table having 3583 collisions and the quote table having over 9999 collisions. The time is took to complete the tables was 14.74 seconds.

Attempt 2: The method of sorting remained the same but the method of determining the key was far worse, with over 9999 collisions for both the titles and quotes. It also took 18.70 seconds to finish the tables.

Attempt 3: The method of sorting was once again the same but I decided to adjust the way of making the key by using prime numbers instead, leading to 9982 collisions on the title hash and 4208 on the quote one. This one took 1.01 seconds to do.

Attempt 4: This time, I kept the key method the same but I sorted by simply appending any collisions into a list within the same bucket,  leading to 6510 title collisions and 6375 quote collisions, the the empty slots being the same for each table respectively. This one took 0.4 seconds to do.

Attempt 5: I now kept the sorting method the same as attempt 4 and went back to the key method of attempt 1, leading to 9295 collisions in the title table and 9969 in the quote table, matching the empty slots in the two tables respectively. This took 0.17 seconds to complete.

Overall: Attempt 5 was the fastest of the 5, with attempts 4 and 5 making it clear that list sorting is far faster than iterating through the table to find the next empty bucket. However, this leaves far more empty buckets which may make it slightly more challenging to find specific data. Overall, I do believe attempt 4 was probably the most effective, as it only took slightly longer than attempt 5 and had far less collisions.