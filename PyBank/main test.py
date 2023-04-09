
import os
import csv

csvpath = os.path.join("C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv")
#"C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv"
#"..",resources","budget_data.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    header_row = next(csvreader)
  
    avgpre =0
  
    months = 0
    total_PL = 0
    avgchanges = []
    sumavgchanges = 0
    current_row = 1 
     
    for row in csvreader:
        
        if csvreader.line_num > 1:
            current_row += 1
            months += 1
            total_PL += int(row[1])
    

    print("Total Months: {}".format(months))         
    print("Total P&L Amount: ${}".format(total_PL))
    
with open ('results_output1', 'w') as file:
    file.write("Total Months: {}\n".format(months))
    file.write("Total P&L Amount: ${}\n".format(total_PL))
            
#! :::::::::::::::::::  CODE ADDED :::::::::::::::::::::::
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)  

    months = 0
    total_PL =0
    avgchanges2 = []
    pre_amount = 0
    current_amount = 0
    calc_amount = 0
    count = 0
    sumAvgChanges = 0
    total2 = 0
    for row in csvreader:
        if count == 0:
            pre_amount = int(row[1])
            #print(pre_amount)
            count += 1
            sumAvgChanges += int(row[1])
        else:
            current_amount = int(row[1])
            calc_amount = current_amount - pre_amount
            avgchanges2.append(calc_amount)
            pre_amount = current_amount
    
    # loop through avgchanges array to calculate total amount in array 
    for item in avgchanges2:
        total2 += item
            
    total2 = total2 / len(avgchanges2)
    max_avg = max(avgchanges2)
    min_avg = min(avgchanges2)

    #! :::::::::::::::::::::::::::::::::::::::::::::::::::::::   

print("Average Change: {}".format((total2)))
print("Greatest Increase in Profits: {}".format(max_avg))
print("Greatest Decrease in Profits: {}".format(min_avg))  
         

with open ('results_output2', 'w') as file:
    file.write("Average Change: ${}\n".format((total2)))
    file.write("Greatest Increase in Profits: ${}\n".format(max_avg))
    file.write("Greatest Decrease in Profits: ${}\n".format(min_avg))
    
    
    
    
    
           