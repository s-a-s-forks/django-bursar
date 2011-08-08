# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'LineItem.sku'
        db.alter_column('bursar_lineitem', 'sku', self.gf('django.db.models.fields.CharField')(max_length=7))


    def backwards(self, orm):
        
        # Changing field 'LineItem.sku'
        db.alter_column('bursar_lineitem', 'sku', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'bursar.authorization': {
            'Meta': {'object_name': 'Authorization'},
            'amount': ('bursar.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'capture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authorizations'", 'to': "orm['bursar.Payment']"}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authorizations'", 'to': "orm['bursar.Purchase']"}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        },
        'bursar.creditcarddetail': {
            'Meta': {'object_name': 'CreditCardDetail'},
            'card_holder': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'credit_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'display_cc': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'encrypted_cc': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'expire_month': ('django.db.models.fields.IntegerField', [], {}),
            'expire_year': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_num': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'payment': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'creditcard'", 'unique': 'True', 'to': "orm['bursar.Payment']"}),
            'start_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'bursar.lineitem': {
            'Meta': {'ordering': "('ordering',)", 'object_name': 'LineItem'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discount': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lineitems'", 'to': "orm['bursar.Purchase']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '18', 'decimal_places': '6'}),
            'shipping': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'sku': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '7'}),
            'sub_total': ('bursar.fields.CurrencyField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'tax': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'total': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '2'}),
            'unit_price': ('bursar.fields.CurrencyField', [], {'max_digits': '18', 'decimal_places': '10'})
        },
        'bursar.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('bursar.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments'", 'to': "orm['bursar.Purchase']"}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        },
        'bursar.paymentfailure': {
            'Meta': {'object_name': 'PaymentFailure'},
            'amount': ('bursar.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paymentfailures'", 'null': 'True', 'to': "orm['bursar.Purchase']"}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        },
        'bursar.paymentnote': {
            'Meta': {'object_name': 'PaymentNote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': "orm['bursar.Payment']"})
        },
        'bursar.paymentpending': {
            'Meta': {'object_name': 'PaymentPending'},
            'amount': ('bursar.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'capture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paymentspending'", 'to': "orm['bursar.Payment']"}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paymentspending'", 'to': "orm['bursar.Purchase']"}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'})
        },
        'bursar.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'bill_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'bill_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'}),
            'bill_postal_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'bill_state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'bill_street1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'bill_street2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'client_ct': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'client_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'orderno': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'ship_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'ship_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'}),
            'ship_postal_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'ship_state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'ship_street1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'ship_street2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'shipping': ('bursar.fields.CurrencyField', [], {'display_decimal': '4', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'sub_total': ('bursar.fields.CurrencyField', [], {'display_decimal': '4', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'tax': ('bursar.fields.CurrencyField', [], {'display_decimal': '4', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('bursar.fields.CurrencyField', [], {'display_decimal': '4', 'max_digits': '18', 'decimal_places': '2'})
        },
        'bursar.recurringlineitem': {
            'Meta': {'object_name': 'RecurringLineItem'},
            'expire_length': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expire_unit': ('django.db.models.fields.CharField', [], {'default': "'DAY'", 'max_length': '5'}),
            'lineitem': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'recurdetails'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['bursar.LineItem']"}),
            'recurring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recurring_price': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '2'}),
            'recurring_shipping': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '2'}),
            'recurring_times': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'trial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trial_length': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'trial_price': ('bursar.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '2'}),
            'trial_times': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['bursar']
