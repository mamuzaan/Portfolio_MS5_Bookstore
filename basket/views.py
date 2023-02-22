from django.shortcuts import render


def view_basket(request):
    """ A view that renders the basket content page """
    return render(request, 'basket/basket.html')
