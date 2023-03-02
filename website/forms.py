from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput
from .models import Testimonial

# Your forms here
class TestimonialForm(forms.ModelForm):
    # Meta data
    class Meta:
        model  = Testimonial
        
        fields = [
            'quote',
            'name',
            'role',
            'twitter',
            'website',
        ]

        # Definition of widgets
        widgets = {
            'quote': Textarea(
                attrs={
                    'name': 'quote',
                    'class': 'form-control',
                    'id': 'quote',
                    'rows': 3,
                    'placeholder': 'let it go your way ...',
                    'aria-describedby': 'helpId'
                }
            ),
            
            'name': TextInput(
                attrs={
                    'name': 'name',
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Edghi Makolle',
                    'aria-describedby': 'helpId'
                }
            ),

            'role': TextInput(
                attrs={
                    'name': 'role',
                    'class': 'form-control',
                    'id': 'role',
                    'placeholder': 'Backend',
                    'aria-describedby': 'helpId'
                }
            ),
            
            'twitter': URLInput(
                attrs={
                    'name': 'twitter',
                    'class': 'form-control',
                    'id': 'twitter',
                    'placeholder': 'https://twitter.com/me',
                    'aria-describedby': 'helpId'
                }
            ),
            
            'website': URLInput(
                attrs={
                    'name': 'website',
                    'class': 'form-control',
                    'id': 'website',
                    'placeholder': 'me.com',
                    'aria-describedby': 'helpId'
                }
            ),
        }
