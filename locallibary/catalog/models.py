from django.contrib.auth.models     import User
from django.db                      import models
from django.urls                    import reverse 
from datetime                       import date
import uuid       


################ITEM###############################
class Item(models.Model):
    #Model representing a item (but not a specific Item).
    title = models.CharField(max_length=200)

    store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a description of Item ')

    def __str__(self):
        #String for representing the Model object.
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this item."""
        return reverse('item-detail', args=[str(self.id)])

class ItemInstance(models.Model):
    #Model representing a specific item 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Item across whole Store')
    item = models.ForeignKey('Item', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    #To see if item is available
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'Refiling soon'),
        ('a', 'Available'),
        ('r', 'Out of item'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Item status',
    )
    got_item = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
    #Determines if item need to be renewed 
        return bool(self.due_back and date.today() > self.due_back)


    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_renewed", "Set Item as renewed"),)

    def __str__(self):
        #String for representing the Model object.
        return f'{self.id} ({self.item.title})'

#################STORE###############################

class Store(models.Model):
    #Model representing an store.
    compeny_name = models.CharField(max_length=100, help_text='Enter a compeny name', default=' ')
    type_name = models.CharField(max_length=100, help_text='Enter a type name', default=' ')
    class Meta:
        ordering = ['type_name', 'compeny_name']

    def get_absolute_url(self):
        #Returns the URL to access a particular store instance.
        return reverse('store_detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the Model object.
        return f'{self.compeny_name}, {self.type_name}'
