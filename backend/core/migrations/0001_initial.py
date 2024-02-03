# Generated by Django 5.0.1 on 2024-01-19 13:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Узбекистан', max_length=255, verbose_name='Страна')),
                ('city', models.CharField(default='Ташкент', max_length=255, verbose_name='Город')),
                ('district', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Район')),
                ('street', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Дом')),
                ('flat', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Квартира')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Индекс')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message='Invalid phone number')], verbose_name='Номер телефона')),
                ('websiteUrl', models.URLField(blank=True, null=True, verbose_name='ссылка на сайт')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='organizations/logos/', verbose_name='Логотип компании')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.address', verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('Файлы PDF', 'pdf'), ('Таблицы экзель', 'excel'), ('Документы', 'word'), ('Схемы', 'visio'), ('Презентации', 'pptx')], max_length=30, verbose_name='Тип документа')),
                ('title', models.CharField(max_length=255, verbose_name='Название документа')),
                ('file', models.FileField(upload_to='media/documents/', verbose_name='Файл документа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.CreateModel(
            name='DeviceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория устройства',
                'verbose_name_plural': 'Категории устройств',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
            },
        ),
        migrations.CreateModel(
            name='OwnershipForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortForm', models.CharField(max_length=255, verbose_name='короткая форма')),
                ('longForm', models.CharField(max_length=255, verbose_name='длинная форма')),
            ],
            options={
                'verbose_name': 'Форма принадлежности',
                'verbose_name_plural': 'Формы принадлежности',
            },
        ),
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название этапа')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('number', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Номер этапа')),
                ('completed', models.BooleanField(default=False, verbose_name='Завершено')),
            ],
            options={
                'verbose_name': 'Этап проекта',
                'verbose_name_plural': 'Этапы проекта',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('legalentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.legalentity')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
            bases=('core.legalentity',),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.details', verbose_name='Реквизиты'),
        ),
        migrations.CreateModel(
            name='DetailField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.details', verbose_name='Реквизиты')),
            ],
            options={
                'verbose_name': 'Поле реквизита',
                'verbose_name_plural': 'Поля реквизитов',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('part_number', models.CharField(max_length=50, verbose_name='Парт номер')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('purpose', models.CharField(max_length=255, verbose_name='Назначение')),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Производитель')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.devicecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('job_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Рабочий E-mail')),
                ('jobTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
            bases=('core.person',),
        ),
        migrations.AddField(
            model_name='legalentity',
            name='ownershipForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ownershipform', verbose_name='Форма принадлежности'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.legalentity', verbose_name='Заказчик')),
                ('specification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.specification', verbose_name='Спецификация')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='TenderStage',
            fields=[
                ('projectstage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.projectstage')),
                ('link', models.URLField(blank=True, null=True, verbose_name='ссылка на лот')),
                ('lot', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендера',
            },
            bases=('core.projectstage',),
        ),
        migrations.AddField(
            model_name='projectstage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstages', to='core.project', verbose_name='Проект'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.device', verbose_name='Оборудование')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specification', verbose_name='Спецификация')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
            },
        ),
        migrations.CreateModel(
            name='Vendordoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('file', models.FileField(upload_to='media/vendordocs/', verbose_name='Файлы вендоров')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specification', verbose_name='Спецификация')),
            ],
            options={
                'verbose_name': 'Файл вендора',
                'verbose_name_plural': 'Файлы вендоров',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('legalentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.legalentity')),
                ('serviceBank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.bank', verbose_name='Обслуживающий банк')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
            bases=('core.legalentity',),
        ),
        migrations.CreateModel(
            name='CorporateDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.document')),
                ('legal_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corporate_documents', to='core.legalentity', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Корпоративный документ',
                'verbose_name_plural': 'Корпоративные документы',
            },
            bases=('core.document',),
        ),
        migrations.CreateModel(
            name='PersonalDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.document')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person', verbose_name='Персона')),
            ],
            options={
                'verbose_name': 'Персональный документ',
                'verbose_name_plural': 'Персональные документы',
            },
            bases=('core.document',),
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.document')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('approved', 'Утвержден'), ('obsolete', 'Устарел')], default='draft', max_length=10, verbose_name='Статус')),
                ('project_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_documents', to='core.projectstage', verbose_name='Этап проекта')),
            ],
            options={
                'verbose_name': 'Документ проекта',
                'verbose_name_plural': 'Документ проекта',
            },
            bases=('core.document',),
        ),
        migrations.CreateModel(
            name='EmployeeDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.document')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Документ сотрудника',
                'verbose_name_plural': 'Документы сотрудников',
            },
            bases=('core.document',),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.legalentity', verbose_name='Компания'),
        ),
    ]