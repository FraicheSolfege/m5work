from django import forms 

class HeyNameForm(forms.Form):
    name = forms.CharField()

class HowOldForm(forms.Form):
    endyear = forms.IntegerField()
    birthyear = forms.IntegerField()
    
class OrderTotalForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()

class CB1FORM(forms.Form):
    num = forms.IntegerField()

class CB2FORM(forms.Form):
    word = forms.CharField()

class CB3FORM(forms.Form):
    is_catdog = forms.CharField()

class CB4FORM(forms.Form):
    int1 = forms.IntegerField()
    int2 = forms.IntegerField()
    int3 = forms.IntegerField()






