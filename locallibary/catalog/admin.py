from django.contrib     import admin
from .models            import Store, Category, Item, ItemInstance

#admin.site.register(Store)
#admin.site.register(Category)
#admin.site.register(Item)
#admin.site.register(ItemInstance)

# admin class
class StoreAdmin(admin.ModelAdmin):
    pass

#admin class with the associated model
admin.site.register(Store, StoreAdmin)


class ItemInstanceInline(admin.TabularInline):
    model = ItemInstance

#Admin classes for Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'store', 'display_category')

    inlines = [ItemInstanceInline]

#Admin classes for ItemInstance
@admin.register(ItemInstance)
class ItemInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('item', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name')

    fields = ['name']

class ItemInstanceAdmin(admin.ModelAdmin):
    list_display = ('item', 'status', 'got_item')
    list_filter = ('status', 'due_back','got_item')

    fieldsets = (
            (None, {
                'fields': ('item', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back','got_item')
            }),
        )
