# Generated by Django 4.1.5 on 2023-01-04 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.wallet')),
            ],
        ),
    ]
