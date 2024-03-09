from django import forms

from games.models import Participant, Battle, Hero
from games.validators import user_exists


class BattleForm(forms.Form):
    WINNER_CHOICES = (
        ('won', 'Да!!!'),
        ('lost', 'Нет :(')
    )

    my_hero = forms.ModelChoiceField(queryset=Hero.objects.all(),
                                     label='Ваш герой',
                                     required=True)
    enemy_hero = forms.ModelChoiceField(queryset=Hero.objects.all(),
                                        label='Герой противника',
                                        required=True)
    enemy_user = forms.CharField(label='Имя противника', required=True,
                                 validators=(user_exists,))
    winner = forms.BooleanField(label='Вы победили?', required=False)
