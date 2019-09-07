import os
import csv

# Set path for CSV file

budget_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and Read CSV File
with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

## Sum the total Months in the DataSet
    Profits_Losses = []
    Months_Year = []
    Revenue_Change = []
    
## Loop to read CSV file
    for row in csv_reader:
        
# fill lists with data
        Profits_Losses.append(int(row[1]))
        Months_Year.append(row[0])
        
# finds total months, but uses next() from above to skip header
list_len = len(Months_Year)  
# finds sum of list of Profits_Losses
sum_profits = sum(Profits_Losses)
# finds first and last #s
first_profit = Profits_Losses[0]
last_profit = Profits_Losses[85]
# calculates average
avg_change = (last_profit - first_profit)/(list_len - 1)

    ## PRINT OUT ANSWERS
#print(Average_Changes)
#print("Financial Analysis")
#print("-----------------------------")
#print(f'Total Months : {list_len}')
#print(f'Total  : ${sum_profits}')
#print(f'Average Change  : ${round(avg_change , 2)}')

## Find changes, but taking the difference of each row on the Profits/Losses col
for i in range(0,len(Profits_Losses)):
        Revenue_Change.append(Profits_Losses[i] - Profits_Losses[i-1])   

        max_rev_change = max(Revenue_Change)

        min_rev_change = min(Revenue_Change)

        max_rev_change_date = str(Months_Year[Revenue_Change.index(max(Revenue_Change))])
        min_rev_change_date = str(Months_Year[Revenue_Change.index(min(Revenue_Change))])

#print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
#print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

a = "Financial Analysis"
b = "-----------------------"
c = f'Total Months : {list_len}'
d = f'Total  : ${sum_profits}'
e = f'Average Change  : ${round(avg_change , 2)}'
f = f'Greatest Increase in Profits : {max_rev_change_date}, ${max_rev_change}'
g = f'Greatest Decrease in Profits : {min_rev_change_date}, ${min_rev_change}'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# Prints results to text
output_results = open('output.txt', 'w')

output_results.write("Financial Analysis\n")
output_results.write("--------------------------\n")
output_results.write(f'Total Months : {list_len}\n')
output_results.write(f'Total  : ${sum_profits}\n')
output_results.write(f'Average Change  : ${round(avg_change , 2)}\n')
output_results.write(f'Greatest Increase in Profits : {max_rev_change_date}, ${max_rev_change}\n')
output_results.write(f'Greatest Decrease in Profits : {min_rev_change_date}, ${min_rev_change}\n')


output_results.close()