# Generated by Django 3.2.8 on 2021-10-16 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Description', models.TextField()),
                ('MCA', models.CharField(max_length=50, verbose_name='MCA ID')),
                ('Type', models.CharField(max_length=70, verbose_name='Company Type')),
                ('revenue', models.BigIntegerField(verbose_name='Latest 1 year Revenue')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minCTC', models.SmallIntegerField(verbose_name='Minimum CTC in Lakhs')),
                ('maxCTC', models.SmallIntegerField(verbose_name='Maximum CTC in Lakhs')),
                ('Description', models.TextField(verbose_name='Roles and Responsibility')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(verbose_name='Extra Info About offer')),
                ('FinalCTC', models.SmallIntegerField()),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='MessageP2C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeStamps', models.DateTimeField()),
                ('Body', models.TextField()),
                ('receivers', models.ManyToManyField(to='api.Company')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.placementcell')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessageC2P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeStamps', models.DateTimeField()),
                ('Body', models.TextField()),
                ('receivers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.placementcell')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=20)),
                ('ExamDateTime', models.DateTimeField(verbose_name='Next Round Exam Start Time')),
                ('Description', models.TextField(verbose_name='Info About Next Roumd')),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='AppliedPositions',
            field=models.ManyToManyField(through='api.Applied', to='api.Position'),
        ),
    ]
