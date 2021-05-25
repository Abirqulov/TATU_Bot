from .keyboard import *
from .main import *

FAC, TEACHER, DAR_JAR, NEWS = ('🎓 Facultetlar', '💼 O\'qituvchilar', '📋 Dars Jadval', '📡 Yangiliklar')


def buttons_work(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == FAC:
        facultetlar(update)
    elif text == TEACHER:
        teachers(update)
    elif text == DAR_JAR:
        dars_jadvali(update)
    elif text == NEWS:
        news(update)

