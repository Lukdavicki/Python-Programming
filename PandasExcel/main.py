import pandas
import xlrd

excel = pandas.read_excel("Financial Sample.xls")
print(excel["Units Sold"])
total_units = 0
for unit in excel["Units Sold"]:
    total_units += unit
print(f"Total units sold: {total_units}")

