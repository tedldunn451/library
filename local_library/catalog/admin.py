from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BooksInstanceInline(admin.TabularInline):
    extra = 0
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
