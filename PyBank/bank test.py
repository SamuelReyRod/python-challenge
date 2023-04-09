
import os
import csv

csvpath = os.path.join("C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv")
#"C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv"
#"..",resources","budget_data.csv"


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    header_row = next(csvreader)
    print(header_row)
    months = 0
    total_PL = 0
    avgchanges = []
    sumavgchanges = 0
    pre_row = next(csvreader)   #this line is throwing off the TTL months and TTLpL
    print(pre_row)
    
    for row in csvreader:
        months += 1
        total_PL += int(row[1])
        avgchange = float(row[1]) - float(pre_row[1])
        
       
        avgchanges.append(avgchange)
        sumavgchanges = sum(avgchanges)   
        pre_row = row
        max_avg = max(avgchanges)
        min_avg = min(avgchanges)
        
print(avgchanges)
            
print("Total Months: {}".format(months))
print("Total P&L Amount: ${}".format(total_PL))
print("Average Change: {}".format((sumavgchanges/months)))
print("Greatest Increase in Profits: {}".format(max_avg))
print("Greatest Decrease in Profits: {}".format(min_avg))



#results_output = os.path.join("C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\results_file.csv")
# Export text file is created in the same folder as the program
with open ('results_output1', 'w') as file:
    file.write("Total Months: {}\n".format(months))
    file.write("Total P&L Amount: ${}\n".format(total_PL))
    file.write("Total P&L Amount: ${}\n".format(sumavgchanges/months))
    file.write("Total P&L Amount: ${}\n".format(max_avg))
    file.write("Total P&L Amount: ${}\n".format(min_avg))
    


