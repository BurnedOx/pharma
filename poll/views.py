from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def home_view(request):
    popular_products = Product.objects.filter(popular=True)
    new_products = Product.objects.all()[:6]
    template = "pages/home.html"
    context = {
        "home_page": "active",
        "popular_products": popular_products,
        "new_products": new_products,
    }
    return render(request, template, context)


class AboutView(generic.TemplateView):
    template_name = "pages/about.html"

    def get(self, request):
        context = { "about_page": "active"}
        return render(request, self.template_name, context)


def product_view(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    template = "pages/products.html"
    context = {
        "products_page": "active",
        "products": products
        }
    return render(request, template, context)


class ContactView(generic.TemplateView):
    template_name = "pages/contact.html"

    def get(self, request):
        context = { "contact_page": "active"}
        return render(request, self.template_name, context)
