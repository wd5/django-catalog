# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CatalogCategory'
        db.create_table('catalog_catalogcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.CatalogCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('catalog', ['CatalogCategory'])

        # Adding model 'CatalogPost'
        db.create_table('catalog_catalogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalog_catalogpost_related', to=orm['auth.User'])),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='active', max_length=15, db_index=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Country'], null=True, blank=True)),
            ('city', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['location.City'])),
        ))
        db.send_create_signal('catalog', ['CatalogPost'])

        # Adding M2M table for field category on 'CatalogPost'
        db.create_table('catalog_catalogpost_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('catalogpost', models.ForeignKey(orm['catalog.catalogpost'], null=False)),
            ('catalogcategory', models.ForeignKey(orm['catalog.catalogcategory'], null=False))
        ))
        db.create_unique('catalog_catalogpost_category', ['catalogpost_id', 'catalogcategory_id'])

        # Adding model 'CatalogPostImages'
        db.create_table('catalog_catalogpostimages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['catalog.CatalogPost'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('catalog', ['CatalogPostImages'])


    def backwards(self, orm):
        # Deleting model 'CatalogCategory'
        db.delete_table('catalog_catalogcategory')

        # Deleting model 'CatalogPost'
        db.delete_table('catalog_catalogpost')

        # Removing M2M table for field category on 'CatalogPost'
        db.delete_table('catalog_catalogpost_category')

        # Deleting model 'CatalogPostImages'
        db.delete_table('catalog_catalogpostimages')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'catalog.catalogcategory': {
            'Meta': {'object_name': 'CatalogCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalog.CatalogCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'catalog.catalogpost': {
            'Meta': {'ordering': "['pk']", 'object_name': 'CatalogPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalog_catalogpost_related'", 'to': "orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.CatalogCategory']", 'symmetrical': 'False'}),
            'city': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['location.City']"}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Country']", 'null': 'True', 'blank': 'True'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '15', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.catalogpostimages': {
            'Meta': {'object_name': 'CatalogPostImages'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['catalog.CatalogPost']", 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'location.city': {
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'County': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'DmaId': ('django.db.models.fields.IntegerField', [], {}),
            'Latitude': ('django.db.models.fields.FloatField', [], {}),
            'Longitude': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'TimeZone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['location.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Region']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '255', 'db_index': 'True'})
        },
        'location.country': {
            'Comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Currency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'CurrencyCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'FIPS104': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ISO2': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ISON': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'MapReference': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'NationalityPlural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'NationalitySingular': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '255', 'db_index': 'True'})
        },
        'location.region': {
            'ADM1Code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['catalog']