# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MatchGoals.team'
        db.alter_column(u'tournaments_matchgoals', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.TournamentTeams']))

        # Changing field 'Match.team1'
        db.alter_column(u'tournaments_match', 'team1_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.TournamentTeams']))

        # Changing field 'Match.team2'
        db.alter_column(u'tournaments_match', 'team2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.TournamentTeams']))

    def backwards(self, orm):

        # Changing field 'MatchGoals.team'
        db.alter_column(u'tournaments_matchgoals', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team']))

        # Changing field 'Match.team1'
        db.alter_column(u'tournaments_match', 'team1_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team']))

        # Changing field 'Match.team2'
        db.alter_column(u'tournaments_match', 'team2_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team']))

    models = {
        u'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.TournamentDay']"}),
            'goal_team1': ('django.db.models.fields.IntegerField', [], {}),
            'goal_team2': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team2'", 'to': u"orm['tournaments.TournamentTeams']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team1'", 'to': u"orm['tournaments.TournamentTeams']"})
        },
        u'tournaments.matchgoals': {
            'Meta': {'object_name': 'MatchGoals'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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