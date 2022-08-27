from django.contrib     import admin
from .models            import Store, Item, ItemInstance

##############STORE####################
class StoreAdmin(admin.ModelAdmin):
    list_display = ('compeny_name','type_name',)

    fields = ['compeny','type_name']


#admin class with the associated model
admin.site.register(Store, StoreAdmin)



##############ITEMS####################
class ItemInstanceInline(admin.TabularInline):
    model = ItemInstance

#Admin classes for Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'store',)

    inlines = [ItemInstanceInline]

@admin.register(ItemInstance)
class ItemInstanceAdmin(admin.ModelAdmin):
    list_display = ('item', 'status', 'got_item','due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
            (None, {
                'fields': ('item', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back','got_item')
            }),
        )