# parts of this code were obtained and modified to the programs needs from 
#[1]“Build an Inventory Management System with Python and Django - Overview,” 
#www.youtube.com. https://www.youtube.com/watch?v=axGWgK2ep4Q&list=PLWwo7xJYACuQ2tVSIzAarcUvNlR3oTk-w&index=1 (accessed Mar. 30, 2024).  

from django.shortcuts import render, redirect
from django.contrib import messages
from .form import AddItem_form, UpdateItem_form, ItemIssue_form, ItemReturned_form, RestockItem_form
from .models import Item, ItemIssue, ItemReturned, RestockItem


#dashboard graph (doesnt work)
#def stockchart(request):
   # stockdata = \
        #DataPool(
            #series=
                #[{'options': {
                    #'source': Item.objects.all()},
                #'terms':[
                   # 'item_name',
                  #  'item_amount']}
              #  ])
    
   # mychart = Chart(
        #    datasource = stockdata,
        #    series_options =
        #      [{'options':{
       #           'type': 'bar',
          #        'stacking': False},
          #      'terms':{
         #         'Item': [
          #            'item_amount',
         #         ]
         #         }}],
        #    chart_options = 
        #        {'title': {
        #            'text': 'Inventory Data'},
          #          'xAxis' : {
           #             'title': {
          #                  'text': 'Amount'}}})
  #  return render({'stockchart': mychart})

#add item defintions 
def add_item(request):
    if request.method == 'POST':
        form = AddItem_form(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.creator = request.user
            add.original_amount = add.item_amount
            add.save()
            messages.info(request, 'New item has been added succesfully!!')
            return redirect('all-items')
        else:
            messages.warning(request, 'Uh Oh... Something went wrong')
            return redirect('add-item')
    else:
        form = AddItem_form()
        context = {'form':form}
        return render(request, 'store/add_item.html', context)
    

#Update item definition
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateItem_form(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item has succesfully been updated!')
            return redirect('all-items')
        else:
            messages.warning(request, 'Uh Oh... Something went wrong')
            
    else:
        form = UpdateItem_form(instance=item)
        context = {'form':form}
        return render(request, 'store/update_item.html', context)
    

#definition to define all items
def all_Items(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'store/all_items.html', context)


#delete the Item
def delete_Item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Item has been successfully deleted')
    return redirect(request, 'store/delete_item.html')


#item issue
def issue_item(request):
    if request.method == "POST":
        form= ItemIssue_form(request.POST)
        if form.is_valid():
            issue = form.save(commit = False)
            issue.issued_by = request.user

            getItem = Item.objects.get(pk=issue.item.pk)
            if getItem.item_amount != 0 or getItem.item_amount > issue.amount:
                if getItem.item_amount > issue.amount:
                    getItem.item_amount = getItem.item_amount - issue.amount
                    getItem.save()
                    issue.save()
                    messages.info(request, f'The item has been issued to {issue.issued_to}')
                    return redirect('all-items')
                else:
                    messages.warning(request, f'Item is low on stock! There is only: {getItem.item_amount} left')
                    return redirect('all-items')
            else:
                messages.warning(request, 'Item is not in stock')
                return redirect('all-items')
        else:
            messages.warning(request, 'Uh oh...something went wrong!')
            return redirect('issue-item')
    else:
        form = ItemIssue_form()
        context = {'form':form}
        return render(request, 'store/issue_item.html', context)
    

#item history 
def issue_history(request):
    items = ItemIssue.objects.all().order_by('issued_by')
    context = {'items':items}
    return render(request, 'store/issue_history.html', context)


#item return
def return_item(request):
    if request.method == "POST":
        form = ItemReturned_form(request.POST)
        if form.is_valid():
            returned = form.save(commit =False)
            getItem = Item.objects.get(pk= returned.item.pk)
            getItem.item_amount = getItem.item_amount + returned.amount_returned
            if getItem.item_amount > getItem.original_amount:
                messages.warning(request, f'Items returend does not match original amount: ({getItem.original_amount})')
                return redirect('all-items')
            else:
                getItem.save()
                returned.save()
                messages.info(request, 'The Item has been returned back to the store')
                return redirect('all-items')
        else:
            messages.warning(request, 'Uh Oh... Something went wrong!')
            return redirect('return-item')
    else:
        form = ItemReturned_form()
        context = {'form':form}
        return render(request, 'store/return_item.html', context)
    

#return history 
def return_history(request):
    items = ItemReturned.objects.all()
    context = {'items':items}
    return render(request, 'store/return_history.html', context)


#Restock item
def restockItem(request):
    if request.method == 'POST':
        form = RestockItem_form(request.POST)
        if form.is_valid():
            restock = form.save(commit=False) 
            getItem = Item.objects.get(pk=restock.item.pk)
            restock.original_value = getItem.original_amount
            getItem.original_amount = getItem.original_amount + restock.amount
            getItem.save()
            restock.save()
            messages.info(request, f'{getItem.item_name} has been restocked!')
            return redirect('all-items')
        else:
            messages.warning(request, 'Uh Oh... Something went wrong!')
            return redirect('restock-item')
    else:
        form = RestockItem_form()
        context = {'form':form}
        return render(request, 'store/restock_item.html', context)
    

#Restock History 
def restock_history(request):
    items = RestockItem.objects.all()
    context = {'items':items}
    return render(request, 'store/restock_history.html', context)

