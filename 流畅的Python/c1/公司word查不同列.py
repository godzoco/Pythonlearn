import xlrd
fileName="a.xlsx"

#获取一个excel内首页表格
def Get_sheet1_from_oneExcel(excelFileName):
    wb=xlrd.open_workbook(excelFileName)
    sheet=wb.sheets()[0]
    return sheet


sheet=Get_sheet1_from_oneExcel(fileName)
list_columnA=sheet.col_values(0)
list_columnE=sheet.col_values(4)

diffrence_list=[]
'''
for i in list_columnA:
    if i =
'''


a=-1

for i in list_columnA:
    if i=="":
        a=a+1
        continue
    if i not in list_columnE:
        diffrence_list.append(i)
        a=a+1
        print(a)

'''
diffrence_list
Out[47]: ['总局']
 
'''

print(diffrence_list)
