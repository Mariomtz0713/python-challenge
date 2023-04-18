import os
import csv
budget_data = os.path.join('Resources', 'budget_data.csv')

date = []
net_amount = []
monthly_change = []


def sum_amount(nums):
    total = 0
    for x in nums:
        total += x
    return sum(nums)

def average_change(nums):
    size =  len(nums)
    total = 0
    for x in nums:
        total += x
    return total/size


with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        net_amount.append(int(row[1]))


#Creating monthly change list
for x in range(len(date)-1):
    monthly_change.append(int(net_amount[x+1] - net_amount[x]))

#Splitting Year/Month from date. Pulled from https://stackoverflow.com/questions/11714859/how-to-display-the-first-few-characters-of-a-string-in-python
year = [date[:2] for date in date]
month = [date[-3:] for date in date]

greatest_increase = max(monthly_change)
greatest_increase_index = monthly_change.index(greatest_increase)
greatest_increase_year = year[greatest_increase_index + 1]
greatest_increase_month = month[greatest_increase_index + 1]

greatest_decrease = min(monthly_change)
greatest_decrease_index = monthly_change.index(greatest_decrease)
greatest_decrease_year = year[greatest_decrease_index + 1]
greatest_decrease_month = month[greatest_decrease_index + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum_amount(net_amount)}")
print(f"Average Change: ${round(average_change(monthly_change), 2)}")
print(f"Greatest Increase in profits: {greatest_increase_month}-{greatest_increase_year} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}-{greatest_decrease_year} (${greatest_decrease})")

#Writing Analysis
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txtfile:   
  
   txtfile.write("Financial Analysis\n")
   txtfile.write("----------------------------\n")
   txtfile.write(f"Total Months: {len(date)}\n")
   txtfile.write(f"Total: ${sum_amount(net_amount)}\n")
   txtfile.write(f"Average Change: ${round(average_change(monthly_change), 2)}\n")
   txtfile.write(f"Greatest Increase in profits: {greatest_increase_month}-{greatest_increase_year} (${greatest_increase})\n")
   txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}-{greatest_decrease_year} (${greatest_decrease})\n")


    
