# Generated by Django 2.1.15 on 2020-08-17 19:59

from datetime import datetime
import pytz

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


def add_existing_data(apps, schema_editor):
    chapter = apps.get_model("authentication", "chapter")
    chapter.objects.bulk_create(
        [
            chapter(
                location='ASRG-S',
                city='Stuttgart',
                country='Germany',
                lead='Sven Schran',
                foundation=datetime(2018, 7, 18, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-D',
                city='Detroit',
                country='USA',
                lead='Brandon Barry',
                foundation=datetime(2018, 5, 2, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-TLV',
                city='Tel Aviv',
                country='Israel',
                lead='Eli Ben Ami',
                foundation=datetime(2019, 2, 28, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-C',
                city='Cluj-Napoca',
                country='Romania',
                lead='Dan Paunescu',
                foundation=datetime(2019, 4, 10, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-SIN',
                city='Singapore',
                country='Singapore',
                lead='Alina Tan',
                foundation=datetime(2019, 8, 12, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-MUC',
                city='Munich',
                country='Germany',
                lead='Jana von Wedel',
                foundation=datetime(2019, 11, 4, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-CAI',
                city='Cairo',
                country='Egypt',
                lead='Mohamed Madbouly',
                foundation=datetime(2019, 11, 10, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-SHA',
                city='Shanghai',
                country='China',
                lead='',
                foundation=datetime(2020, 1, 4, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-BER',
                city='Berlin',
                country='Germany',
                lead='Christian Schmidt-Janssen',
                foundation=datetime(2020, 1, 6, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-PIT',
                city='Pittsburgh',
                country='USA',
                lead='Shalabh Jain',
                foundation=datetime(2020, 1, 26, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-SFO',
                city='San Francisco',
                country='USA',
                lead='',
                foundation=datetime(2020, 1, 27, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-FRA',
                city='Darmstadt',
                country='Germany',
                lead='Patric Lenhart',
                foundation=datetime(2020, 2, 20, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-JPN',
                city='Tokyo',
                country='Japan',
                lead='M. Kamel Ghali',
                foundation=datetime(2020, 2, 15, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-OXF',
                city='Oxford',
                country='UK',
                lead='Erica Yang',
                foundation=datetime(2020, 2, 20, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-SYD',
                city='Sydney',
                country='Australia',
                lead='Jasmine Rhyder',
                foundation=datetime(2020, 3, 11, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-IASI',
                city='Iasi',
                country='Romania',
                lead='Irina-Georgiana Oancea',
                foundation=datetime(2020, 3, 16, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-DNCR',
                city='Delhi',
                country='India',
                lead='Shaurya Singh',
                foundation=datetime(2020, 3, 31, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-DAY',
                city='Dayton',
                country='USA',
                lead='Bryan Fite',
                foundation=datetime(2020, 4, 9, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-REC',
                city='Recife',
                country='Brasil',
                lead='Divanilson Campelo',
                foundation=datetime(2020, 4, 9, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-BLR',
                city='Bangalore',
                country='India',
                lead='Koushik Pal',
                foundation=datetime(2020, 4, 10, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-LAX',
                city='Los Angeles',
                country='USA',
                lead='Kyle Crockett',
                foundation=datetime(2020, 4, 16, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-BUC',
                city='Bucharest',
                country='Romania',
                lead='Anas Ahammed K A',
                foundation=datetime(2020, 7, 21, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-QRO',
                city='Querétaro',
                country='Mexico',
                lead='Alonso Jáuregui Martínez',
                foundation=datetime(2020, 6, 29, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-CGN',
                city='Cologne',
                country='Germany',
                lead='Stefan Würth',
                foundation=datetime(2020, 6, 29, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-TOR',
                city='Toronto',
                country='Canada',
                lead='AJ Khan',
                foundation=datetime(2020, 7, 1, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-WIN',
                city='Windsor',
                country='Canada',
                lead='Ikjot Saini',
                foundation=datetime(2020, 7, 1, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-KER',
                city='Kochi',
                country='India',
                lead='Anas Ahammed K A',
                foundation=datetime(2020, 7, 21, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-VIE',
                city='Vienna',
                country='Austria',
                lead='Martin Schmiedecker',
                foundation=datetime(2020, 7, 27, 0, 0, 0, 0, pytz.UTC),
            ),
            chapter(
                location='ASRG-HYD',
                city='Hyderabad',
                country='India',
                lead='Shravan Paidipala',
                foundation=datetime(2020, 7, 27, 0, 0, 0, 0, pytz.UTC),
            ),
        ]
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={'unique': 'A user with that username already exists.'},
                        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name='username',
                    ),
                ),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                        verbose_name='active',
                    ),
                ),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={'verbose_name': 'user', 'verbose_name_plural': 'users', 'abstract': False,},
            managers=[('objects', django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'location',
                    models.CharField(
                        choices=[
                            ('ASRG-S', 'ASRG-Stuttgart'),
                            ('ASRG-D', 'ASRG-Detroit'),
                            ('ASRG-TLV', 'ASRG-Tel Aviv'),
                            ('ASRG-C', 'ASRG-Cluj-Napoca'),
                            ('ASRG-SIN', 'ASRG-Singapore'),
                            ('ASRG-MUC', 'ASRG-Munich'),
                            ('ASRG-CAI', 'ASRG-Cairo'),
                            ('ASRG-SHA', 'ASRG-Shanghai'),
                            ('ASRG-BER', 'ASRG-Berlin'),
                            ('ASRG-PIT', 'ASRG-Pittsburgh'),
                            ('ASRG-SFO', 'ASRG-San Francisco'),
                            ('ASRG-FRA', 'ASRG-Darmstadt'),
                            ('ASRG-JPN', 'ASRG-Tokyo'),
                            ('ASRG-OXF', 'ASRG-Oxford'),
                            ('ASRG-SYD', 'ASRG-Sydney'),
                            ('ASRG-IASI', 'ASRG-Iasi'),
                            ('ASRG-DNCR', 'ASRG-Delhi'),
                            ('ASRG-DAY', 'ASRG-Dayton'),
                            ('ASRG-REC', 'ASRG-Recife'),
                            ('ASRG-BLR', 'ASRG-Bangalore'),
                            ('ASRG-LAX', 'ASRG-Los Angeles'),
                            ('ASRG-BUC', 'ASRG-Bucharest'),
                            ('ASRG-QRO', 'ASRG-Querétaro'),
                            ('ASRG-CGN', 'ASRG-Cologne'),
                            ('ASRG-TOR', 'ASRG-Toronto'),
                            ('ASRG-WIN', 'ASRG-Windsor'),
                            ('ASRG-KER', 'ASRG-Kochi'),
                            ('ASRG-VIE', 'ASRG-Vienna'),
                            ('ASRG-HYD', 'ASRG-Hyderabad'),
                        ],
                        default=('ASRG-S', 'ASRG-Stuttgart'),
                        max_length=24,
                    ),
                ),
                ('city', models.CharField(blank=True, max_length=56)),
                ('country', models.CharField(blank=True, max_length=56)),
                ('lead', models.CharField(blank=True, max_length=56)),
                ('foundation', models.DateTimeField(blank=True)),
            ],
            options={
                'permissions': [
                    ('ASRG-S', 'ASRG-S'),
                    ('ASRG-local-lead-S', 'ASRG-local-lead-S'),
                    ('ASRG-D', 'ASRG-D'),
                    ('ASRG-local-lead-D', 'ASRG-local-lead-D'),
                    ('ASRG-TLV', 'ASRG-TLV'),
                    ('ASRG-local-lead-TLV', 'ASRG-local-lead-TLV'),
                    ('ASRG-C', 'ASRG-C'),
                    ('ASRG-local-lead-C', 'ASRG-local-lead-C'),
                    ('ASRG-SIN', 'ASRG-SIN'),
                    ('ASRG-local-lead-SIN', 'ASRG-local-lead-SIN'),
                    ('ASRG-MUC', 'ASRG-MUC'),
                    ('ASRG-local-lead-MUC', 'ASRG-local-lead-MUC'),
                    ('ASRG-CAI', 'ASRG-CAI'),
                    ('ASRG-local-lead-CAI', 'ASRG-local-lead-CAI'),
                    ('ASRG-SHA', 'ASRG-SHA'),
                    ('ASRG-local-lead-SHA', 'ASRG-local-lead-SHA'),
                    ('ASRG-BER', 'ASRG-BER'),
                    ('ASRG-local-lead-BER', 'ASRG-local-lead-BER'),
                    ('ASRG-PIT', 'ASRG-PIT'),
                    ('ASRG-local-lead-PIT', 'ASRG-local-lead-PIT'),
                    ('ASRG-SFO', 'ASRG-SFO'),
                    ('ASRG-local-lead-SFO', 'ASRG-local-lead-SFO'),
                    ('ASRG-FRA', 'ASRG-FRA'),
                    ('ASRG-local-lead-FRA', 'ASRG-local-lead-FRA'),
                    ('ASRG-JPN', 'ASRG-JPN'),
                    ('ASRG-local-lead-JPN', 'ASRG-local-lead-JPN'),
                    ('ASRG-OXF', 'ASRG-OXF'),
                    ('ASRG-local-lead-OXF', 'ASRG-local-lead-OXF'),
                    ('ASRG-SYD', 'ASRG-SYD'),
                    ('ASRG-local-lead-SYD', 'ASRG-local-lead-SYD'),
                    ('ASRG-IASI', 'ASRG-IASI'),
                    ('ASRG-local-lead-IASI', 'ASRG-local-lead-IASI'),
                    ('ASRG-DNCR', 'ASRG-DNCR'),
                    ('ASRG-local-lead-DNCR', 'ASRG-local-lead-DNCR'),
                    ('ASRG-DAY', 'ASRG-DAY'),
                    ('ASRG-local-lead-DAY', 'ASRG-local-lead-DAY'),
                    ('ASRG-REC', 'ASRG-REC'),
                    ('ASRG-local-lead-REC', 'ASRG-local-lead-REC'),
                    ('ASRG-BLR', 'ASRG-BLR'),
                    ('ASRG-local-lead-BLR', 'ASRG-local-lead-BLR'),
                    ('ASRG-LAX', 'ASRG-LAX'),
                    ('ASRG-local-lead-LAX', 'ASRG-local-lead-LAX'),
                    ('ASRG-BUC', 'ASRG-BUC'),
                    ('ASRG-local-lead-BUC', 'ASRG-local-lead-BUC'),
                    ('ASRG-QRO', 'ASRG-QRO'),
                    ('ASRG-local-lead-QRO', 'ASRG-local-lead-QRO'),
                    ('ASRG-CGN', 'ASRG-CGN'),
                    ('ASRG-local-lead-CGN', 'ASRG-local-lead-CGN'),
                    ('ASRG-TOR', 'ASRG-TOR'),
                    ('ASRG-local-lead-TOR', 'ASRG-local-lead-TOR'),
                    ('ASRG-WIN', 'ASRG-WIN'),
                    ('ASRG-local-lead-WIN', 'ASRG-local-lead-WIN'),
                    ('ASRG-KER', 'ASRG-KER'),
                    ('ASRG-local-lead-KER', 'ASRG-local-lead-KER'),
                    ('ASRG-VIE', 'ASRG-VIE'),
                    ('ASRG-local-lead-VIE', 'ASRG-local-lead-VIE'),
                    ('ASRG-HYD', 'ASRG-HYD'),
                    ('ASRG-local-lead-HYD', 'ASRG-local-lead-HYD'),
                ],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='chapter',
            field=models.ManyToManyField(related_name='user', to='authentication.Chapter'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups',
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                help_text='Specific permissions for this user.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Permission',
                verbose_name='user permissions',
            ),
        ),
        migrations.RunPython(add_existing_data),
    ]