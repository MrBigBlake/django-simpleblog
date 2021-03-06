# Generated by Django 2.0.7 on 2020-03-14 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('order', models.IntegerField(default=0, verbose_name='排序顺序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('cover', models.ImageField(default='cover/default.png', upload_to='cover/', verbose_name='文章封面')),
                ('about', models.CharField(max_length=128, verbose_name='文章简介')),
                ('content', mdeditor.fields.MDTextField(verbose_name='文章内容')),
                ('view_count', models.IntegerField(blank=True, default=0, verbose_name='阅读数量')),
                ('like_count', models.IntegerField(blank=True, default=0, verbose_name='点赞数量')),
                ('comment_count', models.IntegerField(blank=True, default=0, verbose_name='评论数量')),
                ('author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='文章作者')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'myblog_article',
            },
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('order', models.IntegerField(default=0, verbose_name='排序顺序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('article', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '文章与标签关系表',
                'verbose_name_plural': '文章与标签关系表',
                'db_table': 'myblog_article2tag',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('order', models.IntegerField(default=0, verbose_name='排序顺序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '分类表',
                'verbose_name_plural': '分类表',
                'db_table': 'myblog_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('order', models.IntegerField(default=0, verbose_name='排序顺序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('belong', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='所属文章')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='article.Comment', verbose_name='父评论')),
                ('reply_to', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relied_by', to='article.Comment', verbose_name='回复')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'myblog_comment',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否上线')),
                ('order', models.IntegerField(default=0, verbose_name='排序顺序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签表',
                'verbose_name_plural': '标签表',
                'db_table': 'myblog_tag',
            },
        ),
        migrations.AddField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='article.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='article.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', through='article.Article2Tag', to='article.Tag', verbose_name='文章标签'),
        ),
    ]
