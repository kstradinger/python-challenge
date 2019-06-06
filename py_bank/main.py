import os
import csv

csvpath = os.path.join('..','py_bank', 'budget_data.csv')

with open(csvpath, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    print(csvreader)
    #read the header row first, 
    csv_header= next(csvreader)
    print(f'CSV Header: {csv_header}')
    #set net/min/max profit equal to zero before beginging loop
    net_profit = 0
    max_profit = 0
    min_profit = 0
    profit_change = 0

    for row in csvreader:
        #Define lists for Date & Row column
        date = row[0]
        profit= int(row[1])
        #Count the total months in data set
        total_months=csvreader.line_num-1
        #sum together all profit rows for net profit
        net_profit= int(row[1]) + net_profit
        #if then for max profit
        if int(row[1]) > int(max_profit):
            max_profit = row[1]
        #if then for min profit
        if int(row[1]) < int(min_profit):
            min_profit = row[1]
        #Calculate change in profit for avg change
        


#Print out stats
print('Financial Analysis')
print('-------------------------------------------------')
print(f'Total period length: {total_months} Months')        
print(f'Net profits over the given period: ${net_profit}')
print(f'Max Monthly Profit:${max_profit}')
print(f'Min Monthly Profit ${min_profit}')

# output text file
# with open("Financial_analysis.txt", "w+") as text_file:
#     text_file.write('Financial Analysis')
#     text_file.write('-------------------------------------------------')
#     text_file.write(f'Total period length: {total_months} Months')        
#     text_file.write(f'Net profits over the given period: ${net_profit}')
#     text_file.write(f'Max Monthly Profit:${max_profit}')
#     text_file.write(f'Min Monthly Profit ${min_profit}')



        
