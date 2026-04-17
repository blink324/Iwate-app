from django.db import models

# 学年
GRADE_CHOICES = [
    (1, '1年'),
    (2, '2年'),
    (3, '3年'),
    (4, '4年'),
    (5, '5年'),
    (6, '6年'),
]

# 市町村
CITY_CHOICES = [
    ('盛岡市', '盛岡市'),
    ('花巻市', '花巻市'),
    ('北上市', '北上市'),
    ('奥州市', '奥州市'),
    ('一関市', '一関市'),
    ('宮古市', '宮古市'),
    ('釜石市', '釜石市'),
    ('久慈市', '久慈市'),
    ('二戸市', '二戸市'),
    ('その他', 'その他'),
]


class Graduate(models.Model):
    name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    birth_date = models.DateField()

    department = models.CharField(max_length=100, blank=True, null=True)

    high_school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)

    # 👇これ追加
    graduation_university = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    graduation_year = models.IntegerField()
    hospital = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    grade = models.IntegerField(choices=GRADE_CHOICES)
    birth_date = models.DateField()

    hometown = models.CharField(max_length=100, blank=True, null=True)

    high_school = models.CharField(max_length=100)
    high_school_graduation_year = models.IntegerField()
    hobby = models.TextField()

    # 👇 これはそのままでOK
    desired_department = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

# Create your models here.
