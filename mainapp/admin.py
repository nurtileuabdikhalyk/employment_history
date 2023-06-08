from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'staff')
    list_display_links = ('id', 'first_name', 'last_name',)
    list_filter = ('staff',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'fatherland')
    list_display_links = ('id', 'first_name', 'last_name', 'fatherland')
    list_filter = ('education',)
    search_fields = ('title', 'first_name', 'last_name', 'fatherland', 'jsn', 'education', 'profession')


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'place_of_work',)
    list_display_links = ('id', 'customer',)
    search_fields = ('customer', 'place_of_work',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'data_created')
    list_display_links = ('id', 'name', )
    list_filter = ('completed',)
    search_fields = ('name', 'message')


@admin.register(PlaceOfWork)
class PlaceOfWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bin')
    list_display_links = ('id', 'name', 'bin')


# @admin.register(Reward)
# class RewardAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer', 'place_of_work')
#     list_display_links = ('id', 'customer',)
#     search_fields = ('customer', 'place_of_work',)
admin.site.site_title = 'Жүйе әкімшілігі'
admin.site.site_header = 'Django әкімшілігі'
