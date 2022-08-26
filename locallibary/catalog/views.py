from django.shortcuts               import render
from .models                        import Item, Store, ItemInstance, Category
from django.views                   import generic
from django.contrib.auth.mixins     import LoginRequiredMixin

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

class ItemListView(generic.ListView):
    model = Item 
class ItemDetailView(generic.DetailView):
    model = Item

class ItemListView(generic.ListView):
    model = Item
    paginate_by = 10

class StoreListView(generic.ListView):
    model = Store
class StoreDetailView(generic.DetailView):
    model = Store

class StoreListView(generic.ListView):
    model = Store
    paginate_by = 10


def index(request):
    # …

    num_stores = Store.objects.count()  # The 'all()' is implied by default.
    num_items = Item.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_items': num_items,
        'num_stores': num_stores,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html.
    return render(request, 'index.html', context=context)


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = ItemInstance
    template_name ='catalog/iteminstance_list_got_item_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ItemInstance.objects.filter(got_item=self.request.user).filter(status__exact='o').order_by('due_back')