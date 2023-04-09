
import os
import csv


csvpath = 'C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyPoll\\resources\\election_data.csv'
#! csvpath = ".\\resources\\election_data.csv"  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<THIS DOES NOT WORK, TRY IT!
#! csvpath = os.path.join('.', 'resources', 'election_data.csv')  
#! print("File path: " + csvpath)


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    
    
    candidate_vote_count = {}
    votes = 0
    #candidates = set()
    
    for row in csvreader:
        votes += 1
        #candidates.add(row[2])
        
        cvc = row[2]
        if cvc in candidate_vote_count:
            candidate_vote_count[cvc] += 1
        else:
            candidate_vote_count[cvc] = 1
    
    highScore = 0
    winner = ''
    
    for candidate in candidate_vote_count:
        
        print(candidate, candidate_vote_count[candidate], candidate_vote_count[candidate] / votes * 100)  
        
        score = candidate_vote_count[candidate] / votes * 100
        
        if score > highScore:
            highScore = score
            winner = candidate
        
    print(winner)
            
            
            
            
            
            
            
            
        
    print("Total Votes: {}".format(votes))
    #print(candidates)
    print(candidate_vote_count)
    
    


    
    
        
    