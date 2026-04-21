from django import forms
from .models import Student, Graduate


HS_YEAR_CHOICES = [(y, y) for y in range(2050, 2014, -1)]
GRAD_YEAR_CHOICES = [(y, y) for y in range(2050, 2009, -1)]

GRADE_CHOICES = [
    (1, "1年"),
    (2, "2年"),
    (3, "3年"),
    (4, "4年"),
    (5, "5年"),
    (6, "6年"),
]

DEPARTMENT_CHOICES = [
    ("", "選択してください"),
    ("総合診療科", "総合診療科"),
    ("消化器内科", "消化器内科"),
    ("循環器内科", "循環器内科"),
    ("呼吸器内科", "呼吸器内科"),
    ("整形外科", "整形外科"),
    ("小児科", "小児科"),
    ("産婦人科", "産婦人科"),
    ("眼科", "眼科"),
    ("精神科", "精神科"),
    ("その他", "その他"),
]


# -------------------
# 学生
# -------------------
class StudentForm(forms.ModelForm):

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    high_school_graduation_year = forms.TypedChoiceField(
        choices=HS_YEAR_CHOICES,
        coerce=int
    )

    grade = forms.TypedChoiceField(
        choices=GRADE_CHOICES,
        coerce=int
    )

    desired_department = forms.CharField(required=False)
    desired_department_other = forms.CharField(required=False)

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：岩手太郎'
            }),
            'furigana': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：いわてたろう'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'grade': forms.Select(attrs={'class': 'form-select'}),
            'hometown': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：盛岡市'
            }),
            'high_school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：盛岡第一高校'
            }),
            'high_school_graduation_year': forms.Select(attrs={'class': 'form-select'}),
            'hobby': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '例：テニス・筋トレ'
            }),
            'desired_department': forms.TextInput(attrs={'class': 'form-control'}),
            'desired_department_other': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'その他入力'
            }),
        }


# -------------------
# 卒業生
# -------------------
class GraduateForm(forms.ModelForm):

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    graduation_year = forms.TypedChoiceField(
        choices=GRAD_YEAR_CHOICES,
        coerce=int
    )

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, required=False)
    department_other = forms.CharField(required=False)

    class Meta:
        model = Graduate
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：岩手太郎'
            }),
            'furigana': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：いわてたろう'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'high_school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：盛岡第一高校'
            }),
            'university': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：東北大学'
            }),
            'graduation_year': forms.Select(attrs={'class': 'form-select'}),
            'hospital': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例：岩手医科大学附属病院'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '任意（例：example@gmail.com）'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '任意（例：09012345678）'
            }),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'department_other': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'その他の場合入力'
            }),
        }