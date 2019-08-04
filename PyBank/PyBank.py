import os
import csv

csvpath = os.path.join("..", "BudgetData.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    MonthsTotal = 0
    NetProfitLoss = 0
    ChangeByDate = []
    ChangePLPerMonth = []
    
#Loop to calculate the total number of months in the first column and the net profit and loss of the second column
#With the creation of lists in the first set of variables, the lists will be appended with information from the columns in order to prepare for the next loop to determine the average of the changes in profit and loss

    for row in csvreader:
        MonthsTotal += 1
        NetProfitLoss += int(row[1])
        ChangeByDate.append(row[0])
        ChangePLPerMonth.append(int(row[1]))
        
        
    TotalChangePL = []
    
 #Append individual changes in profit and loss to a list for total changes of profit and loss
 #Calculate average of the changes

    for i in range(MonthsTotal - 1):
        TotalChangePL.append(int(ChangePLPerMonth[i+1]) - int(ChangePLPerMonth[i]))
        AverageChangePL = round(sum(TotalChangePL)/len(TotalChangePL), 2)

#Use list of total changes to determine maximum amounts and dates

MaxIncreaseAmount = max(TotalChangePL)
MaxDecreaseAmount = min(TotalChangePL)
MaxIncreaseDate = ChangeByDate[TotalChangePL.index(max(TotalChangePL))+1]
MaxDecreaseDate = ChangeByDate[TotalChangePL.index(min(TotalChangePL))+1]
 
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {MonthsTotal}")
print(f"Total: {NetProfitLoss}")
print(f"Average Change: {AverageChangePL}")
print(f"Greatest Increase in Profits: {MaxIncreaseDate} with {MaxIncreaseAmount}")
print(f"Greatest Decrease in Profits: {MaxDecreaseDate} with {MaxDecreaseAmount}")

output_file = os.path.join("..", "BudgetDataRevised.csv")

with open(output_file, "w",) as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Months: " + str(MonthsTotal)  + "\n")
    txtfile.write("Total: " + str(NetProfitLoss) + "\n")
    txtfile.write("Average Change: " + str(AverageChangePL) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(MaxIncreaseDate) + " with " + str(MaxIncreaseAmount) + "\n")
    txtfile.write("Greatest Decrease in Profits: " + str(MaxDecreaseDate) + " with " + str(MaxDecreaseAmount) + "\n")      