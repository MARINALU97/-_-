from django.db import models
from datetime import date
import sqlite3

# Создание таблицы "Products"
class Products(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.FloatField()
    creator_id = models.IntegerField()

    def __str__(self):
        return self.name

# Создание таблицы "User_Product_Access"
class User_Product_Access(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    access_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Создание таблицы "Lessons"
class Lessons(models.Model):
    lesson_id = models.IntegerField()
    product_id = models.IntegerField()
    lesson_name = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    creator_id = models.IntegerField()

    def __str__(self):
        return self.name

# Создание таблицы "Groups"
class Groups(models.Model):
    group_id = models.IntegerField()
    product_id = models.IntegerField()
    group_name = models.CharField(max_length=100)
    min_users = models.IntegerField()
    max_users = models.IntegerField()

    def __str__(self):
        return self.name

# Создание базы данных SQLite
conn = sqlite3.connect('learning_system.db')
cursor = conn.cursor()

import random

class Group:
    def __init__(self, group_id, min_users, max_users):
        self.group_id = group_id
        self.min_users = min_users
        self.max_users = max_users
        self.users = []

def distribute_users_to_groups(users, num_groups):
    # Рассчитываем минимальное и максимальное количество пользователей в группе
    avg_users_per_group = len(users) // num_groups
    remaining_users = len(users) % num_groups

    # Создаем группы с минимальным и максимальным количеством пользователей
    groups = [Group(group_id=i + 1, min_users=avg_users_per_group, max_users=avg_users_per_group) for i in range(num_groups)]

    # Добавляем оставшихся пользователей
    for i in range(remaining_users):
        groups[i].max_users += 1

    # Распределяем пользователей
    for user in users:
        # Сортируем группы по текущему количеству пользователей
        groups.sort(key=lambda g: len(g.users))
        # Добавляем пользователя в группу с наименьшим количеством пользователей
        groups[0].users.append(user)

    return groups

# Пример использования
all_users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9"]
num_groups = 3

result = distribute_users_to_groups(all_users, num_groups)
for group in result:
    print(f"Группа {group.group_id}: {group.users}")