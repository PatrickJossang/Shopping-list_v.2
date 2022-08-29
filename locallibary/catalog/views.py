from django.shortcuts                   import render
from .models                            import Item, Store, ItemInstance
from django.views                       import generic
from django.contrib.auth.mixins         import LoginRequiredMixin
from django.contrib.auth.decorators     import login_required, permission_required
from django.shortcuts                   import get_object_or_404
from django.http                        import HttpResponseRedirect
from django.urls                        import reverse
from catalog.forms                      import RenewItemForm
from django.views.generic.edit          import CreateView, UpdateView, DeleteView
from django.urls                        import reverse_lazy
import datetime

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
    paginate_by = 2
class ItemDetailView(generic.DetailView):
    model = Item
    

class StoreListView(generic.ListView):
    model = Store
    paginate_by = 2
class StoreDetailView(generic.DetailView):
    model = Store

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


class UsersItemsByListView(LoginRequiredMixin,generic.ListView):
    model = ItemInstance
    template_name ='catalog/iteminstance_list_got_item_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ItemInstance.objects.filter(got_item=self.request.user).filter(status__exact='o').order_by('due_back')



@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_item(request, pk):
    
    item_instance = get_object_or_404(ItemInstance, pk=pk)

    if request.method == 'POST':

        form = RenewItemForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            item_instance.due_back = form.cleaned_data['renewal_date']
            item_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-items-you-have'))

    
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewItemForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'item_instance': item_instance,
    }

    return render(request, 'catalog/item_renew_item.html', context)

#############RE-STORES##################
class StoreCreate(CreateView):
        model = Store
        fields = ['type_name', 'compeny_name']

class StoreUpdate(UpdateView):
    model = Store
    fields = '__all__' # potential security issue if more fields added

class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('store')

############RE-ITEMS#####################
class ItemCreate(CreateView):
        model = Item
        fields = ['title','store','summary']

class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__' # potential security issue if more fields added

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('items')
