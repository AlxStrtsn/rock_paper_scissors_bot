from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, #то эта клавиатура должна сворачиваться после нажатия пользователя на кнопку с текстом "Не хочу!"
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_rock],
              [button_scissors],
              [button_paper]],
    resize_keyboard=True
)

# Если пользователь нажмет на кнопку "Давай!" -
# клавиатура yes_no_kb будет заменена на игровую клавиатуру.

# Игровой клавиатуре game_kb параметр one_time_keyboard не нужен,
# потому что каждый раз, когда пользователь будет делать свой игровой выбор,
# бот будет сообщать о том, кто победил и присылать клавиатуру yes_no_kb,
# чтобы узнать у пользователя хочет ли он сыграть еще раз.

# Тексты, которые будут отображаться на кнопках клавиатуры,
# берем по соответствующим ключам из словаря LEXICON_RU,
# который предварительно импортируем из модуля lexicon_ru в пакете lexicon.

# Вообще, если в телеграм-боте используется много разных клавиатур - они не хардкодятся как в этом примере.
# Они создаются на лету специальными функциями, принимающими в качестве параметров количество кнопок,
# количество рядов, количество кнопок в ряде, тексты, отображаемые на кнопках и т.п.
# Но здесь клавиатур всего две, поэтому наш подход может считаться оправданным.