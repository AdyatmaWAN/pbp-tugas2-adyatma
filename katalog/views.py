from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Adyatma W.A.N.Y.',
        'npm': '2106750805'
    }
    return render(request, "katalog.html", context)
