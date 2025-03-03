from django.contrib import admin

from typing import Any
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from posApp.models import Category,Products, Sales,inventory, salesItems

admin.site.site_header = "Eve's Glam Admin Panel"
admin.site.site_title = "Eve's Glam POS"
admin.site.index_title = "Welcome to Eve's Glam Management Dashboard"

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(inventory)
# admin.site.register(Employees)