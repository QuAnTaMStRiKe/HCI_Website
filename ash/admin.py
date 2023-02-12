from django.contrib import admin
from .models import Home, About, Category, Profile, Skills, Portfolio


# Register your models here.

#Home
admin.site.register(Home)

#About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]

#Skills
class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine,
    ]

#portfolio
admin.site.register(Portfolio)