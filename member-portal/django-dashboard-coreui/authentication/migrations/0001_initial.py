# Generated by Django 2.1.15 on 2020-08-08 15:31

from datetime import datetime
import pytz

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'location',
                    models.CharField(
                        choices=[
                            ('ASRG-S', 'ASRG-S'),
                            ('ASRG-D', 'ASRG-D'),
                            ('ASRG-TLV', 'ASRG-TLV'),
                            ('ASRG-C', 'ASRG-C'),
                            ('ASRG-SIN', 'ASRG-SIN'),
                            ('ASRG-MUC', 'ASRG-MUC'),
                            ('ASRG-CAI', 'ASRG-CAI'),
                            ('ASRG-SHA', 'ASRG-SHA'),
                            ('ASRG-BER', 'ASRG-BER'),
                            ('ASRG-PIT', 'ASRG-PIT'),
                            ('ASRG-SFO', 'ASRG-SFO'),
                            ('ASRG-FRA', 'ASRG-FRA'),
                            ('ASRG-JPN', 'ASRG-JPN'),
                            ('ASRG-OXF', 'ASRG-OXF'),
                            ('ASRG-SYD', 'ASRG-SYD'),
                            ('ASRG-IASI', 'ASRG-IASI'),
                            ('ASRG-DNCR', 'ASRG-DNCR'),
                            ('ASRG-DAY', 'ASRG-DAY'),
                            ('ASRG-REC', 'ASRG-REC'),
                            ('ASRG-BLR', 'ASRG-BLR'),
                            ('ASRG-LAX', 'ASRG-LAX'),
                            ('ASRG-BUC', 'ASRG-BUC'),
                            ('ASRG-QRO', 'ASRG-QRO'),
                            ('ASRG-CGN', 'ASRG-CGN'),
                            ('ASRG-TOR', 'ASRG-TOR'),
                            ('ASRG-WIN', 'ASRG-WIN'),
                            ('ASRG-KER', 'ASRG-KER'),
                            ('ASRG-VIE', 'ASRG-VIE'),
                            ('ASRG-HYD', 'ASRG-HYD'),
                        ],
                        default=('ASRG-S', 'ASRG-S'),
                        max_length=24,
                    ),
                ),
                ('city', models.CharField(blank=True, max_length=56)),
                ('country', models.CharField(blank=True, max_length=56)),
                ('lead', models.CharField(blank=True, max_length=56)),
                ('foundation', models.DateTimeField(null=True)),
                (
                    'user',
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                'permissions': [
                    ('ASRG_member', 'ASRG_member'),
                    ('ASRG_global_lead', 'ASRG_global_lead'),
                    ('ASRG_global_admin', 'ASRG_global_admin'),
                    ('ASRG_sponsor_L1', 'ASRG_sponsor_L1'),
                    ('ASRG_sponsor_L2', 'ASRG_sponsor_L2'),
                    ('ASRG_sponsor_L3', 'ASRG_sponsor_L3'),
                    ('ASRG_asip_contributor', 'ASRG_asip_contributor'),
                    ('ASRG_S', 'ASRG_S'),
                    ('ASRG_local_lead_S', 'ASRG_local_lead_S'),
                    ('ASRG_D', 'ASRG_D'),
                    ('ASRG_local_lead_D', 'ASRG_local_lead_D'),
                    ('ASRG_TLV', 'ASRG_TLV'),
                    ('ASRG_local_lead_TLV', 'ASRG_local_lead_TLV'),
                    ('ASRG_C', 'ASRG_C'),
                    ('ASRG_local_lead_C', 'ASRG_local_lead_C'),
                    ('ASRG_SIN', 'ASRG_SIN'),
                    ('ASRG_local_lead_SIN', 'ASRG_local_lead_SIN'),
                    ('ASRG_MUC', 'ASRG_MUC'),
                    ('ASRG_local_lead_MUC', 'ASRG_local_lead_MUC'),
                    ('ASRG_CAI', 'ASRG_CAI'),
                    ('ASRG_local_lead_CAI', 'ASRG_local_lead_CAI'),
                    ('ASRG_SHA', 'ASRG_SHA'),
                    ('ASRG_local_lead_SHA', 'ASRG_local_lead_SHA'),
                    ('ASRG_BER', 'ASRG_BER'),
                    ('ASRG_local_lead_BER', 'ASRG_local_lead_BER'),
                    ('ASRG_PIT', 'ASRG_PIT'),
                    ('ASRG_local_lead_PIT', 'ASRG_local_lead_PIT'),
                    ('ASRG_SFO', 'ASRG_SFO'),
                    ('ASRG_local_lead_SFO', 'ASRG_local_lead_SFO'),
                    ('ASRG_FRA', 'ASRG_FRA'),
                    ('ASRG_local_lead_FRA', 'ASRG_local_lead_FRA'),
                    ('ASRG_JPN', 'ASRG_JPN'),
                    ('ASRG_local_lead_JPN', 'ASRG_local_lead_JPN'),
                    ('ASRG_OXF', 'ASRG_OXF'),
                    ('ASRG_local_lead_OXF', 'ASRG_local_lead_OXF'),
                    ('ASRG_SYD', 'ASRG_SYD'),
                    ('ASRG_local_lead_SYD', 'ASRG_local_lead_SYD'),
                    ('ASRG_IASI', 'ASRG_IASI'),
                    ('ASRG_local_lead_IASI', 'ASRG_local_lead_IASI'),
                    ('ASRG_DNCR', 'ASRG_DNCR'),
                    ('ASRG_local_lead_DNCR', 'ASRG_local_lead_DNCR'),
                    ('ASRG_DAY', 'ASRG_DAY'),
                    ('ASRG_local_lead_DAY', 'ASRG_local_lead_DAY'),
                    ('ASRG_REC', 'ASRG_REC'),
                    ('ASRG_local_lead_REC', 'ASRG_local_lead_REC'),
                    ('ASRG_BLR', 'ASRG_BLR'),
                    ('ASRG_local_lead_BLR', 'ASRG_local_lead_BLR'),
                    ('ASRG_LAX', 'ASRG_LAX'),
                    ('ASRG_local_lead_LAX', 'ASRG_local_lead_LAX'),
                    ('ASRG_BUC', 'ASRG_BUC'),
                    ('ASRG_local_lead_BUC', 'ASRG_local_lead_BUC'),
                    ('ASRG_QRO', 'ASRG_QRO'),
                    ('ASRG_local_lead_QRO', 'ASRG_local_lead_QRO'),
                    ('ASRG_CGN', 'ASRG_CGN'),
                    ('ASRG_local_lead_CGN', 'ASRG_local_lead_CGN'),
                    ('ASRG_TOR', 'ASRG_TOR'),
                    ('ASRG_local_lead_TOR', 'ASRG_local_lead_TOR'),
                    ('ASRG_WIN', 'ASRG_WIN'),
                    ('ASRG_local_lead_WIN', 'ASRG_local_lead_WIN'),
                    ('ASRG_KER', 'ASRG_KER'),
                    ('ASRG_local_lead_KER', 'ASRG_local_lead_KER'),
                    ('ASRG_VIE', 'ASRG_VIE'),
                    ('ASRG_local_lead_VIE', 'ASRG_local_lead_VIE'),
                    ('ASRG_HYD', 'ASRG_HYD'),
                    ('ASRG_local_lead_HYD', 'ASRG_local_lead_HYD'),
                ],
            },
        ),
        migrations.RunPython(add_existing_data),
    ]
