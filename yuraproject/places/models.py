"""Модели для приложения мест."""

from django.db import models

from users.models import User

PLACE_CATEGORY_CHOICES = [
    ('161', 'Кафе'),
    ('159', 'Бары'),
    ('192', 'Кинотеатры'),
    ('373', 'Круглосуточные магазины'),
    ('193', 'Музеи'),
    ('168', 'Парки'),
    ('164', 'Рестораны'),
    ('611', 'Торговые центры'),
]


class UserRequest(models.Model):
    """Модель пользовательского запроса."""

    category = models.CharField('категория', max_length=3, choices=PLACE_CATEGORY_CHOICES)
    city = models.CharField('город', max_length=50)
    date = models.DateTimeField('дата запроса', auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        related_name='previous_requests',
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'запрос'
        verbose_name_plural = 'запросы'
        indexes = (models.Index(fields=['-date']),)

    def __str__(self):
        return f'{self.city}: {self.category} ({self.date})'

    def save(self, *args, **kwargs):
        """Удалить самый ранний запрос, если количество превысило 5."""
        if UserRequest.objects.count() == 5:
            UserRequest.objects.earliest('date').delete()

        super().save(*args, **kwargs)


class Place(models.Model):
    """Модель места."""

    address = models.CharField('адрес', max_length=150)
    name = models.CharField('название', max_length=150)
    rating = models.DecimalField('рейтинг', max_digits=3, decimal_places=2)
    reviews_amount = models.PositiveSmallIntegerField('количество оценок')
    user_request = models.ForeignKey(
        UserRequest,
        on_delete=models.CASCADE,
        verbose_name='запрос',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'место'
        verbose_name_plural = 'места'
        indexes = (models.Index(fields=['-id']),)

    def __str__(self):
        return self.name
