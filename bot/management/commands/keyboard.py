from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from bot.models import *
from .callback_query import *


def start_buttons():
    FAC, TEACHER, DAR_JAR, NEWS = ('🎓 Facultetlar', '💼 O\'qituvchilar', '📋 Dars Jadval', '📡 Yangiliklar')
    main_buttons = ReplyKeyboardMarkup([
        [FAC], [TEACHER, DAR_JAR], [NEWS]
    ], resize_keyboard=True)
    return main_buttons


def faculty_buttons():
    other_keyboard = []
    keyboard = []
    fakultetlar = Faculty.objects.all()
    for fakultet in fakultetlar:
        other_keyboard.append(InlineKeyboardButton(fakultet.fac_name, callback_data=fakultet.id))
        if len(other_keyboard) == 2:
            keyboard.append(other_keyboard)
            other_keyboard = []
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def groups_buttons(update):
    other_keyboard = []
    keyboard = []
    query = update.callback_query
    faculty = Faculty.objects.filter(id=query.data).first()
    groups = Groups.objects.filter(faculty=faculty)
    for group in groups:
        other_keyboard.append(InlineKeyboardButton(group.gr_name, callback_data=group.id + 15000))
        if len(other_keyboard) == 2:
            keyboard.append(other_keyboard)
            other_keyboard = []
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def teachers_buttons():
    keyboard = []
    keyboard_list = []
    i = 0
    oqituvchilar = Teachers.objects.all()
    for oqituvchi in oqituvchilar:

        keyboard += [
            InlineKeyboardButton(oqituvchi.f_name + ' ' + oqituvchi.l_name,
                                 callback_data=oqituvchi.id + 1000, ),

        ]

        if i % 2 == 1:
            keyboard_list.append(keyboard)
            keyboard = []
        i += 1
    reply_markup = InlineKeyboardMarkup(keyboard_list)
    return reply_markup


def dars_jadval():
    dars_keyboard = []
    jadval = []
    gruppalar = DarsJadval.objects.all()
    for gruppa in gruppalar:
        dars_keyboard.append(InlineKeyboardButton(gruppa.group_nomi, callback_data=gruppa.id + 10000))
        if len(dars_keyboard) == 3:
            jadval.append(dars_keyboard)
            dars_keyboard = []
    reply_markup = InlineKeyboardMarkup(jadval, resize_keyboard=True)
    return reply_markup


# def filter_groups():
#     fac_id = Faculty.objects.all()
#     group_keyboard = []
#     keyboard = []
#     gruppa = Faculty.objects.filter(id=fac_id).first()
#     guruhlar = Groups.objects.filter(groups=gruppa.id)
#     for guruh in guruhlar:
#         group_keyboard.append(InlineKeyboardButton(guruh.gr_name, callback_data=guruh.id + 20000))
#         if len(group_keyboard) == 2:
#             keyboard.append(group_keyboard)
#             group_keyboard = []
#     reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
#     return reply_markup



