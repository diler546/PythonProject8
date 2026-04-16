listcount = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Испания": "Мадрид",
    "Япония": "Токио",
    "Китай": "Пекин",
    "США": "Вашингтон",
    "Великобритания": "Лондон",
    "Канада": "Оттава"
}

print("Пары ключ-значение:")
for country, capital in listcount.items():
    print(f"{country} - {capital}")

print(f"\nСтолица России: {listcount.get("Россия")}\n")
print(f"Название стран в алфавитном порядке:")

for country in sorted(listcount):
    print(f"{country} - {listcount[country]}")