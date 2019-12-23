from django import forms
from user.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import login, authenticate

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'active', 'admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    is_tutor = forms.BooleanField(label='Are you a tutor?', widget=forms.CheckboxInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'is_tutor')

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # def clean(self):
    #     data = self.cleaned_data
    #     username = data.get('username')
    #     password1 = data.get('password1')
    #     password2 = data.get('password2')

    #     user = User.objects.filter(username=username)

    #     if user.exists():
    #         raise forms.ValidationError("User with name '{}' already exists.".format(username))

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False # send confirmation mail
        if commit:
            user.active = True
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            user = authenticate(username=username, password=password)

            if user == None:
                raise forms.ValidationError('Invalid Password')
        else:
            raise forms.ValidationError('Username {} does not exist'.format(username))

class EditForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(EditForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False # send confirmation mail
        if commit:
            user.active = True
            user.save()
        return user