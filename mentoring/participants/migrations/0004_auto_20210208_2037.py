# Generated by Django 3.1.2 on 2021-02-08 20:37

from django.db import migrations, models
from textwrap import dedent

from mentoring.participants.models import current_expiration


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0003_auto_20210125_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='expires',
            field=models.DateTimeField(
                default=current_expiration, help_text=dedent('''\
                    The date that this information expires.  This can be extended (such as when
                    a pairing is made), and expiration is contingent on not being in a current
                    pair.  This field accomplishes the "lean data" practice of not keeping
                    user information forever. ''')),
        ),
    ]
