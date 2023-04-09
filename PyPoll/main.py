
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
#'C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyPoll\\resources\\election_data.csv'

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)