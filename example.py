from keyboard import VKKeyboard

keyboard = VKKeyboard()
keyboard.set_one_time(True) # Устанавливает одноразовость клавиатуры, дефолтное значение - False
keyboard.set_inline(True) # Если выставляете это значение = True, one_time сразу становится False

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

# А что если я люблю делать кнопочки просто структурой без вот этих наворотов с доп классами
# Всегда пожалуйста:
keyboard.lazy_buttons({
    'inline': True, # Да, инлайн-кнопки тоже поддерживаются
    'one_time': True,
    'buttons': {
        {'text': 'Кнопка 1', 'payload': {'some_key': 'Полезная нагрузка 1'}, 'color': 'primary'},
        {'text': 'Кнопка 2', 'payload': {'some_key': 'Полезная нагрузка 2'}, 'color': 'default'},
        {'text': 'Кнопка 3', 'payload': {'some_key': 'Полезная нагрузка 3'}, 'color': 'negative'},
        {'text': 'Кнопка 4', 'payload': {'some_key': 'Полезная нагрузка 4'}, 'color': 'positive'},
        {'text': 'Кнопка 5', 'payload': {'some_key': 'Полезная нагрузка 5'}, 'color': 'primary'},
        {'text': 'Кнопка 6', 'payload': {'some_key': 'Полезная нагрузка 6'}, 'color': 'default'},
        {'text': 'Кнопка 7', 'payload': {'some_key': 'Полезная нагрузка 7'}, 'color': 'negative'},
        {'text': 'Кнопка 8', 'payload': {'some_key': 'Полезная нагрузка 8'}, 'color': 'positive'}
    }
}) # и того мы получим клавиатуру с inline-кнопкам, 2 рядами и 8 кнопками, магия! 


print(keyboard.get_keyboard()) # Получить клавиатуру в dict формате, для дальнейшего изменения
print(keyboard.dump_keyboard()) # Получить конечный json с клавиатурой, который можно отправлять к пользователю
