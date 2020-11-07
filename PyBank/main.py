# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank\Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    count = 0
    sum = 0
    csvFileArray = []
    max = [0,0]
    min = [0,0]
    for row in csvreader:
        count = count + 1
        sum = sum + int(row[1])
        csvFileArray.append(int(row[1]))
        if float(row[1]) >= float(max[1]):
            max = row
        if float(row[1]) <= float(min[1]):
            min = row
    print("")
    average = (csvFileArray[len(csvFileArray)-1]-csvFileArray[0])/(count-1)

    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${sum}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {max[0]} (${max[1]})")
    print(f"Greatest Decrease in Profits: {min[0]} (${min[1]})")
    
    output_path = os.path.join("..", "PyBank\Analysis", "bank_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
    outF = open(output_path, "w")
    outF.write("Financial Analysis")
    outF.write("\n")
    outF.write("--------------------")
    outF.write("\n")
    outF.write(f"Total Months: {count}")
    outF.write("\n")
    outF.write(f"Total: ${sum}")
    outF.write("\n")
    outF.write(f"Average Change: ${average}")
    outF.write("\n")
    outF.write(f"Greatest Increase in Profits: {max[0]} (${max[1]})")
    outF.write("\n")
    outF.write(f"Greatest Decrease in Profits: {min[0]} (${min[1]})")
    outF.write("\n")
    outF.close()
