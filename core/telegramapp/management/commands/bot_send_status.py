from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import *
from telegram.ext import *
from telegram.utils.request import Request


from coreapp.models import *



def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = 'Произошла ошибка: {0}'.format(e)
            print(error_message)
            raise e

    return inner


'''Основная функция для работы'''


@log_errors
def do_echo(update: Update, contex: CallbackContext):
    chat_id = update.message.chat_id
    update.message.reply_text(text='Нужный вам ID {0}'.format(chat_id))





class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        '''Подклюение'''
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(request=request, token=settings.TELEGRAMM_TOKEN)
        print(bot.get_me())

        '''Обработчики'''
        updater = Updater(bot=bot, use_context=True)

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)
        '''Обработка вход сообщений'''
        updater.start_polling()
        updater.idle()
