# Modules
import os
import csv

# Path for file
csvpath = os.path.join( "Resources", "budget_data.csv")

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    row = next(csvreader,None)
   
    total_months = 1
    total = 0
    change_list_amount = []
    change_list_month = []
    prev_net = int(row[1])
    first_profit_loss = int(row[1]) 
    profit_loss = 0

    for row in csvreader:
        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        total = total + first_profit_loss + profit_loss
        first_profit_loss = 0
        
        #Calculate the average of the changes in "Profit/Losses" over the entire period
        net_change_amount = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_month = row[0]

        # calculate the greatest increase and decrease in Profit/Losses over the entire period
        change_list_amount.append(net_change_amount)
        change_list_month.append(net_change_month)
        greatest_increase_amount = max(change_list_amount)
        greatest_decrease_amount = min(change_list_amount)

        month_index_inc = change_list_amount.index(greatest_increase_amount)
        month_index_dec = change_list_amount.index(greatest_decrease_amount)
        
        best_month = change_list_month[month_index_inc]
        worst_month = change_list_month[month_index_dec]
    avg = round((sum(change_list_amount))/(len(change_list_amount)),2)    

# Display results    
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {total_months}")   
print(f"Total: ${total}")  
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {best_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease_amount})")



    