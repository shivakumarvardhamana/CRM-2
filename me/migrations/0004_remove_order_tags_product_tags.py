# Generated by Django 4.1.2 on 2022-10-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_tag_order_customer_order_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='me.tag'),
        ),
    ]
