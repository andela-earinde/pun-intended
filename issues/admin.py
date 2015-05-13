from django import forms
from issues.models import Users
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _

# Register your models here.
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('username', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1") 
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False) 
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save() 
            return user

class MyUserAdmin(UserAdmin):
    # The fields to be used in displaying the User model. 
    # These override the definitions on the base UserAdmin 
    # that reference specific fields on auth.User.
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ('username',)}),
             (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user. 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ), 
    )
    list_display = ('username', 'is_staff')
    search_fields = ('username',) 
    ordering = ('username',) 
    filter_horizontal = ()


admin.site.register(Users, MyUserAdmin)
