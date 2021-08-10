# from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'manufacturer', 'price', 'quantity']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'manufacturer', 'price', 'quantity']


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')
