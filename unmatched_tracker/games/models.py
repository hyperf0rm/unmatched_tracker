from django.db import models

from games.constants import MAX_NAME_LENGTH, STR_LIMIT, GENERAL_CHAR_LENGTH


class Character(models.Model):
    ATTACK_TYPES = (
        ('MELEE', 'Melee'),
        ('RANGED', 'Ranged')
    )
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    attack_type = models.CharField(max_length=GENERAL_CHAR_LENGTH,
                                   choices=ATTACK_TYPES)
    speed = models.PositiveSmallIntegerField(default=2)

    class Meta:
        ordering = ('name',)
        abstract = True

    def __str__(self) -> str:
        return self.name[:STR_LIMIT]


class Hero(Character):
    about = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True)
    ability = models.TextField(blank=True)


class Sidekick(Character):
    hero = models.ForeignKey(Hero,
                             on_delete=models.CASCADE,
                             related_name='sidekicks')
    count = models.PositiveSmallIntegerField(default=0)


class Battle(models.Model):
    pass
