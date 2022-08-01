from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='E-mail')
    message = forms.Textarea(label='Сообщение')
    #TODO 2:02:33 на видеоуроке