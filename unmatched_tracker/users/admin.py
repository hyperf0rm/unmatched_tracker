from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from games.models import Battle, Participant

User = get_user_model()


class ParticipantInline(admin.TabularInline):
    model = Participant


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    inlines = (ParticipantInline,)
