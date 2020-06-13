# Generated by Django 3.0.3 on 2020-06-13 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pizza_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(null=True, upload_to=pizza_page.models.save_img)),
                ('toppings_no', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NP', 'Not Placed'), ('PL', 'Placed'), ('IN', 'In Progress'), ('CO', 'Completed')], max_length=2)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('M', 'Medium'), ('S', 'Small'), ('L', 'Large')], max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_food_id', to='pizza_page.Food')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_food_id', to='pizza_page.Food')),
                ('food_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_price_id', to='pizza_page.Price')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='pizza_page.Order')),
            ],
        ),
    ]
