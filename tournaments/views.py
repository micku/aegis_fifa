from django.shortcuts import render
from django.db.models import Count
from tournaments.models import Tournament, Team, TournamentTeams, Match, TournamentDay,\
    Scorer, MatchGoals

def index(request):
    tournaments = Tournament.objects.all().order_by('-creation_date')[:5]
    context = {'tournaments': tournaments}
    return render(request, 'tournaments/index.html', context)

def detail(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    teams = TournamentTeams.objects.filter(tournament_id=tournament_id).order_by('team__name')
    days = TournamentDay.objects.filter(tournament_id=tournament_id)
    games = Match.objects.filter(day_id__in=days, played_on__isnull=False)
    
    for i in range(len(teams)):
        teams[i].pt = 0
        teams[i].g = 0
        teams[i].v = 0
        teams[i].n = 0
        teams[i].p = 0
        teams[i].gf = 0
        teams[i].gs = 0
        teams[i].dr = 0
        
        matches = Match.objects.filter(team1__id=teams[i].id).exclude(played_on__isnull=True)
        for m in matches:
            teams[i].g += 1
            if m.goal_team1>m.goal_team2:
                teams[i].pt += 3
                teams[i].v += 1
            elif m.goal_team1==m.goal_team2:
                teams[i].pt += 1
                teams[i].n += 1
            else:
                teams[i].p += 1
            teams[i].gf += m.goal_team1
            teams[i].gs += m.goal_team2
        
        matches = Match.objects.filter(team2__id=teams[i].id).exclude(played_on__isnull=True)
        for m in matches:
            teams[i].g += 1
            if m.goal_team1<m.goal_team2:
                teams[i].pt += 3
                teams[i].v += 1
            elif m.goal_team1==m.goal_team2:
                teams[i].pt += 1
                teams[i].n += 1
            else:
                teams[i].p += 1
            teams[i].gf += m.goal_team2
            teams[i].gs += m.goal_team1
        
        teams[i].dr = teams[i].gf - teams[i].gs
            
    ranking = sorted(teams, key=lambda team: (-team.pt, -team.dr, -team.gf))
    """
     ToDo: Fix sorting order
     - punti conquistati in classifica generale;
     - punti conquistati negli scontri diretti;
     - differenza reti negli scontri diretti;
     - differenza reti in classifica generale;
     - maggior numero di gol segnati in classifica generale;
     - sorteggio.
    """
    last_matches = sorted(games, key=lambda game: game.creation_date)[:10]
    
    scorers = MatchGoals.objects.filter(owngoal=0)\
		.values('scorer__name')\
		.annotate(total=Count('scorer__name'))\
		.order_by('-total')
    
    context = {'tournament': tournament, 'teams': teams, 'last_matches': last_matches, 'ranking': ranking, 'scorers': scorers}
    return render(request, 'tournaments/detail.html', context)

def calendar(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    days = TournamentDay.objects.filter(tournament_id=tournament_id)
    games = Match.objects.filter(day_id__in=days)
    
    context = {'tournament': tournament, 'days': days, 'games': games}
    return render(request, 'tournaments/calendar.html', context)
