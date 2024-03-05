from django.contrib import admin

from games.models import Hero, Sidekick


class SidekickInline(admin.TabularInline):
    model = Sidekick
    extra = 1


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (SidekickInline,)


@admin.register(Sidekick)
class SidekickAdmin(admin.ModelAdmin):
    pass
