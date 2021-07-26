from django.conf import settings
from django.db import models
from telegram import Bot
from telegram.utils.request import Request
from telethon import TelegramClient


class TitleApplicationModel(models.TextChoices):
    applic1 = ('Заявка на ремонт', 'Заявка на ремонт')
    applic2 = ('Заявка на звонок', 'Заявка на звонок')
    applic3 = ('Заявка на выезд курьера', 'Заявка на выезд курьера')
    applic4 = ('Заявка на подау документов', 'Заявка на подау документов')
    applic5 = ('Заявка на получение документов', 'Заявка на получение документов')
    applic6 = ('Заявка для устрава на работу', 'Заявка для устрава на работу')


class UserModel(models.Model):

    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    title = models.CharField(max_length=100, choices=TitleApplicationModel.choices)
    number = models.CharField(max_length=10, unique=True, verbose_name='Номер телефона',help_text='Пример 9134567891')
    mail = models.EmailField(blank=True, unique=True, verbose_name='Электронная почта')
    tel_name = models.CharField(max_length=4000, verbose_name='Имя пользователя в ТГ', unique=True, default=None,help_text='Без @')
    notifications = models.BooleanField(default=False)
    profile_id = models.IntegerField(verbose_name='ID чата', blank=True, null=True)

    STATUS = (
        ('open', 'Открыта'),
        ('inwork', 'В работе'),
        ('closed', 'Закрыта')
    )
    status = models.CharField(max_length=100, choices=STATUS, default=None)
    membercall = models.ForeignKey('MemberModel', on_delete=models.DO_NOTHING, blank=True,null=True)
    createdate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return ' {0} {1},Tel_Id: {2}, Email: {3}'.format(self.firstname,self.lastname, self.tel_name, self.mail)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    '''Вариант первый'''

    def save(self, *args, **kwargs):
        super(UserModel, self).save(*args, **kwargs)
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(request=request, token=settings.TELEGRAMM_TOKEN)
        if self.notifications:
            try:
                if self.status == 'open':
                    bot.send_message(text='Статус вашей заявки "Открыта" \n'
                                          'Заявка {0} \n'
                                          'Созданная {1}'
                                     .format(self.title, self.createdate),
                                     chat_id=self.profile_id
                                     )
                elif self.status == 'inwork':
                    bot.send_message(
                        text='Статус вашей заявки "В работе" \nЗаявка {0} \nВремя изменения статуса{1}\nВзял в работу {2}'
                            .format(self.title, self.createdate, self.membercall),
                        chat_id=self.profile_id
                    )
                elif self.status == 'close':
                    bot.send_message(text='Статус вашей заявки Закрыта \nЗаявка {0} \nВремя изменения статуса {1}'
                                     .format(self.status, self.title, self.createdate),
                                     chat_id=self.profile_id
                                     )
            finally:
                bot.send_message(text='Для того тобы узнать статус напишите что-нибуь в чат',
                                 chat_id=self.profile_id)

        # '''Вариант 2'''
        # api_id =
        # api_hash =
        # client = TelegramClient('имя пользователя', api_id=?, api_hash=?)
        # client.send_message(self.usercall.tel_name,'Статутс вашей заявки {0} {1}'.format(self.usercall.title, self.status))

class MemberModel(models.Model):
    POSITIONS = (
        ("D", "Director"),
        ('M', 'Manager'),
        ('CCO', 'CCOperator'),
        ('C', 'Cleaner')
    )

    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    workmail = models.EmailField(unique=True)
    position = models.CharField(max_length=100, choices=POSITIONS, default=None)

    def __str__(self):
        return 'Username: {0}, Email: {1}'.format(self.username, self.workmail)

    class Meta:
        verbose_name = 'Сотрудник компании'
        verbose_name_plural = 'Сотрудники компании'


