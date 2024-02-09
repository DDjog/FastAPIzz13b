from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_alter_quote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
