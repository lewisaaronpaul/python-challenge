#################################################################
#Name: Aaron Paul Lewis                                         #
#Rice University: Data Analytics and Visualization Boot Camp    #
#Assignment #3: Python Homework - ExtraContent:- PyBoss                        #
#Date: May 23, 2020                                             #
#################################################################

#Import the csv module to manage CSV files.
import csv

#Now import the os module to facilitate file paths across operating systems.
#This allows for portability between different platforms.
import os

#Import the datetime module.
from datetime import datetime

#Link to the relative path of the CSV data file.
employee_path = os.path.join('.','Resources', 'employee_data.csv')

# Open CSV file and read the CSV file in list format.
employee_open = open(employee_path, 'r')
employee_reader = csv.reader(employee_open, delimiter = ',')

#Create the employee_results.csv file in the Analysis folder, and write the result to it.
results_path = os.path.join('Analysis', 'employee_results.csv')
results_file = open(results_path, 'w', newline = "")
results_writer = csv.writer(results_file, delimiter = ",")

col_header = next(employee_reader)

#Dictionary to translate US States to Two letter codes:
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Write the NEW header to the results files employee_data.csv.
results_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

#Original header: Emp ID, Name, DOB, SSN, State
for each_row in employee_reader:

    employee_ID = int(each_row[0])                      #Employee's ID

    employee_name = each_row[1].strip().split(" ")      #Split name into First Name and Last Name
    first_name = employee_name[0]                       #Employee's first name
    last_name = employee_name[1]                        #Employee's last name

    #Create a datetime object.
    date_of_birth_obj = datetime.strptime(each_row[2], '%Y-%m-%d')      
    #Convert datetime object to the desired format.
    date_of_birth = date_of_birth_obj.strftime("%m/%d/%Y")              #Employee's DOB

    employee_SSN = each_row[3].strip().split("-")                       #Employee's SSN
    employee_SSN_lastdigits = employee_SSN[2]                           #Last four digits of SSN
    SSN = f"***-**-{employee_SSN_lastdigits}"
    
    employee_state = us_state_abbrev[each_row[4]]                       #Name of state

    #Write the data to the results file: employee_data.csv
    results_writer.writerow([employee_ID, first_name, last_name, date_of_birth, SSN, employee_state])

results_file.close