from django.urls import path

from games.views import BattleCreateView, BattleListView


app_name = 'games'

urlpatterns = [
    path('', BattleListView.as_view(), name='index'),
    path('games/create/', BattleCreateView.as_view(), name='create'),
]
