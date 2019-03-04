from keyboard import VKKeyboard

keyboard = VKKeyboard()
keyboard.set_one_time(True) # Устанавливает одноразовость клавиатуры, дефолтное значение - False

keyboard.add_row() # 
keyboard.add_row() # Добавляем ряд кнопок (макс 10 шт.)

keyboard.delete_row(0) # Хочу удалить 1 ряд кнопок (как массив)

editor = keyboard.edit_row(0) # Получаем редактор ряда

editor.add_button(
    "Тестовая кнопка", # Название кнопки
    payload={'button': '2'}, # Полезная нагрузка. Она должна быть, иначе парсер вк, чёт не принимает
    color="positive" # Цвет, может быть 4-х типов primary|default|negative|positive
)
# Кнопок всего может быть 4 шт. в одном ряду

editor.delete_button(0) # Хочу удалить кнопку, которую я только что получил

print(keyboard.get_keyboard()) # Получить клавиатуру в dict формате, для дальнейшего изменения
print(keyboard.dump_keyboard()) # Получить конечный json с клавиатурой, который можно отправлять к пользователю
