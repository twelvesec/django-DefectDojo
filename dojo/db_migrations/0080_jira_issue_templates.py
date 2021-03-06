# Generated by Django 2.2.17 on 2021-02-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0079_system_settings_disclaimer'),
    ]

    operations = [
        migrations.AddField(
            model_name='jira_instance',
            name='issue_template',
            field=models.CharField(blank=True, help_text='Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jira_project',
            name='issue_template',
            field=models.CharField(blank=True, help_text='Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.', max_length=255, null=True),
        ),
    ]
