from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput, Textarea, DateInput, TimeInput, DateTimeInput
#
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваше імя',
            }),
             "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваш email'
            }),
              "date": DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'День та час коли Вам зателефонувати'
              
            })
            #  "phone": NumberInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введіть ваш телефон'
            # }),
            #  "subject": Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введіть ваше повідомлення',
                
            # }),
           
            # "time": TimeInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'Час коли вам зателефонувати'
            # })
        }