# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timeline'
        db.create_table('timelinejs_timeline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('timelinejs', ['Timeline'])

        # Adding model 'TimelineEvent'
        db.create_table('timelinejs_timelineevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Timeline'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('timelinejs', ['TimelineEvent'])


    def backwards(self, orm):
        # Deleting model 'Timeline'
        db.delete_table('timelinejs_timeline')

        # Deleting model 'TimelineEvent'
        db.delete_table('timelinejs_timelineevent')


    models = {
        'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        'timelinejs.timelineevent': {
            'Meta': {'object_name': 'TimelineEvent'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timelinejs.Timeline']"})
        }
    }

    complete_apps = ['timelinejs']