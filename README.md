# SportsReferenceEngineering
A repository for my application to present my solution to Sports Reference

For my approach, I chose to use python to process the data and structured my solution using
loops and a 2D array to contain the data. The code itself has comments and explanations for each step but for an overall explanation, I needed to find what the data contained and how I could manipulate it to create a matrix containing what we want from the data.

First, I made a list of teams to use as key references while accessing the data

I then made a matrix to hold the data based on the number of teams in the json

Then I created nested loops to iterate over the pairs of teams and designed the loops
to account for the fact the json contains repeat data, and made the loops avoid
double checking pairs of teams that were already assigned in the matrix

Once the data is processed and saved to a 2D matrix variable, I made sure to print
the data in a way that is easy to read and check for validity.

I used this approach to try and process the data with an original approach and precise data management going through the content one by one, but I understand that using data management tools and libraries are capable of organizing and managing the data as a whole data structure as well.
