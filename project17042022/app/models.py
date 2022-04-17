from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk}, {self.firstname}, {self.lastname}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.CharField(max_length=255)
    taken_by = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}, {self.title}, {self.pages}, {self.taken_by}"
# Создание файл инструкцию по внесенным измениям
# python manage.py makemigrations
# Реализация изменений согласно созданных инструкций
# python manage.py migrate