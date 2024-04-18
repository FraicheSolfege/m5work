from django import forms 

class HeyNameForm(forms.Form):
    name = forms.CharField()

class HowOldForm(forms.Form):
    endyear = forms.IntegerField()
    birthyear = forms.IntegerField()
    
class OrderTotalForm(forms.Form):
    Burgers = forms.IntegerField()
    fries = forms.IntegerField()
    fries = forms.IntegerField()