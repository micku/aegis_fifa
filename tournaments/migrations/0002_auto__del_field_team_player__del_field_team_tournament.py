# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Team.player'
        db.delete_column(u'tournaments_team', 'player_id')

        # Deleting field 'Team.tournament'
        db.delete_column(u'tournaments_team', 'tournament_id')


    def backwards(self, orm):
        # Adding field 'Team.player'
        db.add_column(u'tournaments_team', 'player',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Player'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.tournament'
        db.add_column(u'tournaments_team', 'tournament',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['tournaments.Tournament']),
                      keep_default=False)


    models = {
        u'tournaments.player': {
            'Meta': {'ordering': "['name']", 'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tournaments.team': {
            'Meta': {'ordering': "['name']", 'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tournaments.tournament': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tournament'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tournaments']