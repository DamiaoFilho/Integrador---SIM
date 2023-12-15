from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from crispy_forms.layout import Column, Layout, Row, Fieldset
from django import forms
User = get_user_model()


from django import forms
from .models import Student, Professor
from .models import User as UserModel
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm

class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["user", "is_colleger"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]

class StudentUserForm(MultiModelForm):
    form_classes = {
        "student": StudentForm,
        "user": SignupForm
    }

        
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["register", "user", "is_colleger"]

class StudentMultiUpdateForm(MultiModelForm):
    form_classes = {
        "student": StudentUpdateForm,
        "user": UserForm,
    }

    layout = Layout(
        Fieldset(
            Row("user-email", css_class="col"),
            Row(
                Column("student-photo", css_class="col")
            ),
            Row(
                Column("student-phone", css_class="col"),
            ),
            Row(
                Column("student-course", css_class="col"),
            ),
            Row(
                Column("student-year", css_class="col-md-4"),
                Column("student-shift", css_class="col-md-4"),
            ),
        ),
    )

class ProfessorUpdateForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ["user"]


     