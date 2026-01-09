#sanple data from SR website
data = {

'BRO': {

'BSN': { 'W': 10, 'L': 12 },

'CHC': { 'W': 15, 'L': 7 },

'CIN': { 'W': 15, 'L': 7 },

'NYG': { 'W': 14, 'L': 8 },

'PHI': { 'W': 14, 'L': 8 },

'PIT': { 'W': 15, 'L': 7 },

'STL': { 'W': 11, 'L': 11 }

},

'BSN': {

'BRO': { 'W': 12, 'L': 10 },

'CHC': { 'W': 13, 'L': 9 },

'CIN': { 'W': 13, 'L': 9 },

'NYG': { 'W': 13, 'L': 9 },

'PHI': { 'W': 14, 'L': 8 },

'PIT': { 'W': 12, 'L': 10 },

'STL': { 'W': 9, 'L': 13 }

},

'CHC': {

'BRO': { 'W': 7, 'L': 15 },

'BSN': { 'W': 9, 'L': 13 },

'CIN': { 'W': 12, 'L': 10 },

'NYG': { 'W': 7, 'L': 15 },

'PHI': { 'W': 16, 'L': 6 },

'PIT': { 'W': 8, 'L': 14 },

'STL': { 'W': 10, 'L': 12 }

},

'CIN': {

'BRO': { 'W': 7, 'L': 15 },

'BSN': { 'W': 9, 'L': 13 },

'CHC': { 'W': 10, 'L': 12 },

'NYG': { 'W': 13, 'L': 9 },

'PHI': { 'W': 13, 'L': 9 },

'PIT': { 'W': 13, 'L': 9 },

'STL': { 'W': 8, 'L': 14 }

},

'NYG': {

'BRO': { 'W': 8, 'L': 14 },

'BSN': { 'W': 9, 'L': 13 },

'CHC': { 'W': 15, 'L': 7 },

'CIN': { 'W': 9, 'L': 13 },

'PHI': { 'W': 12, 'L': 10 },

'PIT': { 'W': 15, 'L': 7 },

'STL': { 'W': 13, 'L': 9 }

},

'PHI': {

'BRO': { 'W': 8, 'L': 14 },

'BSN': { 'W': 8, 'L': 14 },

'CHC': { 'W': 6, 'L': 16 },

'CIN': { 'W': 9, 'L': 13 },

'NYG': { 'W': 10, 'L': 12 },

'PIT': { 'W': 13, 'L': 9 },

'STL': { 'W': 8, 'L': 14 }

},

'PIT': {

'BRO': { 'W': 7, 'L': 15 },

'BSN': { 'W': 10, 'L': 12 },

'CHC': { 'W': 14, 'L': 8 },

'CIN': { 'W': 9, 'L': 13 },

'NYG': { 'W': 7, 'L': 15 },

'PHI': { 'W': 9, 'L': 13 },

'STL': { 'W': 6, 'L': 16 }

},

'STL': {

'BRO': { 'W': 11, 'L': 11 },

'BSN': { 'W': 13, 'L': 9 },

'CHC': { 'W': 12, 'L': 10 },

'CIN': { 'W': 14, 'L': 8 },

'NYG': { 'W': 9, 'L': 13 },

'PHI': { 'W': 14, 'L': 8 },

'PIT': { 'W': 16, 'L': 6 }

}

}
#print([x for x in data])

#Get the team names in a list to reference them
teams = [x for x in data]


#def testfunc():

#Created a matrix to fill in with the data from the json
statmatrix = [[0,0,0,0,0,0,0,0,0] for x in range(len(teams)+1)]
statmatrix[0][0] = "Teams"
#print((matrix))



#The loop is used to itereate over the teams in the json, and index number is used
#for this loop specifically to iterate through the stat matrix at the same time
for x in range(len(teams) ):

    #these three lines fill out the first row and column
    #as well as the diagonal comparing a team to itself
    statmatrix[0][x+1] = teams[x]
    statmatrix[x+1][0] = teams[x]
    statmatrix[x+1][x+1] = "N/A"

    #for the current team in the loop, this saves the W/L stats to teamrow
    #to access in the next loop
    teamrow = data[teams[x]]


    #this loop fills out the the matrix stats for the current team in the outer loop
    #since the data has stats for all individual teams the W/L for team pairs show up twice for each pair of teams
    #to handle this, the loop below only checks teams after the current team in the outside loop
    #in the bottom loop, previous team pair stats are already filled out in an earlier iteration
    #so to avoid repeating the same pair only teams ahead in the list are compared.
    for y in range(len(teams[x+1:])):
       
        #using the index comparisons for both loop the correct matrix position can be filled
        #and the W/L data is accessed using "teamrow" and the index for the sliced teams from this loop

        statmatrix[x+1][x+2+y] = teamrow[teams[x+1:][y]]['W']
        statmatrix[x+2+y][x+1] = teamrow[teams[x+1:][y]]['L']
    

#added a bottom row to match the visual provided of a row of teams at the bottom of the matrix    
statmatrix.append(statmatrix[0])


for x in statmatrix:
#prints each row individually for better readability    
    print(x)

    #return matrix


#testfunc() tested out provding the solution as a function as well




