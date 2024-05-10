from django import forms
from .models import Customer, Driver, BookRide

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Password'}), label=None)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Confirm Password'}), label=None)

    class Meta:
        model = Customer
        fields = ('username', 'email', 'mobile', 'password', 'confirm_password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'pattern': '[0-9]+', 'placeholder': 'Mobile Number'}),
        }

        labels = {
            'username': None,
            'email': None,
            'mobile': None,
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("The mobile number must contain only digits.")
        return mobile

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = False  # Set is_staff to False for normal users
        user.is_superuser = False  # Set is_superuser to False for normal users
        if commit:
            user.save()
        return user



class DriverSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Password'}), label=None)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Confirm Password'}), label=None)

    class Meta:
        model = Driver
        fields = ('username', 'email', 'mobile', 'driving_license', 'vehicle_number', 'password', 'confirm_password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'pattern': '[0-9]+', 'placeholder': 'Mobile Number'}),
            'driving_license': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Driving License'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Vehicle Number'}),
        }

        labels = {
            'username': None,
            'email': None,
            'mobile': None,
            'driving_license': None,
            'vehicle_number': None
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("The mobile number must contain only digits.")
        return mobile

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

    def save(self, commit=True):
        user = super(DriverSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = False  # Set is_staff to False for normal users
        user.is_superuser = False  # Set is_superuser to False for normal users
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Password'}))


class BookrideForm(forms.ModelForm):
    class Meta:
        model = BookRide
        fields = ['source', 'destination', 'ride_status']


        widgets = {
            'source': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Source'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Destination'}),
            'ride_status': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),  # Readonly status field

        }

        labels = {
            'source': None,
            'destination': None,
            'ride_status': None,
        }

