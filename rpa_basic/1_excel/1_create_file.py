from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴
ws.title = "지수" # sheet의 이름을 변경, not name of the file!! just one sheet
wb.save("jeesoo.xlsx")
wb.close()