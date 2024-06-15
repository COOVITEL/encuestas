from django import forms
from.models import Asociado, Colaborador, Dirigente

NIVEL_EDUCATIVO = [
    ('Sin educación formal', 'Sin educación formal'),
    ('Educación primaria', 'Educación primaria'),
    ('Educación secundaria', 'Educación secundaria'),
    ('Educación técnica o profesional', 'Educación técnica o profesional'),
    ('Educación universitaria (pregrado)', 'Educación universitaria (pregrado)'),
    ('Posgrado (maestría, doctorado, etc.)', 'Posgrado (maestría, doctorado, etc.)'),
]

EDUCATIVAS_PERSONALES = [
    ('Habilidades Técnicas: Formación específica en el uso de herramientas y tecnologías relevantes para el trabajo.',
     'Habilidades Técnicas: Formación específica en el uso de herramientas y tecnologías relevantes para el trabajo.'),
    ('Habilidades Blandas: Desarrollo de habilidades como comunicación, liderazgo, trabajo en equipo, y gestión del tiempo.',
     'Habilidades Blandas: Desarrollo de habilidades como comunicación, liderazgo, trabajo en equipo, y gestión del tiempo.'),
    ('Gestión y Liderazgo: Capacitación en gestión de proyectos, liderazgo, y toma de decisiones.',
     'Gestión y Liderazgo: Capacitación en gestión de proyectos, liderazgo, y toma de decisiones.'),
    ('Educación Financiera: Cursos sobre planificación financiera, inversiones, y gestión de finanzas personales.',
     'Educación Financiera: Cursos sobre planificación financiera, inversiones, y gestión de finanzas personales.'),
    ('Innovación y Creatividad: Talleres que fomenten la innovación, el pensamiento creativo y la solución de problemas.',
     'Innovación y Creatividad: Talleres que fomenten la innovación, el pensamiento creativo y la solución de problemas.'),
    ('Desarrollo Profesional Continuo: Programas de educación continua, certificaciones y desarrollo de carrera.',
     'Desarrollo Profesional Continuo: Programas de educación continua, certificaciones y desarrollo de carrera.'),
    ('Marketing y Ventas: Capacitación en estrategias de marketing, ventas y atención al cliente.',
     'Marketing y Ventas: Capacitación en estrategias de marketing, ventas y atención al cliente.'),
    ('Tecnologías de la Información: Formación en nuevas tecnologías, ciberseguridad y habilidades digitales.',
     'Tecnologías de la Información: Formación en nuevas tecnologías, ciberseguridad y habilidades digitales.'),
    ('Bienestar y Salud: Cursos sobre manejo del estrés, bienestar mental y físico, y balance vida-trabajo.',
     'Bienestar y Salud: Cursos sobre manejo del estrés, bienestar mental y físico, y balance vida-trabajo.'),
    ('Idiomas: Aprendizaje de nuevos idiomas o mejora de habilidades lingüísticas existentes.',
     'Idiomas: Aprendizaje de nuevos idiomas o mejora de habilidades lingüísticas existentes.'),
    ('Responsabilidad Social y Sostenibilidad: Capacitación en prácticas sostenibles, responsabilidad social corporativa y ética profesional.',
     'Responsabilidad Social y Sostenibilidad: Capacitación en prácticas sostenibles, responsabilidad social corporativa y ética profesional.'),
    ('Cooperativismo: Cursos Básicos y avanzado.',
     'Cooperativismo: Cursos Básicos y avanzado.')
]

OPTIONS = [
    ('Sí', 'Sí'),
    ('No', 'No'),
]

SCALE = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class AsociadoForm(forms.ModelForm):
    nivelEducativo = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=NIVEL_EDUCATIVO,
        label="¿Cuál es su nivel educativo actual?"
    )
    familiares = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Tiene familiares directos (hijos, cónyuge) que estén actualmente estudiando?"
    )
    
    personal1 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=EDUCATIVAS_PERSONALES,
        label="¿Qué tipo de formación o capacitación considera más importante para su desarrollo personal y profesional?"
    )
    
    personal3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?"
    )
    
    familiares2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Considera que Coovitel podría ofrecer algún tipo de apoyo o programa educativo para sus familiares?"
    )
    
    pesem3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?"
    )
    
    solidario2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?"
    )
    
    solidario3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Está familiarizado con los principios y valores cooperativos?"
    )
        
    solidario4 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?"
    )
    
    coovitel3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Conoce los servicios y beneficios que ofrece Coovitel a sus asociados?"
    )
    
    coovitel4 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?"
    )
    
    coovitel5 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="¿Cómo calificaría su experiencia general con Coovitel?"
    )

    class Meta:
        model = Asociado
        fields = [
            'name', 'cedula', 'edad', 'nivelEducativo', 'familiares', 'familiaresDetalles',
            'personal1', 'personal1Detalles', 'personal2', 'personal3', 'personal4',
            'familiares1', 'familiares2', 'familiares2Detalles', 'familiares3',
            'pesem1', 'pesem2', 'pesem3',
            'solidario1', 'solidario2', 'solidario3', 'solidario4',
            'coovitel1', 'coovitel2', 'coovitel3', 'coovitel3Detalles', 'coovitel4', 'coovitel5', 'coovitel6',
            'sugerencia1', 'sugerencia2'
            ]
        labels = {
            'name': '¿Cuál es su nombre completo?',
            'cedula': '¿Cuál es su cedula?',
            'edad': '¿Cuántos años tiene?',
            'familiaresDetalles': 'Si su respuesta es, Sí, ¿Quienes?',
            
            'personal1Detalles': '¿Por que?',
            'personal2': '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?',
            'personal4': '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?',
            
            'familiares1': '¿Cuáles son las necesidades educativas más urgentes para sus familiares que están estudiando actualmente?',
            'familiares2Detalles': '¿Como cual?',
            'familiares3': '¿Qué tipo de apoyo educativo (becas, talleres, cursos) le gustaría que Coovitel proporcionara a sus familiares?',
            
            'pesem1': '¿Qué espera de los programas educativos y de formación que ofrece Coovitel?',
            'pesem2': '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?',
            
            'solidario1': '¿Qué entiende por sector solidario y cooperativo?',
            
            'coovitel1': '¿Cómo conoció a Coovitel?',
            'coovitel2': '¿Cuánto tiempo lleva siendo asociado de Coovitel?',
            'coovitel3Detalles': '¿Cuales?',
            'coovitel6': '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus asociados?',
            
            'sugerencia1': '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas?',
            'sugerencia2': '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?',
        }


class ColaboradorForm(forms.ModelForm):
    
    nivelEducativo = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=NIVEL_EDUCATIVO,
        label="¿Cuál es su nivel educativo más alto alcanzado?"
    )
    personal1 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=EDUCATIVAS_PERSONALES,
        label="¿Qué tipo de formación o capacitación considera más importante para su desarrollo profesional dentro de Coovitel?"
    )
    personal3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?"
    )
    personal5 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?"
    )
    personal6 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="¿Cómo calificaría su experiencia en las actividades o programas educativos en los que ha participado?"
    )
    pesem3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?"
    )
    solidario2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?"
    )
    solidario4 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Está familiarizado con los principios y valores cooperativos?"
    )
    solidario5 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?"
    )
    coovitel2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Conoce los servicios y beneficios que Coovitel ofrece a sus colaboradores?"
    )
    coovitel3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="¿Cómo calificaría su experiencia general trabajando en Coovitel?"
    )
    class Meta:
        model = Colaborador
        fields = [
            'name', 'cargo', 'años', 'nivelEducativo',
            'personal1', 'personal1Detalles', 'personal2', 'personal3', 'personal4', 'personal5', 'personal6',
            'pesem1', 'pesem2', 'pesem3', 'pesem4',
            'solidario1', 'solidario2', 'solidario3', 'solidario4', 'solidario5',
            'coovitel1', 'coovitel2', 'coovitel2Detalles', 'coovitel3', 'coovitel4',
            'sugerencia1', 'sugerencia2', 'sugerencia3'      
        ]
        labels = {
            'name': '¿Cuál es su nombre completo?',
            'cargo': '¿Cuál es su cargo actual en Coovitel?',
            'años': '¿Cuántos años lleva trabajando en Coovitel?',
            
            'personal1Detalles': '¿Por que?',
            'personal2': '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?',
            'personal4': '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?',
            
            'pesem1': '¿Qué espera de los programas educativos y de formación que ofrece Coovitel para los colaboradores?',
            'pesem2': '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?',
            'pesem4': '¿Qué impacto espera que tenga el PESEM en su desarrollo profesional dentro de la cooperativa?',
            
            'solidario1': '¿Qué entiende por sector solidario y cooperativo?',
            'solidario3': '¿Qué importancia cree que tiene el sector solidario y cooperativo en la sociedad?',
            
            'coovitel1': '¿Cómo conoció a Coovitel?',
            'coovitel2Detalles': '¿Cuales?',
            'coovitel4': '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus colaboradores?',
            
            'sugerencia1': '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas para los colaboradores?',
            'sugerencia2': '¿Hay algún curso o tema específico que le gustaría que se incluyera en el PESEM?',
            'sugerencia3': '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?',
        }


class DirigenteForm(forms.ModelForm):
    
    nivelEducativo = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=NIVEL_EDUCATIVO,
        label="¿Cuál es su nivel educativo más alto alcanzado?"
    )
    personal1 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=EDUCATIVAS_PERSONALES,
        label="¿Qué tipo de formación o capacitación considera más importante para su desarrollo como dirigente dentro de Coovitel?"
    )
    personal3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán satisfecho está con las oportunidades educativas que ofrece actualmente Coovitel?"
    )
    personal5 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha participado en actividades o programas educativos ofrecidos por Coovitel?"
    )
    personal6 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="¿Cómo calificaría su experiencia en las actividades o programas educativos en los que ha participado?"
    )
    pesem3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="En una escala del 1 al 5, ¿cuán probable es que participe en nuevas iniciativas educativas ofrecidas por Coovitel?"
    )
    solidario2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Ha recibido alguna formación o información sobre el sector solidario y cooperativo?"
    )
    solidario4 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Está familiarizado con los principios y valores cooperativos?"
    )
    solidario5 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Le gustaría recibir más información o formación sobre el sector solidario y cooperativo?"
    )
    coovitel2 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=OPTIONS,
        label="¿Conoce los servicios y beneficios que Coovitel ofrece a sus dirigentes?"
    )
    coovitel3 = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=SCALE,
        label="¿Cómo calificaría su experiencia general dirigiendo en Coovitel?"
    )
    class Meta:
        model = Dirigente
        fields = [
            'name', 'cargo', 'años', 'nivelEducativo',
            'personal1', 'personal1Detalles', 'personal2', 'personal3', 'personal4', 'personal5', 'personal6',
            'pesem1', 'pesem2', 'pesem3', 'pesem4',
            'solidario1', 'solidario2', 'solidario3', 'solidario4', 'solidario5',
            'coovitel1', 'coovitel2', 'coovitel2Detalles', 'coovitel3', 'coovitel4',
            'sugerencia1', 'sugerencia2', 'sugerencia3'      
        ]
        labels = {
            'name': '¿Cuál es su nombre completo?',
            'cargo': '¿Cuál es su cargo actual en Coovitel?',
            'años': '¿Cuántos años lleva como Dirigente de Coovitel?',
            
            'personal1Detalles': '¿Por que?',
            'personal2': '¿Qué habilidades o conocimientos le gustaría adquirir o mejorar en el corto plazo (1-2 años)?',
            'personal4': '¿Qué temáticas o áreas de formación le gustaría que Coovitel ofreciera en el futuro?',
            
            'pesem1': '¿Qué espera de los programas educativos y de formación que ofrece Coovitel para los dirigentes?',
            'pesem2': '¿Cómo cree que Coovitel podría mejorar sus servicios educativos para satisfacer mejor sus necesidades?',
            'pesem4': '¿Qué impacto espera que tenga el PESEM en su desarrollo como dirigente dentro de la cooperativa?',
            
            'solidario1': '¿Qué entiende por sector solidario y cooperativo?',
            'solidario3': '¿Qué importancia cree que tiene el sector solidario y cooperativo en la sociedad?',
            
            'coovitel1': '¿Cómo conoció a Coovitel?',
            'coovitel2Detalles': '¿Cuales?',
            'coovitel4': '¿Qué sugerencias tiene para mejorar la relación y comunicación entre Coovitel y sus dirigentes?',
            
            'sugerencia1': '¿Tiene alguna sugerencia específica sobre cómo Coovitel podría mejorar sus ofertas educativas para los dirigentes?',
            'sugerencia2': '¿Hay algún curso o tema específico que le gustaría que se incluyera en el PESEM?',
            'sugerencia3': '¿Qué considera que es lo más importante para el éxito del PESEM en la cooperativa?',
        }
        
        def clean(self):
            cleaned_data = super().clean()
            
            name = cleaned_data.get('name')
            
            if Dirigente.objects.filter(name=name).exists():
                self.add_error('name', 'El nombre debe ser único.')

            return cleaned_data