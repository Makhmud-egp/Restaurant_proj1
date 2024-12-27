from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order, OrderItem
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def menu(request):
    # Menu korsatish
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'items': items})

@login_required
def create_order(request):
    if request.method == 'POST':
        table_number = request.POST['table_number']
        order = Order.objects.create(table_number=table_number)

        
        for item_id, quantity in request.POST.items():
            if item_id.startswith('item_'):  
                menu_item_id = int(item_id.split('_')[1])  
                try:
                    menu_item = MenuItem.objects.get(id=menu_item_id)
                    if int(quantity) > 0:  
                        OrderItem.objects.create(order=order, menu_item=menu_item, quantity=int(quantity))
                except MenuItem.DoesNotExist:
                    continue  

        return redirect('order_list')

    items = MenuItem.objects.all()
    return render(request, 'orders/create_order.html', {'items': items})

@login_required
def order_list(request):
    
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def generate_bill(request, pk):
    
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/bill.html', {'order': order})

def mark_as_paid(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.is_paid = True
    order.save()
    return redirect('menu')

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  
    else:
        form = AuthenticationForm()

    return render(request, 'orders/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  

@login_required
def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'items': items})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    total = order.total_price()  
    return render(request, 'orders/order_detail.html', {'order': order, 'total': total})
