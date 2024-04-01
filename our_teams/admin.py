from django.contrib import admin
from .models import My_Team, Team


class MyTeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
    )

    ordering = ('team_name',)

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
        'first_name',
        'last_name',
        'email',
        'position',
        'position_side',
        'health_conditions',
        'comments',
    )

    ordering = ('position',)

# Register your models here.
admin.site.register(My_Team, MyTeamAdmin)
admin.site.register(Team, TeamAdmin)