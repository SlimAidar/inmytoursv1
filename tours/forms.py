from django import forms

class BookForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'First name'
                    }), label = '')
    last_name = forms.CharField(max_length=100, required=True,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Last name'
                    }), label = '')
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
                        'placeholder': 'Email'    
                    }), label = '')
    phone = forms.CharField(required=True, widget=forms.TextInput(
                            attrs={
                                'placeholder': 'Phone'
                            }
                        ), label =  '')
    message = forms.CharField(required=False, widget=forms.TextInput(
                            attrs={
                                'placeholder': 'Your message'
                            }
                        ), label =  '')