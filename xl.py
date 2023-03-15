import xlwt

#Create a new workbook
book = xlwt.Workbook()

#Add a new sheet
sheet = book.add_sheet('Sheet1')

#Write data to the sheet
sheet.write(0, 0, 'TestName')
sheet.write(0, 1, 'Iteration')
sheet.write(0, 2, 'Thread')
sheet.write(0, 3, 'Status')
sheet.write(0, 4, 'Description')
sheet.write(1, 0, 'riscv-arithmetic')
sheet.write(1, 1, '1')
sheet.write(1, 2, '1')
sheet.write(1, 3, "PASS")

#Save the workbook
book.save('file.xls')


import xlrd

#Open the workbook
book = xlrd.open_workbook('file.xls')

#Access the first sheet
sheet = book.sheet_by_index(0)

#Iterate through the rows and print the values
for i in range(sheet.nrows):
    print(sheet.row_values(i))
