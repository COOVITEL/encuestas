from django.shortcuts import render, redirect
from .forms import AsociadoForm, ColaboradorForm, DirigenteForm

def asociados(request):
    form = AsociadoForm()
    if request.method == 'POST':
        form = AsociadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    return render(request, 'asociado.html', {'form': form})

def colaborador(request):
    form = ColaboradorForm()
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    return render(request, 'colaborador.html', {'form': form})

def dirigente(request):
    form = DirigenteForm()
    if request.method == 'POST':
        form = DirigenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    return render(request, 'dirigente.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')
