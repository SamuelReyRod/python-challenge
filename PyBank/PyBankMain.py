

# #! Code with greatest month added

# import os
# import csv

# csvpath = os.path.join("C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv")

# with open(csvpath, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
    
#     header_row = next(csvreader)
  
#     avgpre =0
  
#     months = 0
#     total_PL = 0
#     avgchanges = []
#     sumavgchanges = 0
#     current_row = 1 
     
#     for row in csvreader:
        
#         if csvreader.line_num > 1:
#             current_row += 1
#             months += 1
#             total_PL += int(row[1])
    

#     print("Total Months: {}".format(months))         
#     print("Total P&L Amount: ${}".format(total_PL))
    
# with open ('results_output1', 'w') as file:
#     file.write("Total Months: {}\n".format(months))
#     file.write("Total P&L Amount: ${}\n".format(total_PL))
            

# with open(csvpath, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)

#     next(csvreader)  

#     months = 0
#     total_PL =0
#     avgchanges2 = []
#     pre_amount = 0
#     current_amount = 0
#     calc_amount = 0
#     count = 0
#     sumAvgChanges = 0
#     total2 = 0
#     months_data = []
    
#     for row in csvreader:
#         if count == 0:
#             pre_amount = int(row[1])
#             count += 1
#             sumAvgChanges += int(row[1])
#         else:
#             current_amount = int(row[1])
#             calc_amount = current_amount - pre_amount
#             avgchanges2.append(calc_amount)
#             months_data.append(row[0])
#             pre_amount = current_amount
    
#     for i in range(len(avgchanges2)):
#         if avgchanges2[i] == max(avgchanges2):
#             max_month = months_data[i]
#         if avgchanges2[i] == min(avgchanges2):
#             min_month = months_data[i]
    
#     total2 = sum(avgchanges2) / len(avgchanges2)
#     max_avg = max(avgchanges2)
#     min_avg = min(avgchanges2)

# print("Average Change: ${:.2f}".format(total2))
# print("Greatest Increase in Profits: {} (${})".format(max_month, max_avg))
# print("Greatest Decrease in Profits: {} (${})".format(min_month, min_avg))  
         

# with open ('results_output2', 'w') as file:
#     file.write("Average Change: ${:.2f}\n".format(total2))
#     file.write("Greatest Increase in Profits: {} (${})\n".format(max_month, max_avg))
#     file.write("Greatest Decrease in Profits: {} (${})\n".format(min_month, min_avg))





#! yet another update but the wrong month is printing out

import os
import csv

csvpath = os.path.join("C:\\Users\\Pablo\\Desktop\\UCF_GitLab\\Projects\\Python Challenge Module 3\\python-challenge\\PyBank\\resources\\budget_data.csv")

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
    
with open ('results_output', 'w') as file:
    file.write("Total Months: {}\n".format(months))
    file.write("Total P&L Amount: ${}\n".format(total_PL))
    
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
        max_inc_month = ''
        max_dec_month = ''
        for row in csvreader:
            if count == 0:
                pre_amount = int(row[1])
                count += 1
                sumAvgChanges += int(row[1])
            else:
                current_amount = int(row[1])
                calc_amount = current_amount - pre_amount
                avgchanges2.append(calc_amount)
                pre_amount = current_amount

                # Update max and min months
                if calc_amount > total2:
                    max_inc_month = row[0]
                elif calc_amount < total2:
                    max_dec_month = row[0]

            sumAvgChanges += int(row[1])
            months += 1

        # loop through avgchanges array to calculate total amount in array 
        for item in avgchanges2:
            total2 += item

        total2 = total2 / len(avgchanges2)
        max_avg = max(avgchanges2)
        min_avg = min(avgchanges2)

    file.write("\nAverage Change: ${}\n".format((total2)))
    file.write("Greatest Increase in Profits: {} (${})\n".format(max_inc_month, max_avg))
    file.write("Greatest Decrease in Profits: {} (${})\n".format(max_dec_month, min_avg))
    
    print("\nAverage Change: ${}".format((total2)))
    print("Greatest Increase in Profits: {} (${})".format(max_inc_month, max_avg))
    print("Greatest Decrease in Profits: {} (${})".format(max_dec_month, min_avg))
