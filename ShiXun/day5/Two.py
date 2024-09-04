from openpyxl import load_workbook

staff_wb = load_workbook('./公司人员名单.xlsx')

active_ws = staff_wb.active
fhy_ws = staff_wb["上半年公司名单"]
print(active_ws)
# print(active_ws[5])

# for i in active_ws[5]:
#     print(i.value)
# print(active_ws['B'])

# for row in fhy_ws