from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Region


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    birth = forms.CharField(
        label='생일',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    phone = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )

    city = forms.ChoiceField(
        label='시/도',
        choices=[('', '선택해주세요')] + [(city, city) for city in Region.objects.values_list(
            'city', flat=True).distinct()],
        widget=forms.Select(
            attrs={'class': 'signup-input'})
    )
    town = forms.ChoiceField(
        label='군/구',
        choices=[('', '------')] + [(town, town) for town in Region.objects.values_list('town', flat=True).distinct()],
        widget=forms.Select(attrs={'class': 'signup-input'})
    )

    address = forms.CharField(
        label='상세 주소',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'nickname', 'password1',
                  'password2', 'birth', 'phone', 'address']

    def save(self, commit=True):
        city = self.cleaned_data['city']
        town = self.cleaned_data['town']
        region, created = Region.objects.get_or_create(city=city, town=town)

        # 사용자가 선택한 region을 저장
        self.instance.region = region

        return super().save(commit)


class UpdateForm(forms.ModelForm):
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    birth = forms.CharField(
        label='생일',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    phone = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )
    city = forms.ChoiceField(
        label='시/도',
        choices=[('', '선택해주세요')] + [(city, city) for city in Region.objects.values_list(
            'city', flat=True).distinct()],
        widget=forms.Select(
            attrs={'class': 'signup-input'})
    )
    town = forms.ChoiceField(
        label='군/구',
        choices=[('', '------')] + [(town, town)
                                    for town in Region.objects.values_list('town', flat=True).distinct()],
        widget=forms.Select(attrs={'class': 'signup-input'})
    )

    address = forms.CharField(
        label='상세 주소',
        widget=forms.TextInput(
            attrs={
                'class': 'signup-input'
            }
        )
    )

    class Meta:
        model = User
        fields = ["nickname", "birth", "phone", "address"]

    def save(self, commit=True):
        city = self.cleaned_data['city']
        town = self.cleaned_data['town']
        region, created = Region.objects.get_or_create(city=city, town=town)

        # 사용자가 선택한 region을 저장
        self.instance.region = region

        return super().save(commit)
