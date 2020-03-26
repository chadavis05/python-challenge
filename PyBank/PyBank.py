import os
import csv

budget_data_path = os.path.join("Resources","budget_data.csv")

months = []
pl = []

with open(budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    
    # Read through each row of data after the header

    for row in csv_reader:
        
    # For readability, it can help to assign your values to variables with descriptive names

        months.append(row[0])
        pl.append(row[1])
        # total_months = total_months + 1
        # print(row[1])
        # total_profit_loss = (total_profit_loss + int(row[1]))
        # Convert row to float and compare to grams of fiber
        # print(row)
        total_months = len(months)

    total_profit_loss = 0
    greatest_increase = pl[0]
    greatest_decrease = pl[0]

    for r in range(len(pl)):
        if pl[r] >= greatest_increase:
            greatest_increase = pl[r]
            greatest_increase_month = months[r]
        elif pl[r] <= greatest_decrease:
            greatest_decrease = pl[r]
            greatest_decrease_month = months[r]
        total_profit_loss += int(pl[r])

    average_change = round(total_profit_loss/total_months, 2)


    print(f"Financial Analysis")
    print(f"----------------------------------------")
    print(f"Total Months: {int(total_months)}")
    print(f"Total: ${int(total_profit_loss)}")
    print(f"Average change: ${int(average_change)}")
    print(f"Greatest Increase in Profits: {str(greatest_increase_month)} ${int(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} ${int(greatest_decrease)}")