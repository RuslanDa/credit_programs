from django.db import models


# Кредитная организация
class Organization(models.Model):
    cbrf_id = models.IntegerField('ID CBRF', default=0)
    title = models.CharField('Название', max_length=150)
    reg_num = models.IntegerField('Регистрационный номер', default=0)
    reg_date = models.DateField('Дата регистрации', null=True, blank=True)
    address = models.CharField('Адрес', max_length=150)
    ogrn = models.CharField('ОГРН', max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


# Партнёр
class Partner(models.Model):
    title = models.CharField('Название', max_length=150)
    address = models.CharField('Адрес', max_length=150)
    inn = models.CharField('ИНН', max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'


# Предложение
class Offer(models.Model):
    CONSUMER = 1
    MORTGAGE = 2
    CARLOAN = 3
    OFFER_CHOICES = (
        (CONSUMER, 'Потребительский'),
        (MORTGAGE, 'Ипотечный'),
        (CARLOAN, 'Автокредит'),
    )
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)
    date_begin_rotation = models.DateField('дата начала ротации', blank=True)
    date_end_rotation = models.DateField('Дата окончания ротации', blank=True)
    offer_title = models.CharField('Название предложения', max_length=150)
    offer_type = models.IntegerField('Тип предложения', choices=OFFER_CHOICES, default=CONSUMER)
    min_scoring = models.IntegerField('Минимальный скоринговый балл', default=0)
    max_scoring = models.IntegerField('Максимальный скоринговый балл', default=0)
    organization = models.ForeignKey(
        Organization, on_delete = models.CASCADE, verbose_name='Организация',
    )

    def __str__(self):
        return self.offer_title

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


# Анкета
class Checklist(models.Model):
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)
    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.DateField('Дата рождения', blank=True)
    phone = models.CharField('Номер телефона', max_length=10)
    passport = models.CharField('Номер паспорта', max_length=10)
    scoring = models.IntegerField('Скоринговый балл', default=0)
    partner = models.ForeignKey(
        Partner, on_delete=models.CASCADE, verbose_name='Партнер',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}, {self.birthday}'

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


# Заявка
class Order(models.Model):
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    sended = models.DateTimeField('Дата отправки')
    checklist = models.ForeignKey(
        Checklist, on_delete=models.CASCADE, verbose_name='Анкета',
        )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, verbose_name='Предложение',
    )
    S_NEW = 1
    S_SEND = 2
    S_GET = 3
    S_AGREED = 4
    S_REFUSED = 5
    S_GIVEN = 6
    STATUS = (
        (S_NEW, 'Новая'),
        (S_SEND, 'Отправлена'),
        (S_GET, 'Получена'),
        (S_AGREED, 'Одобрено'),
        (S_REFUSED, 'Отказано'),
        (S_GIVEN, 'Выдано'),
        )
    status = models.IntegerField('Статус', choices=STATUS, default=S_NEW)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
