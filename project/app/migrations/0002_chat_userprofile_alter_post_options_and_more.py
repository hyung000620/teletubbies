# Generated by Django 4.2.5 on 2023-09-25 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, null=True)),
                ('region_certification', models.CharField(default='N', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_dt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='작성일자'),
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default=2, upload_to='post_images/', verbose_name='이미지'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='product_reserved',
            field=models.CharField(default='N', max_length=1, verbose_name='예약여부'),
        ),
        migrations.AddField(
            model_name='post',
            name='product_sold',
            field=models.CharField(default='N', max_length=1, verbose_name='판매여부'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='post',
            name='chat_num',
            field=models.PositiveIntegerField(default=0, verbose_name='채팅수'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_num',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]