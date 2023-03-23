from prettytable import PrettyTable
from prettytable import from_csv

table = PrettyTable()
table.field_names = ('num', 'name', 'ip')
table.add_row([1, "CTC01", "192.168.13.170"])
table.add_row([1, "CTC02", "192.168.13.171"])
table.add_row([1, "CTC03", "192.168.13.172"])
print(table)

with open("2023-03-01 23-15-37.csv") as file:
    csvTable = from_csv(file)
    print(csvTable)

