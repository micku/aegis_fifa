# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'tournaments_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'tournaments', ['Player'])

        # Adding model 'Tournament'
        db.create_table(u'tournaments_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creation_date', self.gf('django.db.models.fields.DateField')()),
            ('second_round', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tournaments', ['Tournament'])

        # Adding model 'Team'
        db.create_table(u'tournaments_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Player'], null=True, blank=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'])),
        ))
        db.send_create_signal(u'tournaments', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'tournaments_player')

        # Deleting model 'Tournament'
        db.delete_table(u'tournaments_tournament')

        # Deleting model 'Team'
        db.delete_table(u'tournaments_team')


    models = {
        u'tournaments.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tournaments.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Player']", 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        },
        u'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'second_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tournaments']