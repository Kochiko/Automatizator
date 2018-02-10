#! python3

import openpyxl, os, glob

# Даем понять в каком каталоге работать - в рабочем
place = os.getcwd()
#os.chdir("/home/kochiko/Рабочий стол/Автоматизатор/")

# Получение названия файла с таблицей
file = glob.glob("*.xlsx")

# Создание переменной в которую помещаем наш файл
wb = openpyxl.load_workbook(file[0])
# Назначаем переменную для работы с нужным листом
sheet = wb["Лист1"]

#######################################################################################
# Считывание названий изделий из ТАБЛИЦЫ и создание списка с наименованиями
#######################################################################################

# Список
list_names = []
list_types = []
# Добавление элементов в список
for row in range(1, sheet.max_row):
    list_names.append(sheet['B' + str(row)].value)
    list_types.append(sheet['D' + str(row)].value)

#######################################################################################
# Считывание названий изделий из ПАПКИ и создание списка с наименованиями
# При этом убираем тип элемента из названия чтобы сравнивать со столбцом в таблице
#######################################################################################    

# Список который будет изменен
folder = glob.glob("*.docx")
# Список который будет использован в качестве аргумента в функции переименования
folder_ = glob.glob("*.docx")

print(len(folder))
# Составление названий без индекса .docx 
for i in range(0, len(folder)):
    folder[i] = folder[i][:folder[i].find(".")]
    # и без типа элемента
    folder[i] = folder[i][folder[i].find(" ") + 1:]

print(folder)
########################################################################################
# Поиск имен из folder в list_names
########################################################################################
new_folder = folder.copy()
for i in range(0, len(folder)):
    for j in range(0, len(list_names)):
        if folder[i] == list_names[j]:
            new_folder[i] = str(j + 1) + ". " + list_types[j] + " " + folder[i] + ".docx"
print(new_folder)

for i in range(0, len(folder)):
    os.rename(folder_[i], new_folder[i])


