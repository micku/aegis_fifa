# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TournamentDay'
        db.create_table(u'tournaments_tournamentday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tournaments', ['TournamentDay'])

        # Adding model 'Scorer'
        db.create_table(u'tournaments_scorer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team'])),
        ))
        db.send_create_signal(u'tournaments', ['Scorer'])

        # Adding model 'MatchGoals'
        db.create_table(u'tournaments_matchgoals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team'])),
            ('scorer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Scorer'])),
            ('owngoal', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tournaments', ['MatchGoals'])

        # Adding model 'Match'
        db.create_table(u'tournaments_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team2', to=orm['tournaments.Team'])),
            ('team2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team1', to=orm['tournaments.Team'])),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.TournamentDay'])),
            ('goal_team1', self.gf('django.db.models.fields.IntegerField')()),
            ('goal_team2', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tournaments', ['Match'])


    def backwards(self, orm):
        # Deleting model 'TournamentDay'
        db.delete_table(u'tournaments_tournamentday')

        # Deleting model 'Scorer'
        db.delete_table(u'tournaments_scorer')

        # Deleting model 'MatchGoals'
        db.delete_table(u'tournaments_matchgoals')

        # Deleting model 'Match'
        db.delete_table(u'tournaments_match')


    models = {
        u'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.TournamentDay']"}),
            'goal_team1': ('django.db.models.fields.IntegerField', [], {}),
            'goal_team2': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team2'", 'to': u"orm['tournaments.Team']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team1'", 'to': u"orm['tournaments.Team']"})
        },
        u'tournaments.matchgoals': {
            'Meta': {'object_name': 'MatchGoals'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owngoal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scorer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Scorer']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Team']"})
        },
        u'tournaments.player': {
            'Meta': {'ordering': "['name']", 'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tournaments.scorer': {
            'Meta': {'object_name': 'Scorer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Team']"})
        },
        u'tournaments.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tournaments.tournament': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tournament'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tournaments.tournamentday': {
            'Meta': {'object_name': 'TournamentDay'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        },
        u'tournaments.tournamentteams': {
            'Meta': {'object_name': 'TournamentTeams'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        }
    }

    complete_apps = ['tournaments']