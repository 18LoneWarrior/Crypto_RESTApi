# Generated by Django 5.0.3 on 2024-03-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_data', '0002_blockchain_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='blockchain',
            field=models.CharField(choices=[('BITCOIN', 'Bitcoin'), ('ETHEREUM', 'Ethereum'), ('SOLANA', 'Solana'), ('BSC', 'BNB'), ('MANTA', 'Manta'), ('POLYGON', 'Polygon'), ('ARBITRUM', 'Arbitrum'), ('AVALANCHE', 'Avalanche'), ('FANTOM', 'Fantom'), ('HECO', 'Heco'), ('OKEX', 'OKEx')], default='ETHEREUM', max_length=10),
        ),
    ]
