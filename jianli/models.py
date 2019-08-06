# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Books(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    post_title = models.CharField(max_length=255, blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    post_comm = models.CharField(max_length=255, blank=True, null=True)
    post_img = models.CharField(max_length=255)
    post_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Stopwords(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    words = models.CharField(db_column='Words', max_length=50, blank=True, null=True)  # Field name made lowercase.
    words_type = models.IntegerField(db_column='Words_Type')  # Field name made lowercase.
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stopwords'


class Tasklist(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    task_name = models.CharField(db_column='Task_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    task_url_from = models.CharField(db_column='Task_URL_from', max_length=500, blank=True, null=True)  # Field name made lowercase.
    task_language = models.IntegerField(db_column='Task_Language', blank=True, null=True)  # Field name made lowercase.
    task_infotype = models.IntegerField(db_column='Task_InfoType', blank=True, null=True)  # Field name made lowercase.
    task_pagetype = models.IntegerField(db_column='Task_PageType', blank=True, null=True)  # Field name made lowercase.
    task_iscrawlall = models.IntegerField(db_column='Task_isCrawlAll', blank=True, null=True)  # Field name made lowercase.
    task_isproxy = models.IntegerField(db_column='Task_isProxy', blank=True, null=True)  # Field name made lowercase.
    task_bingfa = models.IntegerField(db_column='Task_bingfa', blank=True, null=True)  # Field name made lowercase.
    task_jiange = models.IntegerField(db_column='Task_Jiange', blank=True, null=True)  # Field name made lowercase.
    task_crawltype = models.IntegerField(db_column='Task_CrawlType', blank=True, null=True)  # Field name made lowercase.
    task_level = models.IntegerField(db_column='Task_Level', blank=True, null=True)  # Field name made lowercase.
    task_deep = models.IntegerField(db_column='Task_Deep', blank=True, null=True)  # Field name made lowercase.
    task_db_type = models.CharField(db_column='Task_DB_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_db_host = models.CharField(db_column='Task_DB_Host', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_db_name = models.CharField(db_column='Task_DB_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_db_uid = models.CharField(db_column='Task_DB_UID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_db_pwd = models.CharField(db_column='Task_DB_Pwd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_rule_domain_included = models.CharField(db_column='Task_Rule_Domain_Included', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_domain_excluded = models.CharField(db_column='Task_Rule_Domain_Excluded', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_dir_included = models.CharField(db_column='Task_Rule_DIR_Included', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_dir_excluded = models.CharField(db_column='Task_Rule_DIR_Excluded', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_file_included = models.CharField(db_column='Task_Rule_file_Included', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_file_excluded = models.CharField(db_column='Task_Rule_file_Excluded', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_replace = models.CharField(db_column='Task_Rule_Replace', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_cut = models.CharField(db_column='Task_Rule_Cut', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_rule_filter = models.CharField(db_column='Task_Rule_filter', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    task_stat = models.IntegerField(db_column='Task_stat', blank=True, null=True)  # Field name made lowercase.
    task_time_post = models.DateTimeField(db_column='Task_Time_post')  # Field name made lowercase.
    task_time_start = models.DateTimeField(db_column='Task_Time_start')  # Field name made lowercase.
    task_time_end = models.DateTimeField(db_column='Task_Time_end')  # Field name made lowercase.
    task_isxpath = models.IntegerField(db_column='Task_isXpath', blank=True, null=True)  # Field name made lowercase.
    task_xpath_content = models.CharField(db_column='Task_Xpath_Content', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_xpath_breadcrumbs = models.CharField(db_column='Task_Xpath_Breadcrumbs', max_length=300, blank=True, null=True)  # Field name made lowercase.
    task_xpath_answers = models.CharField(db_column='Task_Xpath_Answers', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tasklist'


class Visitor(models.Model):
    visitor_name = models.CharField(max_length=255, blank=True, null=True)
    visitor_email = models.CharField(max_length=255, blank=True, null=True)
    visitor_text = models.CharField(max_length=255, blank=True, null=True)
    visitor_context = models.CharField(max_length=255, blank=True, null=True)
    visitor_tel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitor'
