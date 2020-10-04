# Python Challenge - DU Data Bootcamp

The goal of this assignment was to extract 2 datasets from .csv files, analyze the data to get counts, means, mins, and maxes, and print the results to the terminal, as well as output them to a new .txt file.

One of the advantages of Python is how much flexibility it gives you, especially when it comes to structuring and manipulating your data. For this assignment, I wanted to play around with a few different approaches when solving each problem to find one that felt pythonic.

## PyBank

The source .csv file for PyBank contains 2 columns:

- Date
- Profits/Losses

The Python script opens the .csv data and loops over the rows. Each loop appends the data to a list of tuples - which seemed like a tidy data structure to use for a dataset with 2 columns - and increments the total.

I then put the list in ascending order using *sort()*, but with a lambda function passed in as the key. The lambda takes in the tuple and returns the second value - ie *Profits/Losses* - to tell *sort()* what to sort by.

That made finding the greatest increase and decrease was simple, just by appending `[0]` and `[-1]` to the sorted list. Number of months is just the length of the list, and with the total already calculated, it's simple to get the average.

Next was finding a way out of writing so many print statements, as well as having redundancy between that and the text file output. I ended up making a list of strings, using f-strings for data interpolation, and looped over them inside the *with* block of the *open()* method. Each line gets printed to the terminal and written to the results file, using `"%s\n"` to create line breaks.

## PyPoll

The PyPoll data consists of a list of individual votes cast in an election. It has 3 columns:

- Voter ID
- County
- Candidate

In this instance, we can be totally agnostic of the identity or location of individual voters. We are only looking for the percentage of votes cast for each candidate, so that's the only column I analyzed.

Since this is an exercise in tallying, I thought a dictionary would be a good data structure. The code block in the loop contains a conditional, which asks if there isn't a key for that candidate yet in the dictionary. It either initializes their tally at 1, or increments their existing tally by 1. Either way, it also increments the counter for total votes by 1.

To find the winner, I used the *max()* method and passed it the dictionary, and similar to the PyBank, also passed it (but didn't call) its *get()* method as the key, so that it will return the key for the largest value - ie the candidate's name - not the value itself.

In the end, we need to calculate each candidate's percent of the vote and output results the same format, which seemed like a good use case for a function. It takes in the candidate's name and number of votes, calculates their percentage, and returns a properly formatted f-string.

Next I used that function within a list comprehension to output a list of formatted strings for each candidate. Similar to PyBank, I created a list of strings for each line to be output, and looped over them in the *with* block of the file *open*, simultaneously writing to the terminal and the new text file.
