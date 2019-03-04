import json

class VKRow:

    def __init__(self, keyboard, row):
        self.allowed_types = ['primary', 'default', 'negative', 'positive']
        self.keyboard = keyboard
        self.row = row
    
    def add_button(self, label, payload, color="default"):
        '''
        Добавляет кнопку

        :param args: Название кнопки
        :param str payload: Полезная нагрузка кнопки
        :param str color: Цвет кнопки
        '''
        if len(self.keyboard.buttons[self.row])+1>4:
            raise ValueError("Количество кнопок превышает лимит (4 шт.)")

        if not color in self.allowed_types:
            raise ValueError("Невалидный цвет кнопки")

        if not label:
            raise ValueError("Отсутствует название кнопки")

        formatted_payload = None
        if type(payload) is str:
            formatted_payload = json.loads(payload)
        if type(payload) is dict:
            formatted_payload = payload
        else:
            raise ValueError("Payload с некорректным типом")
        
        if len(formatted_payload)<1:
            raise ValueError("Payload пустой")

        formatted_payload = json.dumps(payload)

        self.keyboard.buttons[self.row].append(dict(
            action=dict(
                type="text",
                payload=formatted_payload,
                label=label
            ),
            color=color
        ))
    
    def delete_button(self, index):
        '''
        Удаляет кнопку

        :param int index: Позиция кнопки для удаления
        '''
        if len(self.keyboard.buttons[self.row])<index:
            raise ValueError("Этой кнопки не существует")
        
        del(self.keyboard.buttons[self.row][index])
        return True

class VKKeyboard:

    def __init__(self):
        self.one_time = False
        self.buttons = []

    def set_one_time(self, onetime):
        '''
        Устанавливает одноразовость клавиатуры

        :param bool onetime: True или False
        '''
        self.one_time = onetime

    def check_keyboard(self):
        for row in self.buttons:
            if len(row)<1:
                return False

        return True
    
    def add_row(self):
        '''
        Добавляет ряд с кнопками
        '''
        if len(self.buttons)+1>10:
            raise ValueError("Количество рядов с кнопками превышает лимит (10 шт.)")
        
        self.buttons.append([])
        return True
    
    def delete_row(self, index):
        '''
        Удалить ряд с кнопками

        :param int index: Удалить определенный ряд с кнопками
        '''
        if len(self.buttons)<index:
            raise ValueError("Этого ряда с кнопками не существует")
        
        del(self.buttons[index])
        return True
    
    def edit_row(self, index):
        '''
        Отредактировать ряд с кнопками

        :param int index: Отредактировать определенный ряд с кнопками
        '''
        if len(self.buttons)<index:
            raise ValueError("Этого ряда с кнопками не существует")
        
        return VKRow(self, index)
        
    def get_keyboard(self):
        if not self.check_keyboard():
            raise RuntimeError("Один из рядов не корректен")
        
        return dict(
            one_time=self.one_time,
            buttons=self.buttons
        )
    
    def dump_keyboard(self):
        if not self.check_keyboard():
            raise RuntimeError("Один из рядов не корректен")

        return json.dumps(dict(
            one_time=self.one_time,
            buttons=self.buttons
        ), ensure_ascii=False)