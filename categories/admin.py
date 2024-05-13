from django.contrib import admin

from categories.models import Categories, Movie

# admin.site.register(Categories)
# admin.site.register(Movie)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}