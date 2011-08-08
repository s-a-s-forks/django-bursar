# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Authorization'
        db.create_table('bursar_authorization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('amount', self.gf('bursar.fields.CurrencyField')(null=True, max_digits=18, decimal_places=2, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reason_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authorizations', to=orm['bursar.Purchase'])),
            ('capture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authorizations', to=orm['bursar.Payment'])),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bursar', ['Authorization'])

        # Adding model 'CreditCardDetail'
        db.create_table('bursar_creditcarddetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment', self.gf('django.db.models.fields.related.OneToOneField')(related_name='creditcard', unique=True, to=orm['bursar.Payment'])),
            ('credit_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('display_cc', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('encrypted_cc', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('expire_month', self.gf('django.db.models.fields.IntegerField')()),
            ('expire_year', self.gf('django.db.models.fields.IntegerField')()),
            ('card_holder', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('start_month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('start_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('issue_num', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('bursar', ['CreditCardDetail'])

        # Adding model 'Payment'
        db.create_table('bursar_payment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('amount', self.gf('bursar.fields.CurrencyField')(null=True, max_digits=18, decimal_places=2, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reason_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payments', to=orm['bursar.Purchase'])),
            ('success', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bursar', ['Payment'])

        # Adding model 'PaymentFailure'
        db.create_table('bursar_paymentfailure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('amount', self.gf('bursar.fields.CurrencyField')(null=True, max_digits=18, decimal_places=2, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reason_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='paymentfailures', null=True, to=orm['bursar.Purchase'])),
        ))
        db.send_create_signal('bursar', ['PaymentFailure'])

        # Adding model 'PaymentNote'
        db.create_table('bursar_paymentnote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notes', to=orm['bursar.Payment'])),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bursar', ['PaymentNote'])

        # Adding model 'PaymentPending'
        db.create_table('bursar_paymentpending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('amount', self.gf('bursar.fields.CurrencyField')(null=True, max_digits=18, decimal_places=2, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reason_code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(related_name='paymentspending', to=orm['bursar.Purchase'])),
            ('capture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='paymentspending', to=orm['bursar.Payment'])),
        ))
        db.send_create_signal('bursar', ['PaymentPending'])

        # Adding model 'Purchase'
        db.create_table('bursar_purchase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('client_pk', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('client_ct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('orderno', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('ship_street1', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('ship_street2', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('ship_city', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('ship_state', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('ship_postal_code', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('ship_country', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('bill_street1', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('bill_street2', self.gf('django.db.models.fields.CharField')(default='', max_length=80)),
            ('bill_city', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('bill_state', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('bill_postal_code', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('bill_country', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('sub_total', self.gf('bursar.fields.CurrencyField')(display_decimal=4, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('tax', self.gf('bursar.fields.CurrencyField')(display_decimal=4, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('shipping', self.gf('bursar.fields.CurrencyField')(display_decimal=4, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('total', self.gf('bursar.fields.CurrencyField')(display_decimal=4, max_digits=18, decimal_places=2)),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('bursar', ['Purchase'])

        # Adding model 'LineItem'
        db.create_table('bursar_lineitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(default='1', max_length=255)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lineitems', to=orm['bursar.Purchase'])),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=18, decimal_places=6)),
            ('unit_price', self.gf('bursar.fields.CurrencyField')(max_digits=18, decimal_places=10)),
            ('sub_total', self.gf('bursar.fields.CurrencyField')(max_digits=18, decimal_places=10)),
            ('shipping', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=10)),
            ('discount', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=10)),
            ('tax', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=10)),
            ('total', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=2)),
        ))
        db.send_create_signal('bursar', ['LineItem'])

        # Adding model 'RecurringLineItem'
        db.create_table('bursar_recurringlineitem', (
            ('lineitem', self.gf('django.db.models.fields.related.OneToOneField')(related_name='recurdetails', unique=True, primary_key=True, to=orm['bursar.LineItem'])),
            ('recurring', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recurring_price', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=2)),
            ('recurring_shipping', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=2)),
            ('recurring_times', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('expire_length', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('trial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('trial_price', self.gf('bursar.fields.CurrencyField')(default='0.00', max_digits=18, decimal_places=2)),
            ('trial_length', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('trial_times', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('expire_unit', self.gf('django.db.models.fields.CharField')(default='DAY', max_length=5)),
        ))
        db.send_create_signal('bursar', ['RecurringLineItem'])


    def backwards(self, orm):
        
        # Deleting model 'Authorization'
        db.delete_table('bursar_authorization')

        # Deleting model 'CreditCardDetail'
        db.delete_table('bursar_creditcarddetail')

        # Deleting model 'Payment'
        db.delete_table('bursar_payment')

        # Deleting model 'PaymentFailure'
        db.delete_table('bursar_paymentfailure')

        # Deleting model 'PaymentNote'
        db.delete_table('bursar_paymentnote')

        # Deleting model 'PaymentPending'
        db.delete_table('bursar_paymentpending')

        # Deleting model 'Purchase'
        db.delete_table('bursar_purchase')

        # Deleting model 'LineItem'
        db.delete_table('bursar_lineitem')

        # Deleting model 'RecurringLineItem'
        db.delete_table('bursar_recurringlineitem')


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
            'sku': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '255'}),
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
