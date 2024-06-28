from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import AsociadoForm, ColaboradorForm, DirigenteForm
from .models import Asociado, Colaborador, Dirigente
from django.shortcuts import render, redirect
from django.http import HttpResponse
from io import BytesIO
import pandas as pd


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

@login_required
def registersAso(request):
    """"""
    regisAsociados = Asociado.objects.all()
    paginatorAso = Paginator(regisAsociados, 10)
    page_number = request.GET.get('page', 1)
    try:
        regisAso = paginatorAso.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        regisAso = paginatorAso.page(1)
    
    lenAsociados = len(regisAsociados)
    return render(request, 'registros/regisAsociados.html', {
        'regisAso': regisAso,
        'lenAso': lenAsociados,
    })

@login_required
def registersCol(request):
    """"""
    regisColaboradores = Colaborador.objects.all()
    paginationCol = Paginator(regisColaboradores, 10)
    page_number_col = request.GET.get('page', 1)
    try:
        regisCol = paginationCol.page(page_number_col)
    except (EmptyPage, PageNotAnInteger):
        regisCol = paginationCol.page(1)
    lenColoboradores = len(regisColaboradores)
    return render(request, 'registros/regisColaboradores.html', {
        'regisCol': regisCol,
        'lenCol': lenColoboradores,
    })

@login_required
def registersDir(request):
    """"""       
    regisDirigentes = Dirigente.objects.all()
    paginationDir = Paginator(regisDirigentes, 10)
    page_number_dir = request.GET.get('page', 1)
    try:
        regisDir = paginationDir.page(page_number_dir)
    except (EmptyPage, PageNotAnInteger):
        regisDir = paginationDir.page(1)
    lenDigigentes = len(regisDirigentes)
    return render(request, 'registros/regisDirigentes.html', {
        'regisDir': regisDir,
        'lenDir': lenDigigentes
    })

@login_required
def downloadExcel(request):
    """"""
    regisAso = Asociado.objects.all()
    listRegisAso = list(regisAso.values())
    setRegisAso = [
        {**d,
            'Nombre': d.pop('name'),
            'Cedula': d.pop('cedula'),
            'Edad': d.pop('edad'),
            'Nivel Educativo': d.pop('nivelEducativo'),
            '¿Tiene familiares directos (hijos, cónyuge) que estén actualmente estudiando?': d.pop('familiares'),
            'Si su respuesta es, Sí, ¿Quienes?, Si es no, ingresa No': d.pop('familiaresDetalles'),
            
            '¿Qué tipo de formación o capacitación considera más importante para su desarrollo personal y profesional?': d.pop('personal1'),         
            '¿Por que?': d.pop('personal1Detalles'),
            '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?': d.pop('personal2'),
            'En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?': d.pop('personal3'),
            '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?': d.pop('personal4'),
            
            '¿Cuáles son las necesidades educativas más urgentes para sus familiares que están estudiando actualmente?': d.pop('familiares1'),
            '¿Considera que Coovitel podría ofrecer algún tipo de apoyo o programa educativo para sus familiares?': d.pop('familiares2'),
            '¿Como cual?': d.pop('familiares2Detalles'),
            '¿Qué tipo de apoyo educativo (becas, talleres, cursos) le gustaría que Coovitel proporcionara a sus familiares?': d.pop('familiares3'),
            
            '¿Qué espera de los programas educativos y de formación que ofrece Coovitel?': d.pop('pesem1'),
            '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?': d.pop('pesem2'),
            'En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?': d.pop('pesem3'),
            
            '¿Qué entiende por sector solidario y cooperativo?': d.pop('solidario1'),
            '¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?': d.pop('solidario2'),
            '¿Está familiarizado con los principios y valores cooperativos?': d.pop('solidario3'),
            '¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?': d.pop('solidario4'),
            
            '¿Cómo conoció a Coovitel?': d.pop('coovitel1'),
            '¿Cuánto tiempo lleva siendo asociado de Coovitel?': d.pop('coovitel2'),
            '¿Conoce los servicios y beneficios que ofrece Coovitel a sus asociados?': d.pop('coovitel3'),
            '¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?': d.pop('coovitel4'),
            '¿Cuales?': d.pop('coovitel3Detalles'),
            '¿Cómo calificaría su experiencia general con Coovitel?': d.pop('coovitel5'),
            '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus asociados?': d.pop('coovitel6'),
            
            '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas?': d.pop('sugerencia1'),
            '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?': d.pop('sugerencia2'), 
        }
        for d in listRegisAso
    ]
   
    regisCol = Colaborador.objects.all()
    listRegisCol = list(regisCol.values())
    setRegisCol = [
        {**d,
            '¿Cuál es su nombre completo?': d.pop('name'),
            '¿Cuál es su cedula?': d.pop('cedula'),
            '¿Cuál es su cargo actual en Coovitel?': d.pop('cargo'),
            '¿Cuántos años lleva trabajando en Coovitel?': d.pop('years'),
            '¿Cuál es su nivel educativo más alto alcanzado?': d.pop('nivelEducativo'),
            
            '¿Qué tipo de formación o capacitación considera más importante para su desarrollo profesional dentro de Coovitel?': d.pop('personal1'),
            '¿Por que?': d.pop('personal1Detalles'),
            '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?': d.pop('personal2'),
            'En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?': d.pop('personal3'),
            '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?': d.pop('personal4'),
            '¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?': d.pop('personal5'),
            '¿Cómo calificaría su experiencia en las actividades o programas educativos en los que ha participado?': d.pop('personal6'),
            
            '¿Qué espera de los programas educativos y de formación que ofrece Coovitel para los colaboradores?': d.pop('pesem1'),
            '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?': d.pop('pesem2'),
            'En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?': d.pop('pesem3'),
            '¿Qué impacto espera que tenga el PESEM en su desarrollo profesional dentro de la cooperativa?': d.pop('pesem4'),
            
            '¿Qué entiende por sector solidario y cooperativo?': d.pop('solidario1'),
            '¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?': d.pop('solidario2'),
            '¿Qué importancia cree que tiene el sector solidario y cooperativo en la sociedad?': d.pop('solidario3'),
            '¿Está familiarizado con los principios y valores cooperativos?': d.pop('solidario4'),
            '¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?': d.pop('solidario5'),
            
            '¿Cómo conoció a Coovitel?': d.pop('coovitel1'),
            '¿Conoce los servicios y beneficios que Coovitel ofrece a sus colaboradores?': d.pop('coovitel2'),
            '¿Cuales?': d.pop('coovitel2Detalles'),
            '¿Cómo calificaría su experiencia general trabajando en Coovitel?': d.pop('coovitel3'),
            '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus colaboradores?': d.pop('coovitel4'),
            
            '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas para los colaboradores?': d.pop('sugerencia1'),
            '¿Hay algún curso o tema específico que le gustaría que se incluyera en el PESEM?': d.pop('sugerencia2'),
            '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?': d.pop('sugerencia3'),
        }
    for d in listRegisCol]
    
    regisDir = Dirigente.objects.all()
    listRegisDir = list(regisDir.values())
    setRegisDir = [
        {**d,
            '¿Cuál es su nombre completo?': d.pop('name'),
            '¿Cuál es su cargo actual en Coovitel?': d.pop('cargo'),
            '¿Cuántos años lleva como Dirigente de Coovitel?': d.pop('years'),
            '¿Cuál es su nivel educativo más alto alcanzado?': d.pop('nivelEducativo'),
            
            '¿Qué tipo de formación o capacitación considera más importante para su desarrollo como dirigente dentro de Coovitel?': d.pop('persosnal1'),
            '¿Por que?': d.pop('personal1Detalles'),
            '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?': d.pop('personal2'),
            'En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?': d.pop('personal3'),
            '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?': d.pop('personal4'),
            '¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?': d.pop('personal5'),
            '¿Cómo calificaría su experiencia en las actividades o programas educativos en los que ha participado?': d.pop('personal6'),
            
            '¿Qué espera de los programas educativos y de formación que ofrece Coovitel para los dirigentes?': d.pop('pesem1'),
            '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?': d.pop('pesem2'),
            'En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?': d.pop('pesem3'),
            '¿Qué impacto espera que tenga el PESEM en su desarrollo como dirigente dentro de la cooperativa?': d.pop('pesem4'),
            
            '¿Qué entiende por sector solidario y cooperativo?': d.pop('solidario1'),
            '¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?': d.pop('solidario2'),
            '¿Qué importancia cree que tiene el sector solidario y cooperativo en la sociedad?': d.pop('solidario3'),
            '¿Está familiarizado con los principios y valores cooperativos?': d.pop('solidario4'),
            '¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?': d.pop('solidario5'),
            
            '¿Cómo conoció a Coovitel?': d.pop('coovitel1'),
            '¿Conoce los servicios y beneficios que Coovitel ofrece a sus dirigentes?': d.pop('coovitel2'),
            '¿Cuales?': d.pop('coovitel2Detalles'),
            '¿Cómo calificaría su experiencia general dirigiendo en Coovitel?': d.pop('coovitel3'),
            '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus dirigentes?': d.pop('coovitel4'),
            
            '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas para los dirigentes?': d.pop('sugerencia1'),
            '¿Hay algún curso o tema específico que le gustaría que se incluyera en el PESEM?': d.pop('sugerencia2'),
            '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?': d.pop('sugerencia3'),
        } for d in listRegisDir
    ]

    df_asociados = pd.DataFrame(setRegisAso)
    df_colaboradores = pd.DataFrame(setRegisCol)
    df_dirigentes = pd.DataFrame(setRegisDir)
    buffer = BytesIO()
    
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df_asociados.to_excel(writer, sheet_name='Asociados', index=False)
        df_colaboradores.to_excel(writer, sheet_name='Colaboradores', index=False)
        df_dirigentes.to_excel(writer, sheet_name='Dirigentes', index=False)

    buffer.seek(0)
    
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename=registrosPESEM.xlsx'}
    )

    return response