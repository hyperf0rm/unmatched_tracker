from django.db import models
from django.contrib.auth import get_user_model

from games.constants import MAX_NAME_LENGTH, STR_LIMIT, GENERAL_CHAR_LENGTH

User = get_user_model()


class Character(models.Model):
    MELEE, RANGED = 'MELEE', 'RANGED'
    ATTACK_TYPES = (
        (MELEE, 'Melee'),
        (RANGED, 'Ranged')
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


class Participant(models.Model):
    hero = models.ForeignKey(Hero,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    is_winner = models.BooleanField(default=False)
    battle = models.ForeignKey('Battle', on_delete=models.CASCADE,
                               related_name='participants')

    def __str__(self):
        return f'{self.user.username} играл за {self.hero.name}: {self.winner_str}'

    @property
    def winner_str(self):
        if self.is_winner:
            return 'победа'
        return 'поражение'


class Battle(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сражение #{self.pk}'
