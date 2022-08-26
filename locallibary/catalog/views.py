from django.shortcuts   import render
from .models            import Item, Store, ItemInstance, Category

def index(request):
    #View home page of site.

    # Generate counts of some of the main objects
    num_items = Item.objects.all().count()
    num_instances = ItemInstance.objects.all().count()

    # Available items (status = 'a')
    num_instances_available = ItemInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_store = Store.objects.count()

    context = {
        'num_items': num_items,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_store': num_store,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
