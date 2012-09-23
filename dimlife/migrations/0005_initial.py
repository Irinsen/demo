# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table('dimlife_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('access_mask', self.gf('django.db.models.fields.CharField')(default='All', max_length=100, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_show', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='NOT_ACTIVE', max_length=100)),
            ('impotant', self.gf('django.db.models.fields.CharField')(default='Unimportant', max_length=100)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('dimlife', ['News'])

        # Adding model 'Category'
        db.create_table('dimlife_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dimlife.News'], null=True, blank=True)),
        ))
        db.send_create_signal('dimlife', ['Category'])

        # Adding model 'Keywords'
        db.create_table('dimlife_keywords', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dimlife', ['Keywords'])

        # Adding M2M table for field news on 'Keywords'
        db.create_table('dimlife_keywords_news', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('keywords', models.ForeignKey(orm['dimlife.keywords'], null=False)),
            ('news', models.ForeignKey(orm['dimlife.news'], null=False))
        ))
        db.create_unique('dimlife_keywords_news', ['keywords_id', 'news_id'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table('dimlife_news')

        # Deleting model 'Category'
        db.delete_table('dimlife_category')

        # Deleting model 'Keywords'
        db.delete_table('dimlife_keywords')

        # Removing M2M table for field news on 'Keywords'
        db.delete_table('dimlife_keywords_news')


    models = {
        'dimlife.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dimlife.News']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dimlife.keywords': {
            'Meta': {'object_name': 'Keywords'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dimlife.News']", 'null': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dimlife.news': {
            'Meta': {'object_name': 'News'},
            'access_mask': ('django.db.models.fields.CharField', [], {'default': "'All'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_show': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impotant': ('django.db.models.fields.CharField', [], {'default': "'Unimportant'", 'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NOT_ACTIVE'", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['dimlife']