import os
import csv

csvpath = os.path.join("..", "BudgetData.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    MonthsTotal = 0
    NetProfitLoss = 0

    #Find total months and total profits
    for row in csvreader:
        MonthsTotal += 1
        NetProfitLoss += int(row[1])

  #  print(MonthsTotal)
  #  print(NetProfitLoss)

    BaseRow = int(row[1])
    TotalChangePL = []

    print(BaseRow)
    print(TotalChangePL)
#change per month, creation of a list of changes
  #  for row in csvreader:
  #     ChangePLPerMonth = int(row[1]) - BaseRow
  #     TotalChangePL.append(ChangePLPerMonth)
  #      BaseRow = int(row[1])

  #  AverageChangePL = sum(TotalChangePL)/ len(TotalChangePL)
    AverageChangePL = NetProfitLoss / MonthsTotal

    print(AverageChangePL)
    
    MaxIncreaseAmount = 0
    MaxIncreaseDate = 0
    MaxDecreaseAmount = 0
    MaxDecreaseDate = 0

    for row in csvreader:
        if int(row[1]) > MaxIncreaseAmount:
            MaxIncreaseAmount = int(row[1])
            MaxIncreaseDate = row[0]

        if int(row[1]) < MaxDecreaseAmount:
            MaxDecreaseAmount = int(row[1])
            MaxDecreaseDate = row[0]

print("Financial Analysis")
print(_________________________)
print("Total Months: " + MonthsTotal)
print("Total: " + NetProfitLoss)
print("Average Change: " + AverageChangePL)
print("Greatest Increase in Profits: " + MaxIncreaseDate + " with " + MaxIncreaseAmount)
print("Greatest Decrease in Profits: " + MaxDecreaseDate + " with " + MaxDecreaseAmount)

output_file = os.path.join("BudgetDataRevised.csv")

with open(output_file, "w",) as txtfile:
    txtfile.write("Financial Analysis" , "\n")
    txtfile.write("_________________________" , "\n")
    txtfile.write("Total Months: " + MonthsTotal , "\n")
    txtfile.write("Total: " + NetProfitLoss , "\n")
    txtfile.write("Average Change: " + AverageChangePL , "\n")
    txtfile.write("Greatest Increase in Profits: " + MaxIncreaseDate + " with " + MaxIncreaseAmount , "\n")
    txtfile.write("Greatest Decrease in Profits: " + MaxDecreaseDate + " with " + MaxDecreaseAmount , "\n")