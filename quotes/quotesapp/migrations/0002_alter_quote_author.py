import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotesapp.author'),
        ),
    ]
