# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.template.defaultfilters import mark_safe
from datetime import date

class Player(models.Model):
    name = models.CharField('Nome', max_length=200)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Allenatore'
        verbose_name_plural = 'Allenatori'
        ordering = ['name']
        
class Team(models.Model):
    name = models.CharField('Nome', max_length=200)
#    player = models.ForeignKey(Player,
#                               verbose_name='Player',
#                               null=True,
#                               blank=True)
#    tournament = models.ForeignKey(Tournament, verbose_name='Torneo')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Squadra'
        verbose_name_plural = 'Squadre'

class Scorer(models.Model):
    name = models.CharField('Nome', max_length=200)
    team = models.ForeignKey(Team,
                             verbose_name="Squadra")
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Giocatore'
        verbose_name_plural = 'Giocatori'

class Tournament(models.Model):
    name = models.CharField('Nome', max_length=200)
    creation_date = models.DateField('Data creazione')
    second_round = models.BooleanField('Girone di ritorno')
    
    def __unicode__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Tournament._meta.fields]
    
    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Tornei'
        ordering = ['name']

class TournamentTeams(models.Model):
    tournament = models.ForeignKey(Tournament,
                                   verbose_name='Torneo')
    player = models.ForeignKey(Player,
                               verbose_name='Player',
                               null=False,
                               blank=False)
    team = models.ForeignKey(Team,
                               verbose_name='Team',
                               null=False,
                               blank=False)
    
    def __unicode__(self):
        return u'{} - {} - {}'.format(self.tournament.name, self.player.name, self.team.name)
    
    class Meta:
        verbose_name = 'Squadra Torneo'
        verbose_name_plural = 'Squadre Torneo'

class TournamentDay(models.Model):
    tournament = models.ForeignKey(Tournament,
                                   verbose_name='Torneo')
    day = models.IntegerField('Giornata')
    
    def __unicode__(self):
        return u'{} - {} giornata'.format(self.tournament.name, self.day)
    
    class Meta:
        verbose_name = 'Giornata'
        verbose_name_plural = 'Giornate'

class Match(models.Model):
    team1 = models.ForeignKey(TournamentTeams,
                               verbose_name='Team 1',
                               null=False,
                               blank=False,
                               related_name='team2')
    team2 = models.ForeignKey(TournamentTeams,
                               verbose_name='Team 2',
                               null=False,
                               blank=False,
                               related_name='team1')
    day = models.ForeignKey(TournamentDay,
                            verbose_name='Giornata')
    goal_team1 = models.IntegerField('Goal squadra 1',
                                     null=True)
    goal_team2 = models.IntegerField('Goal squadra 2',
                                     null=True)
    
    creation_date = models.DateTimeField('Data creazione',
                                         default=datetime.today())
    
    played_on = models.DateTimeField('Data partita',
                                     null=True)
    
    def __unicode__(self):
        return u'{} - {} giornata - {} vs. {}'.format(self.day.tournament.name, self.day.day, self.team1.team.name, self.team2.team.name)
    
    class Meta:
        verbose_name = 'Partita'
        verbose_name_plural = 'Partite'

class MatchGoals(models.Model):
    match = models.ForeignKey(Match,
                             verbose_name='Match')
    team = models.ForeignKey(TournamentTeams,
                             verbose_name='Team')
    scorer = models.ForeignKey(Scorer,
                               verbose_name='Giocatore')
    owngoal = models.BooleanField('Autogol')
    
    def __unicode__(self):
        return u'{} ({}) - {}'.format(self.scorer.name, self.owngoal, self.team.team.name)
    
    class Meta:
        verbose_name = 'Gol'
        verbose_name_plural = 'Gol'
    