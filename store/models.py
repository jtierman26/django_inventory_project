#parts of this code were obtained and modified to the programs needs from 
#[1]“Build an Inventory Management System with Python and Django - Overview,” 
#www.youtube.com. https://www.youtube.com/watch?v=axGWgK2ep4Q&list=PLWwo7xJYACuQ2tVSIzAarcUvNlR3oTk-w&index=1 (accessed Mar. 30, 2024). 

from django.db import models
from django.contrib.auth.models import User


#Item class 

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_amount = models.PositiveBigIntegerField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    original_amount = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.item_name 

#Item Issue class definition

class ItemIssue(models.Model):
    #setting types of departments
    department_choices = (
        ('Clothing','Clothing'),
        ('Food','Food'),
        ('Home','Home'),
        ('Outdoors','Outdoors'),
        ('Pet','Pet'),
        ('Security','Security'),
        ('Sports','Sports'),
        ('Tech','Tech'),
        ('Arts n Crafts','Arts n Crafts')
    )

    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    amount = models.PositiveBigIntegerField()
    issued_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #can i make it so the form has a drop down to choose from users
    issued_to = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices= department_choices)
    date_issued = models.DateTimeField(auto_now_add = True)
    date_return = models.DateField()
    #is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} - {self.issued_to}'
    

# Returned Item class 

class ItemReturned(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_returned = models.DateField(auto_now_add=True)
    amount_returned = models.PositiveIntegerField()
    #all_items_returned = models.BooleanField(default = False)
    returner = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.item} - {self.returner}'


# Restock Item Class 
    
class RestockItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField()
    timestamp = models.DateField(auto_now_add=True)
    original_value = models.PositiveBigIntegerField(null=True, blank=True)

