# Generated by Django 3.2.6 on 2021-08-18 17:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_doctor', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='doctor status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'AdminHOD'), (2, 'Pharmacist'), (3, 'Doctor'), (4, 'PharmacyClerk'), (5, 'Patients')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='admin.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_employed', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='patient.jpg', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, default='0', null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('date_admitted', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_imprint', models.CharField(blank=True, max_length=6, null=True)),
                ('drug_name', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_color', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_shape', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('manufacture', models.CharField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('drug_strength', models.CharField(blank=True, max_length=10, null=True)),
                ('valid_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('valid_to', models.DateTimeField(null=True)),
                ('drug_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('drug_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.category')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('prescribe', models.CharField(max_length=100, null=True)),
                ('date_precribed', models.DateTimeField(auto_now_add=True)),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.patients')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyClerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='')),
                ('age', models.IntegerField(blank=True, default='0', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, default='0', null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='images2.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField(null=True)),
                ('feedback_reply', models.TextField(null=True)),
                ('admin_created_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.adminhod')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.patients')),
                ('pharmacist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacist')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, default='0', null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='doctor.png', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dispense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispense_quantity', models.PositiveIntegerField(default='1', null=True)),
                ('taken', models.CharField(blank=True, max_length=300, null=True)),
                ('stock_ref_no', models.CharField(blank=True, max_length=300, null=True)),
                ('instructions', models.TextField(max_length=300, null=True)),
                ('dispense_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('drug_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.stock')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharmacy.patients')),
            ],
        ),
    ]
