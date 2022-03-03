from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Bot
from bot.models import *
from .callback_query import *
from .keyboard import *


def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    update.message.reply_html('Assalomu alaykum <b>{}!</b>\nSiz bilan <b>Sulton Abirqulov</b>\n \n'
    '<b>Ramazon oyi muborak bo\'lsin</b>\n \nKerakli bo\'limni tanlang! 👇👇👇'.
        format(user.first_name), reply_markup=start_buttons())



def facultetlar(update):
    user = update.message.from_user.id
    chat_id = update.message.chat_id

    update.message.reply_text(text='Sizga qaysi facultet haqida ma\'lumot kerak 👇👇👇', reply_markup=faculty_buttons())


def teachers(update):
    update.message.reply_text(text='O\'qituvchilar haqida ma\'lumot 👇👇👇', reply_markup=teachers_buttons())


def dars_jadvali(update):
    update.message.reply_text(text='Qaysi guruh dars jadvalini bilmoqchisiz 👇👇👇', reply_markup=dars_jadval())


# def groups(update):
#     update.message.reply_text(text='Kerakli gruh haqida malumotni olishingiz mukin 👇👇👇', reply_markup=filter_groups())


def news(update):
    yangiliklar = News.objects.all()
    for yangilik in yangiliklar:
        reply_text = '<b>' + yangilik.title + '</b>\n\n'
        reply_text += '<b>' + yangilik.description + '</b>\n'
        photo_path = '{}'.format(yangilik.img)
        update.message.reply_photo(photo=open(photo_path, 'rb'), caption=reply_text, parse_mode='HTML')


def callback_query(update, context):

    query = update.callback_query
    print('query.data', query.data)

    facultetlar_ids = []
    facultetlar = Faculty.objects.filter(id=int(query.data))
    for facultet in facultetlar:
        if int(facultet.id) == int(query.data):
            groups_call(update, context)
        facultetlar_ids.append(facultet.id)
    print('facultetlar_ids = ', facultetlar_ids)

    groups = Groups.objects.filter(id=int(query.data) - 15000)
    group_ids = []
    for group in groups:
        group_ids.append(group.id + 15000)
    print('proup_ids =', group_ids)

    oqituvchilar = Teachers.objects.filter(id=int(query.data) - 1000)
    oqituvchi_ids = []
    for oqituvchi in oqituvchilar:
        oqituvchi_ids.append(oqituvchi.id + 1000)
    print('oqituvchi_ids', oqituvchi_ids)

    yangiliklar = News.objects.filter(id=int(query.data) - 1000)
    yangiliklar_ids = []
    for yangilik in yangiliklar:
        yangiliklar_ids.append(yangilik.id + 1000)
    print('yangiliklar_ids =', yangiliklar_ids)

    jadvallar = DarsJadval.objects.filter(id=int(query.data) - 10000)
    dars_jadval_ids = []
    for jadval in jadvallar:
        dars_jadval_ids.append(jadval.id + 10000)
    print('jadval idisi = ', dars_jadval_ids)
    #
    # gruhlar = Groups.objects.filter(id=int(query.data) - 500)
    # gruhlar_ids = []
    # for gruh in gruhlar:
    #     gruhlar_ids.append((gruh.id + 500))
    # print('gruhlar_ids =', gruhlar_ids)

    if query.data in str(oqituvchi_ids):
        oqituvchi_inline(update, context)

    elif query.data in str(dars_jadval_ids):
        dars_jadval_inline(update, context)

    elif query.data in str(group_ids):
        groups_inline(update, context)


    # facultetlar1 = Faculty.objects.all()
    # fac1_ids = []
    # for facultet1 in facultetlar1:
    #     if int(facultet1.id) == int(query.data):
    #         groups_call(update, context)
    #         fac1_ids.append(facultet1.id)
    # print('facultetlar1_ids =', fac1_ids)