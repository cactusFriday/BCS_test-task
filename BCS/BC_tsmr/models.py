from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Transaction(models.Model):
    # num = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    creator = models.ForeignKey(
        User,
        verbose_name = 'user created transaction',
        on_delete = models.CASCADE,
        null = True,
        # default = ''
        )
    to_user = models.CharField(
        max_length = 150, 
        verbose_name = 'send coins to',
        # default = ''
        )
    prev_hash = models.CharField(max_length = 150, verbose_name = 'previous hash')
    amount = models.IntegerField(verbose_name = 'coins', blank=True, null=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'transaction by {User.login} to {to_user}'
    def gen_hash(self):
        return 'new_hash_sum'