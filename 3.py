import json
anketa = {"Имя": "Алексей",
    "Группа": "КБ-101",
    "Навыки": ["Python", "Excel"],
    "Уведомления": True}
file = open("participant.json", "w", encoding="utf-8")
json.dump(anketa, file, ensure_ascii=False, indent=4)
file.close()
file = open("participant.json", "r", encoding="utf-8")
anketas = json.load(file)
file.close()
anketas["Навыки"].append("CSV")
anketas["Уведомления"] = False
file = open("participant.json", "w", encoding="utf-8")
json.dump(anketas, file, ensure_ascii=False, indent=4)
file.close()
file = open("participant.json", "r", encoding="utf-8")
itog_anketa = json.load(file)
file.close()
print("Имя:", itog_anketa["Имя"])
print("Группа:", itog_anketa["Группа"])
print("Навыки:", itog_anketa["Навыки"])
print("Уведомления:", itog_anketa["Уведомления"])
