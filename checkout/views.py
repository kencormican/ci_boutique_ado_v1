from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

from django.conf import settings
from bag.contexts import bag_contents

import stripe

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
         'stripe_public_key': 'pk_test_51I896EKt3nd5V9dl3nqH1s5E0tSduGijapjDcN6o3YfLnAUpDq7fGndyCK7HlJ270mn3raSGyUZny4NycLtRFgez00cwWOfiYa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
