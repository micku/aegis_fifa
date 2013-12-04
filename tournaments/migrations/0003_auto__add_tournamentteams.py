# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TournamentTeams'
        db.create_table(u'tournaments_tournamentteams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Player'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Team'])),
        ))
        db.send_create_signal(u'tournaments', ['TournamentTeams'])


    def backwards(self, orm):
        # Deleting model 'TournamentTeams'
        db.delete_table(u'tournaments_tournamentteams')


    models = {
        u'tournaments.player': {
            'Meta': {'ordering': "['name']", 'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'tournaments.tournamentteams': {
            'Meta': {'object_name': 'TournamentTeams'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        }
    }

    complete_apps = ['tournaments']