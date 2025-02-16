from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from .models import App

def verify_apps(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet[App]) -> None:
    queryset.update(is_verified=True)

verify_apps.short_description = "Mark selected apps as verified"  # type: ignore

class AppAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'price', 'is_verified', 'created_at']
    list_filter = ['is_verified']
    actions = [verify_apps]

admin.site.register(App, AppAdmin)
