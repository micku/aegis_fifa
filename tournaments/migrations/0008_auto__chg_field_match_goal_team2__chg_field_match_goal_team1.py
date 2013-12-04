# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Match.goal_team2'
        db.alter_column(u'tournaments_match', 'goal_team2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.goal_team1'
        db.alter_column(u'tournaments_match', 'goal_team1', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Match.goal_team2'
        db.alter_column(u'tournaments_match', 'goal_team2', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Match.goal_team1'
        db.alter_column(u'tournaments_match', 'goal_team1', self.gf('django.db.models.fields.IntegerField')(default=''))

    models = {
        u'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 26, 0, 0)'}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.TournamentDay']"}),
            'goal_team1': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'goal_team2': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team2'", 'to': u"orm['tournaments.TournamentTeams']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team1'", 'to': u"orm['tournaments.TournamentTeams']"})
        },
        u'tournaments.matchgoals': {
            'Meta': {'object_name': 'MatchGoals'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Match']"}),
            'owngoal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scorer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Scorer']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.TournamentTeams']"})
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