from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема', widget=forms.TextInput(attrs={'humanReadable': 'Тема', 'class':'form-control'}))
    sender = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'humanReadable': 'E-mail', 'class':'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'humanReadable': 'Сообщение', 'class':'form-control'}))
    copy = forms.BooleanField(label='Отправить копию себе', required=False)
