# Generated by Django 2.1.4 on 2019-07-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(db_column='year')),
                ('stock_name', models.CharField(db_column='stock_name', max_length=255)),
                ('share_capital', models.DecimalField(db_column='share_capital', decimal_places=2, max_digits=20)),
                ('reserve_surplus', models.DecimalField(db_column='reserve_surplus', decimal_places=2, max_digits=20)),
                ('net_worth', models.DecimalField(db_column='net_worth', decimal_places=2, max_digits=20)),
                ('secured_loan', models.DecimalField(db_column='secured_loan', decimal_places=2, max_digits=20)),
                ('unsecured_loan', models.DecimalField(db_column='unsecured_loan', decimal_places=2, max_digits=20)),
                ('gross_block', models.DecimalField(db_column='gross_block', decimal_places=2, max_digits=20)),
                ('depreciation', models.DecimalField(db_column='depreciation', decimal_places=2, max_digits=20)),
                ('net_block', models.DecimalField(db_column='net_block', decimal_places=2, max_digits=20)),
                ('capital_wip', models.DecimalField(db_column='capital_wip', decimal_places=2, max_digits=20)),
                ('investments', models.DecimalField(db_column='investments', decimal_places=2, max_digits=20)),
                ('inventories', models.DecimalField(db_column='inventories', decimal_places=2, max_digits=20)),
                ('sundry_debtors', models.DecimalField(db_column='sundry_debtors', decimal_places=2, max_digits=20)),
                ('cash_and_bank', models.DecimalField(db_column='cash_and_bank', decimal_places=2, max_digits=20)),
                ('loan_and_advances', models.DecimalField(db_column='loan_and_advances', decimal_places=2, max_digits=20)),
                ('total_current_assests', models.DecimalField(db_column='total_current_assests', decimal_places=2, max_digits=20)),
                ('current_liabilities', models.DecimalField(db_column='current_liabilities', decimal_places=2, max_digits=20)),
                ('provisions', models.DecimalField(db_column='provisions', decimal_places=2, max_digits=20)),
                ('total_current_liabilites', models.DecimalField(db_column='total_current_liabilites', decimal_places=2, max_digits=20)),
                ('net_current_assets', models.DecimalField(db_column='net_current_assets', decimal_places=2, max_digits=20)),
                ('misc_expenses', models.DecimalField(db_column='misc_expenses', decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'balance_sheet',
                'ordering': ['year'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShortBalanceSheetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(db_column='year')),
                ('stock_name', models.CharField(db_column='stock_name', max_length=255)),
                ('net_worth', models.DecimalField(db_column='net_worth', decimal_places=2, max_digits=20)),
                ('total_liabilities', models.DecimalField(db_column='total_liabilities', decimal_places=2, max_digits=20)),
                ('total_current_assests', models.DecimalField(db_column='total_current_assests', decimal_places=2, max_digits=20)),
                ('net_current_assets', models.DecimalField(db_column='net_current_assets', decimal_places=2, max_digits=20)),
                ('total_assets', models.DecimalField(db_column='total_assets', decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'short_balance_sheet',
                'managed': True,
            },
        ),
    ]