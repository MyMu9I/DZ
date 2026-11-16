files = "diary.txt"
spisok = ["Сегодня мы работали с файлами Python.","Научились сохранять текст.","Узнали, как читать данные обратно."]
with open(files, "w", encoding="utf-8") as file:
    for a in spisok:
        file.write(a +"\n")
list = "Следующее занятие – CSV и JSON"
with open(files, "a", encoding="utf-8") as file:
    file.write(list + "\n")
with open(files, "r", encoding="utf-8") as file:
    lines = file.readlines()
print("Содержимое дневника:")
for line in lines:
    print(line)
print(f"Количество записей в файле: {len(lines)}")
