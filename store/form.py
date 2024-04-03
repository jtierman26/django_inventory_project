# parts of this code were obtained and modified to the programs needs from 
#[1]“Build an Inventory Management System with Python and Django - Overview,” 
#www.youtube.com. https://www.youtube.com/watch?v=axGWgK2ep4Q&list=PLWwo7xJYACuQ2tVSIzAarcUvNlR3oTk-w&index=1 (accessed Mar. 30, 2024).  

from django import forms 
from .models import Item, ItemIssue, RestockItem, ItemReturned



#Adding Item Class
class AddItem_form(forms.ModelForm):
    class Meta:
        model = Item
        fields =['item_name', 'item_amount']


#Update Item
class UpdateItem_form(forms.ModelForm):
    class Meta:
        model = Item
        fields =['item_name']


#Item Issue
class ItemIssue_form(forms.ModelForm):
    class Meta:
        model = ItemIssue
        fields = ['item', 'amount', 'issued_to', 'department', 'date_return']

#Return Item 
class ItemReturned_form(forms.ModelForm):
    class Meta:
        model = ItemReturned
        fields = ['item', 'amount_returned', 'returner']


#Restock Item
class RestockItem_form(forms.ModelForm):
    class Meta:
        model = RestockItem
        fields = ['item', 'amount']
