from django import forms

class ContactUsForm(forms.Form):
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
    subject = forms.CharField(required=False, widget=forms.Textarea(
                            attrs={
                                'placeholder': 'Your message',
                                'class': 'materialize-textarea'
                            }
                        ), label =  '')