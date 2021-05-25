from django.core.management.base import BaseCommand
from django.conf import settings
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,Bot
from django.views.decorators.csrf import csrf_exempt
from telegram.utils.request import Request
from django.http import HttpResponse
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)
from .main import *
from .messages import *
from .keyboard import *


@csrf_exempt
def webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, buttons_work))
    data = json.loads(request.body.decode("utf-8"))
    update = Update.de_json(data, bot)
    updater.dispatcher.process_update(update)

    return HttpResponse("ok")


def set_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    print(bot.get_me())
    print(bot.get_webhook_info())

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.bot.set_webhook(settings.BASE_URL + "/webhook/" + settings.TOKEN)
    return HttpResponse(settings.BASE_URL + "/webhook/" + settings.TOKEN)


def delete_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    print(bot.get_me())

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.bot.delete_webhook()
    return HttpResponse("ok")


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )

        bot = Bot(
            #request=request,
            token=settings.TOKEN,
            # base_url=settings.PROXY_URL,
        )
        print(bot.get_me())
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, buttons_work))
        updater.start_polling()
        updater.idle()













#
# BTN_TODAY, BTN_TOMORROW, BTN_MONTH, BTN_REGION, BTN_DUO = ('⏱ Bugun', '☎️Ertaga', '📋 ️T\'liq taqvim', '🇺🇿 Mintaqa', '🤲 Duo')
# main_buttons = ReplyKeyboardMarkup([
#     [BTN_TODAY], [BTN_TOMORROW, BTN_MONTH], [BTN_REGION], [BTN_DUO]
#     ], resize_keyboard=True)
#
# STATE_REGION = 1
# STATE_CALENDAR = 2
#
#
# def start(update, context):
#     user = update.message.from_user
#
#     buttons = [
#         [
#             InlineKeyboardButton('Jizzax', callback_data='region_1'),
#             InlineKeyboardButton('Toshkent', callback_data='region_2')
#         ]
#     ]
#
#     update.message.reply_html('Assalomu alaykum <b>{}!</b>\nSiz bilan <b>Sulton Abirqulov</b>\n \n'
#     '<b>Ramazon oyi muborak bo\'lsin</b>\n \nKerakli bo\'limni tanlang!'.
#         format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))
#
#     return STATE_REGION
#
#
# def inline_callback(update, context):
#     try:
#         query = update.callback_query
#         query.message.delete()
#         query.message.reply_html(text='<b>Ramazon taqvimi</b> 2️⃣0️⃣2️⃣1️⃣\n \n Quyidagilrdan birini tanlang 👇👇', reply_markup=main_buttons)
#         return STATE_CALENDAR
#
#     except Exception as e:
#         print('error', str(e))
#
#
# def calendar_today(update, context):
#     update.message.reply_text('Bugunni ko\'rish belgilandi.')
#
#
# def calendar_tomorrow(update, context):
#     update.message.reply_text('Ertanni ko\'rish belgilandi.')
#
#
# def calendar_month(update, context):
#     update.message.reply_text('To\'liq taqvim belgilandi.')
#
#
# def select_region(update, context):
#     update.message.reply_text('Region belgilandi.')
#
#
# def select_duo(update, context):
#     update.message.reply_text('Duoni ko\'rish belgilandi.')
#
#
# def main():
#     # updater o'rnatib olamiz
#     updater = Updater('1754370562:AAHMXBJc7nbVoXjFpAI6YG054Ti-pvZrE10', use_context=True)
#
#     # Dispatcher eventlarini aniwlash uchun.
#     dispatcher = updater.dispatcher
#
#     # start kamandasini ushlab qolish uchun
#     # dispatcher.add_handler(CommandHandler('start', start))
#
#     # inline button query
#     # dispatcher.add_handler(CallbackQueryHandler(inline_callback))
#
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler('start', start)],
#         states={
#             STATE_REGION: [CallbackQueryHandler(inline_callback)],
#             STATE_CALENDAR: [
#                 MessageHandler(Filters.regex('^('+BTN_TODAY+')$'), calendar_today),
#                 MessageHandler(Filters.regex('^('+BTN_TOMORROW+')$'), calendar_tomorrow),
#                 MessageHandler(Filters.regex('^('+BTN_MONTH+')$'), calendar_month),
#                 MessageHandler(Filters.regex('^('+BTN_REGION+')$'), select_region),
#                 MessageHandler(Filters.regex('^('+BTN_DUO+')$'), select_duo)
#             ],
#         },
#         fallbacks=[CommandHandler('start', start)]
#     )
#     dispatcher.add_handler(conv_handler)
#
#     updater.start_polling()
#     updater.idle()
#
# main()