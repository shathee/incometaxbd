# Generated by Django 2.2.6 on 2021-01-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Zone Name')),
                ('acc_code_company', models.CharField(blank=True, max_length=20, null=True)),
                ('acc_code_except_company', models.CharField(blank=True, max_length=20, null=True)),
                ('acc_code_other_fee', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
