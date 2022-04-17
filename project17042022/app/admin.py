from django.contrib import admin
from app.models import Student, Book


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ['full_name']
    search_fields = ('firstname', 'lastname')

    def full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'pages', 'taken_by')
