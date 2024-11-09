from django.shortcuts import render, redirect
from django.http import FileResponse
from django.utils.translation import gettext as _
from reportlab.pdfgen import canvas
from user.models import Client
from shoppingCart.models import CartProduct

# Create your views here.
def generar_pdf(request):
    user = request.user
    response = FileResponse(generate_file(user),
                            as_attachment=True,
                            filename=_('factura.pdf'))
    return response

def generate_file(user):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    user = user
    cart = CartProduct.objects.filter(client=Client.objects.get(user=user))
    total_price = sum(item.product.price * item.quantity for item in cart)

    p.drawString(100, 800, _('Factura de {first_name} {last_name}').format(first_name=user.first_name, last_name=user.last_name))
    p.drawString(100, 780, _('Cliente: {email}').format(email=user.email))
    p.drawString(100, 760, _('Productos:'))
    y = 710
    for item in cart:
        p.drawString(120, y, _('{product_name} x {quantity}..........${total_price:.2f}').format(
            product_name=item.product.name,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity
        ))
        y -= 50
    p.drawString(100, y, _('Total: ${total_price:.0f}').format(total_price=total_price))
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
