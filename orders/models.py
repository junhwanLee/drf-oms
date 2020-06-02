from django.db import models
from django.contrib.auth import get_user_model


class Order(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='고객')
    order_number = models.CharField(unique=True, max_length=12, verbose_name='주문번호')
    product_name = models.CharField(max_length=100, verbose_name='제품명')
    paymented_at= models.DateTimeField(auto_now_add=True, verbose_name='결제일시')

    def __str__(self):
        return "{}-{}".format(customer.email, self.product_name)
