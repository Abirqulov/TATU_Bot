from .keyboard import *
from bot.models import *
from telegram import ParseMode
import json


def oqituvchi_inline(update, context):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    oqituvchilar = Teachers.objects.filter(id=str(int(query.data)-1000))
    for oqituvchi in oqituvchilar:
        reply_text = '<b>'+oqituvchi.f_name+' '+oqituvchi.l_name+'</b>\n\n'
        reply_text += '<b>'+'📞Telefon raqami : '+oqituvchi.phone+'</b>\n'
        photo_path = '{}'.format(oqituvchi.img)
        query.message.reply_photo(photo=open(photo_path, 'rb'), caption=reply_text, parse_mode='HTML')


def dars_jadval_inline(update, context):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    jadvallar = DarsJadval.objects.filter(id=str(int(query.data)-10000))
    for jadval in jadvallar:
        reply_text = '<b>'+jadval.group_nomi+'-Gruh dars jadvali'+'</b>\n\n'
        photo_path = '{}'.format(jadval.img)
        query.message.reply_photo(photo=open(photo_path, 'rb'), caption=reply_text, parse_mode='HTML')


def groups_call(update, context):
    query = update.callback_query
    # gruppalar = Groups.objects.all()
    query.message.reply_text(text="Qaysi gruh haqida malumotlar kerak 👇👇👇", parse_mode='HTML',reply_markup=groups_buttons(update))


def groups_inline(update, context):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    gruppalar = Groups.objects.filter(id=str(int(query.data) - 15000))
    for gruh in gruppalar:
        reply_text = '<b>'+gruh.gr_name+'-Guruh haqida qisqacha'+'</b>\n\n'
        reply_text += '<b>'+gruh.gr_name+'-Guruh rahbari \n'+str(gruh.teacher)+'</b>\n\n'
        reply_text += '<b>'+'Talabalar soni-'+gruh.tal_soni+'</b>\n\n'
        photo_path = '{}'.format(gruh.img)
        query.message.reply_photo(photo=open(photo_path, 'rb'), caption=reply_text, parse_mode='HTML')




# def news_inline(update, context):
#     query = update.callback_query
#     message_id = query.message.message_id
#     chat_id = query.message.chat.id
#     yangiliklar = News.objects.all()
#     for yangilik in yangiliklar:
#         reply_text = '<b>'+yangilik.title+'</b>\n\n'
#         reply_text += '<b>'+yangilik.description+'</b>\n'
#         photo_path = '{}'.format(yangilik.img)
#         query.message.reply_photo(photo=open(photo_path, 'rb'), caption=reply_text, parse_mode='HTML')
