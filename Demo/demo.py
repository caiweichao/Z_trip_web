# import openpyxl
#
#
# class TIMU:
#     # 初始化题目
#     def __init__(self):
#         self.daan = None
#         self.timu = None
#         self.xxA = None
#         self.xxB = None
#         self.xxC = None
#         self.xxD = None
# class newtimu:
#     def __init__(self):
#         self.timi =None
#         self.daan = None
#         self.wanzen = None
#
#
# class DoExcel:
#     # 打开文件
#     def __init__(self, filename):
#         self.filename = filename
#         self.workbook = openpyxl.load_workbook(filename=filename)
#
#     def get_timu(self, sheet_name):
#         sheet = self.workbook[sheet_name]
#         max_row = sheet.max_row
#         timus = []
#         for r in range(2, max_row + 1):
#             timu = TIMU()
#             new_timu =newtimu()
#             timu.timu = sheet.cell(row=r, column=2).value
#             timu.daan = sheet.cell(row=r, column=1).value
#             timu.xxA = sheet.cell(row=r, column=3).value
#             timu.xxB = sheet.cell(row=r, column=4).value
#             timu.xxC = sheet.cell(row=r, column=5).value
#             timu.xxD = sheet.cell(row=r, column=6).value
#             newtimu.timi = '答案'+str(timu.daan)+"  "+str(timu.timu)
#             newtimu.daan = 'A: '+str(timu.xxA)+"  B: "+str(timu.xxB)+"  C: "+str(timu.xxC)+"  D: "+str(timu.xxD)
#             newtimu.wanzen = newtimu.timi+"\n"+newtimu.daan+"\n"
#             print(newtimu.wanzen)
#             timus.append(newtimu)
#         return timus
# if __name__ == '__main__':
#         do = DoExcel(filename="D:\Python_project\Z_trip_web\Demo\\123.xlsx")
#         timu = do.get_timu('Sheet1')
#

from Commons.MysqlConnect import Mysql_Util