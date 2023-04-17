import os
import csv
budget_data = os.path.join('Resources', 'budget_data.csv')

dates = []
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
        dates.append(row[0])
        net_amount.append(int(row[1]))


for x in range(len(dates)-1):
    monthly_change.append(int(net_amount[x+1] - net_amount[x]))
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)


#print(type('net_amount'))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${sum_amount(net_amount)}")
print(f"Average Change: ${average_amount(monthly_change)}")
print(f"Greatest Increase in profits: $({greatest_increase})")
print(f"Greatest Decrease in Profits: $({greatest_decrease})")



