# Generated by Django 4.1.5 on 2024-01-01 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_categoria_disponibilidad_estado_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to='post.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to='post.usuario')),
            ],
        ),
    ]