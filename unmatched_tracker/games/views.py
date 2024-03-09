from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.contrib.auth import get_user_model
from games.forms import BattleForm
from games.models import Battle, Participant

from django.urls import reverse, reverse_lazy

User = get_user_model()


class BattleListView(ListView):
    model = Battle
    paginate_by = 30
    template_name = 'games/index.html'


class BattleCreateView(FormView):
    form_class = BattleForm
    template_name = 'games/create.html'
    success_url = reverse_lazy('games:index')

    def form_valid(self, form):
        winner = form.cleaned_data['winner']
        battle = Battle.objects.create()
        my_participant = Participant.objects.create(
            hero=form.cleaned_data['my_hero'],
            user=self.request.user,
            is_winner=winner,
            battle=battle
        )
        enemy_participant = Participant.objects.create(
            hero=form.cleaned_data['enemy_hero'],
            user=User.objects.get(username=form.cleaned_data['enemy_user']),
            is_winner=not winner,
            battle=battle
        )
        return super().form_valid(form)


class BattleDetailView(DetailView):
    model = Battle
