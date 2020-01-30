import gspread
from oauth2client.service_account import ServiceAccountCredentials
# 1-2 задания------------------------------------------------------------------------------
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(creds)
wks = gc.open("conduit 9")
list_of_wks = wks.worksheet('9')
# 3 задание--------------------------------------------------------------------------------
def create_table_without_duplicate(sheet_name: str, row_number: int, col_number: int):
  try:
    wks.del_worksheet(wks.worksheet(sheet_name))
  except:
    pass
  wks.add_worksheet(sheet_name, row_number, col_number)
create_table_without_duplicate('bolluev', 30, 30)
# 4 задание--------------------------------------------------------------------------------
def copy_student_marks(surname: str, row_number: int):
    b = wks.worksheet('bolluev')
    v1 = list_of_wks.row_values(1)
    v2 = list_of_wks.row_values(2)
    
    cell_list1 = b.range('A1:C1')
    for cell1 in range(len(v1)):
        cell_list1[cell1].value = v1[cell1]
    b.update_cells(cell_list1)
    
    cell_list2 = b.range('A2:Z2')
    for cell2 in range(len(v2)):
        cell_list2[cell2].value = v2[cell2]
    b.update_cells(cell_list2)
    if list_of_wks.row_count<row_number:
        print('в таблице нет столько строк')
    else:
        cell = list_of_wks.find(surname)
        v3 = list_of_wks.row_values(cell.row)
    strp = 'A' + str(row_number) + ':Z' + str(row_number)
    cell_list3 = b.range(strp)
    for cell3 in range(len(v3)):
        cell_list3[cell3].value = v3[cell3]
    b.update_cells(cell_list3)

copy_student_marks('Боллуев Мусса', 6)
# 5 задание-----------------------------------------------------------------------------------
def titles_of_lists(table_name: str):
    wks = gc.open(table_name)
    wks_list = wks.worksheets()
    title = []
    for i in wks_list:
        title.append(i.title)
    return title
t_list = titles_of_lists('conduit 9')
print(t_list)