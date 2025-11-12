import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from library.models.member import Member
from library.models.author import Author
from library.models.book import Book
"""
## Задача 1: Создание нового члена библиотеки
1. Создать нового члена библиотеки
2. Установить обязательные поля: email='new_member@test.com', role='lib_member'
"""
#new_member = Member(
#    first_name = 'Irina',
#    last_name = 'Ivanova',
#    email='new_member@test.com',
#    role='lib_member',
#    birth_date='1980-12-01',
#    age=45)
#new_member.save()
#print(f"added new member with id: {new_member.id}")

#new_member = Member.objects.create(
#    first_name = 'Olga',
#    last_name = 'Ivanova',
#    email='new_test2@test.com',
#    role='lib_member',
#    birth_date='1980-12-01',
#    age=45)
#
#print(f"added new member with id: {new_member.id}")


"""
## Задача 2: Получение конкретного автора и обновление рейтинга
**ТЗ:**
1. Найти автора с id=1 (Andrzej Sapkowski)
2. Обновить его рейтинг на 9.5
3. Сохранить изменения в базе данных
"""
#author = Author.objects.get(id=1)
#author.rating = 11.5
#author.save()
#print(f"author with id 1: {author}, rating: {author.rating}")

"""## Задача 3: Фильтрация книг по категории и количеству страниц с подсчетом
**ТЗ:**
1. Найти все книги категории с названием, содержащим 'Fiction'
2. Исключить книги с количеством страниц меньше 200
3. Подсчитать количество таких книг"""

#books = Book.objects.filter(
#    category__name_category__contains='Fiction',
#    page_count__gte=200
#)
#cnt = books.count()
#print(f"count of books:{cnt}")
"""## Задача 4: Поиск членов библиотеки с использованием Q-объектов
**ТЗ:**
1. Найти всех членов библиотеки, которые являются либо администраторами, 
либо модераторами
2. Исключить неактивных членов
3. Отсортировать по фамилии и имени
"""
#from django.db.models import Q
#from library.enums  import Role

#x = Member.objects.filter(
#    Q(role=Role.admin.name) | Q(role=Role.moderator.name),
    #active=True,
    #~Q(active=False)
#).exclude(active=False).order_by('last_name', 'first_name')
#print(f"all: {x.count()}")
#for itm in x:
#    print(f"{itm.last_name}, {itm.first_name}, {itm.role}, {itm.active}")

"""## Задача 5: Поиск авторов с использованием field lookups
**ТЗ:**
1. Найти всех авторов, чье имя начинается с 'A'
2. Найти авторов с рейтингом выше 8.5
3. Найти авторов, родившихся после 1950 года
4. Получить первого автора из результата
"""
# from datetime import date
# authors_with_A = Author.objects.filter(first_name__startswith='A')
# authors_rating = Author.objects.filter(rating__gt=8.5)
# #authors_birthday = Author.objects.filter(birthday__gte='1950-01-01')
# authors_birthday = Author.objects.filter(birthday__gte=date(1950, 1, 1))
# print(f"number 1 from list: authors_with_A: {authors_with_A[0]}")
# print(f"number 1 from list: authors_rating: {authors_rating.first()}, {authors_rating.last().rating}")
# print(f"number 1 from list: authors_birthday: {authors_birthday.first()}, {authors_birthday.last().birthday}")

"""## Задача 8: Массовое обновление членов библиотеки
**ТЗ:**
1. Найти всех членов библиотеки с ролью 'moderator'
2. Массово обновить их статус active на False
3. Использовать bulk_update для оптимизации
"""
# from library.models import Member
# from library.enums import Role
# members = Member.objects.filter(role=Role.moderator.name)
# for member in members:
#     member.active = False
#     print(f"{member}-role:{member.role}, status_active: {member.active}")
# Member.objects.bulk_update(members, ['active'])
# print(f"members status update, count: {members.count()}")

"""## Задача 12: Поиск просроченных займов с использованием Q объектов
**ТЗ:**
1. Найти все займы (Borrow), которые не возвращены (is_returned=False)
2. Среди них найти те, где return_date уже прошла (меньше текущей даты)
3. Исключить займы, где return_date равно None
4. Отсортировать по дате займа (старые первыми)
"""
from library.models.borrow  import Borrow
from django.db.models import Q
from django.utils import timezone

today = timezone.now().date()
x = (Borrow.objects.filter(Q(returned=False)
                        & Q(Q(return_date__lt=today)
                        #& ~Q(return_date=None)
                        | Q(return_date__isnull=True))
                        ).order_by('borrow_date'))
#print(x.first().return_date)
for item in x[:5]:
    print(f"returned: {item.returned}, return_date: {item.return_date}, fact returd date: {item.actual_return_date}")

print(x.count())


