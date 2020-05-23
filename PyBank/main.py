#################################################################
#Name: Aaron Paul Lewis                                         #
#Rice University: Data Analytics and Visualization Boot Camp    #
#Assignment #3: Python Homework - PyBank                        #
#Date: May 21, 2020                                             #
#################################################################

#Import the csv module to manage CSV files.
import csv

#Now import the os module to facilitate file paths accross operating systems.
#This allows for portability between different platforms.
import os

#Link to the relative path of the CSV data file.
budget_path = os.path.join('.','Resources', 'budget_data.csv')

# Open CSV file and read the CSV file in list format.
budget_open = open(budget_path, 'r')
budget_reader = csv.reader(budget_open, delimiter = ',')

col_header = next(budget_reader)

# Create the budget_data list for later calculations.
budget_data = []

#Loop through each row lists in budget_reader and set the types.
for each_row in budget_reader:

    #For each row in budget_reader: Date = each_row[0] , Profit/Losses = each_row[1]
    profit_loss = float(each_row[1])            #Convert Profit/Losses to float type.
    budget_data.append([each_row[0], profit_loss])    #Building budget_data dataset.

#Create the bank_results.txt file in the Analysis folder, and write the result to it.
results_path = os.path.join('Analysis', 'bank_results.txt')
results_file = open(results_path, 'w')

#Total number of months in the dataset.
num_months = len(budget_data)

#Initialize variables.
net_pro_loss = 0.0
tot_chg_pro_loss = 0.0
max_pro_chg = 0.0
min_pro_chg = 0.0

#Perform the calculations.
#Looping over each month in budget_data.
for i in range(num_months - 1):

    currentmth_data = budget_data[i]
    nextmth_data = budget_data[i+1]

    #budget_data header: Date = each_row[0] , profit_loss.
    current_date = currentmth_data[0]
    next_date = nextmth_data[0]

    #Net profit/loss.
    net_pro_loss += currentmth_data[1]
    if i == num_months - 2:
        net_pro_loss += nextmth_data[1]

    #Calculate profit/loss change each month.
    chg_pro_loss = nextmth_data[1] - currentmth_data[1]
    tot_chg_pro_loss += chg_pro_loss
    
    #Find the greatest increase profits.
    # Find the greatest decrease losses.
    start_pro_loss = chg_pro_loss

    if start_pro_loss > max_pro_chg:
        max_pro_chg = start_pro_loss
        date_max_pro = next_date

    elif start_pro_loss < min_pro_chg:
        min_pro_chg = start_pro_loss
        date_min_pro = next_date

#Average change in profit/loss:
avg_chg_pro_loss = tot_chg_pro_loss/(num_months -1)

#Print summary:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${int(net_pro_loss)}")
print(f"Average Change: ${avg_chg_pro_loss:.2f}")
print(f"Greatest Increase in Profits: {date_max_pro} (${int(max_pro_chg)})")
print(f"Greatest Decrease in Profits: {date_min_pro} (${int(min_pro_chg)})")

#Write to bank_results.txt:
results_file.write("Financial Analysis \n")
results_file.write("---------------------------- \n")
results_file.write(f"Total Months: {num_months} \n")
results_file.write(f"Total: ${int(net_pro_loss)} \n")
results_file.write(f"Average Change: ${avg_chg_pro_loss:.2f} \n")
results_file.write(f"Greatest Increase in Profits: {date_max_pro} (${int(max_pro_chg)}) \n")
results_file.write(f"Greatest Decrease in Profits: {date_min_pro} (${int(min_pro_chg)}) \n")
results_file.close
