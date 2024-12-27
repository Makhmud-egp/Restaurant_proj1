from django.db import models

# Menu model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Description field added
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price field

    def __str__(self):
        return f"{self.name} - ${self.price}"

# Zakaz model
class Order(models.Model):
    table_number = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    
    
    def total_price(self):
        return sum(order_item.quantity * order_item.menu_item.price for order_item in self.order_items.all())

    def __str__(self):
        return f"Order for Table {self.table_number} - Paid: {self.is_paid}"

# Zakazed model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
