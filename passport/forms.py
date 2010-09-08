'''
Created on Sep 8, 2010

@author: scollins
'''

from django import forms

class DrexelIDForm(forms.Form):
    drexel_id = forms.CharField(max_length=25)
    drexel_username = forms.CharField(max_length=25) 