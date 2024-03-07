from django.contrib import admin

from games.models import Hero, Sidekick, Battle, Participant


class SidekickInline(admin.TabularInline):
    model = Sidekick
    extra = 1


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (SidekickInline,)


@admin.register(Sidekick)
class SidekickAdmin(admin.ModelAdmin):
    pass


class ParticipantInline(admin.TabularInline):
    model = Participant


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    inlines = (ParticipantInline,)
