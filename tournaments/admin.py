from django.contrib import admin
from tournaments.models import *

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(TournamentTeams)
admin.site.register(TournamentDay)
admin.site.register(Match)
admin.site.register(MatchGoals)
admin.site.register(Scorer)