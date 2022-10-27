# Generated by Django 3.2.13 on 2022-10-27 05:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('writer', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=20)),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('소설', '소설'), ('시, 수필, 에세이', '시, 수필, 에세이'), ('재테크', '재테크'), ('철학, 예술, 종교', '철학, 예술, 종교'), ('자기계발서', '자기계발서'), ('어학, 외국어', '어학, 외국어'), ('역사, 인문학', '역사, 인문학'), ('가정, 육아, 요리', '가정, 육아, 요리'), ('정치, 사회과학', '정치, 사회과학'), ('기타', '기타')], max_length=73)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]