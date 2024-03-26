from django.shortcuts import render

# Creamos una vista que se encargara de mostrar los productos de la pagina principal

def store(request):
    context = {}
    return render(request,'store/store.html',context)

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
    
