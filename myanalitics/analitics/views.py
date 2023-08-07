from django.shortcuts import render, redirect
from django.db import connections
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from .moodle import Mdlm9CourseCategories, Mdlm9Course, Mdlm9User, Mdlm9ForumPosts, Mdlm9ForumDiscussions, Mdlm9ChatMessages, Mdlm9UserEnrolments, Mdlm9Enrol, Mdlm9Chat
from .analitics import ForumPost, ForumDiscussion, ChatMessage
from django.db.models import Q
import pdb #pdb.set_trace()
import re
import pandas as pd
import nltk
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer


# Create Class your views here.
class Mdlm9Facultads:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mdlm9Actividades:
    def __init__(self, id, name):
        self.id = id
        self.name = name
                
# Create your views here.

#Index
def index(request):
    
    facultads = [
                Mdlm9Facultads(id=3365, name='FACULTAD DE ADMINISTRACION CENTRAL'),
                Mdlm9Facultads(id=3366, name='FACULTAD DE ARQUITECTURA Y URBANISMO'),
                Mdlm9Facultads(id=3367, name='FACULTAD DE CIENCIAS ADMINISTRATIVAS'),
                Mdlm9Facultads(id=3368, name='FACULTAD DE CIENCIAS AGRARIAS'),
                Mdlm9Facultads(id=3369, name='FACULTAD DE CIENCIAS ECONOMICAS'),
                Mdlm9Facultads(id=3381, name='FACULTAD DE CIENCIAS INTERNACIONALES Y DIPLOMACIA'),
                Mdlm9Facultads(id=3095, name='FACULTAD DE CIENCIAS MATEMATICAS Y FISICAS'),
                Mdlm9Facultads(id=3370, name='FACULTAD DE CIENCIAS MEDICAS'),
                Mdlm9Facultads(id=3371, name='FACULTAD DE CIENCIAS NATURALES'),
                Mdlm9Facultads(id=3377, name='FACULTAD DE CIENCIAS PARA EL DESARROLLO'),
                Mdlm9Facultads(id=3372, name='FACULTAD DE CIENCIAS PSICOLOGICAS'),
                Mdlm9Facultads(id=3374, name='FACULTAD DE CIENCIAS QUIMICAS'),
                Mdlm9Facultads(id=3373, name='FACULTAD DE COMUNICACION SOCIAL'),
                Mdlm9Facultads(id=3375, name='FACULTAD DE DIRECCION GENERAL DE POSTGRADO'),
                Mdlm9Facultads(id=3376, name='FACULTAD DE EDUCACION FISICA, DEPORTE Y RECREACION'),
                Mdlm9Facultads(id=3378, name='FACULTAD DE FILOSOFIA, LETRAS Y CIENCIA DE LA EDUCACION'),
                Mdlm9Facultads(id=3379, name='FACULTAD DE INGENIERIA INDUSTRIAL'),
                Mdlm9Facultads(id=3380, name='FACULTAD DE INGENIERIA QUIMICA'),
                Mdlm9Facultads(id=3380, name='FACULTAD DE JURISPRUDENCIA, CIENCIAS SOCIALES Y POLITICA')
            ]
    
    cursos = []
    materias = []

    if (request.GET.get('facultad') == '3095'):

        carreras = Mdlm9CourseCategories.objects.using('other').exclude(idnumber='').all()
        carrera_options_html = ''                       
        for carrera in carreras:
            carrera_options_html += f'<option value="{carrera.id}">{carrera.name}</option>'
                                
        # Agregar las opciones del select box de facultades al contexto del template
        context = {'carrera_options_html': carrera_options_html}                        
        #context = {'carreras': carreras}
    elif request.GET.get('carrera'):
        
        carrera_id = request.GET.get('carrera')
        cursos = Mdlm9CourseCategories.objects.using('other').filter(parent=carrera_id).all()
        
        # Construir un fragmento HTML que contenga las opciones del select box de cursos
        curso_options_html = ''
        for curso in cursos:
            curso_options_html += f'<option value="{curso.id}">{curso.name}</option>'

        # Agregar el fragmento HTML al contexto del template
        context = {'curso_options_html': curso_options_html}
    
    elif request.GET.get('curso'):
            curso_id = request.GET.get('curso')
            materias = Mdlm9Course.objects.using('other').filter(category=curso_id).all()
            
            # Construir un fragmento HTML que contenga las opciones del select box de materias
            materia_options_html = ''
            for materia in materias:
                materia_options_html += f'<option value="{materia.id}">{materia.fullname}</option>'
            
            # Agregar las opciones del select box de materias al contexto del template
            context = {'materia_options_html': materia_options_html}
            
    elif request.GET.get('materia'):
            materia_id = request.GET.get('materia')

            with connections['other'].cursor() as cursor:

                cursor.execute('''
                    SELECT u.id, u.firstname, u.lastname
                    FROM mdlm9_user u
                    INNER JOIN mdlm9_user_enrolments ue ON u.id = ue.userid
                    INNER JOIN mdlm9_enrol e ON ue.enrolid = e.id
                    WHERE e.courseid = %s
                ''', [materia_id])
                estudiantes_duplas = cursor.fetchall()

                estudiantes = []
                for estudiante_tupla in estudiantes_duplas:
                    estudiante = Mdlm9User()
                    estudiante.id = estudiante_tupla[0]
                    estudiante.firstname = estudiante_tupla[1]
                    estudiante.lastname = estudiante_tupla[2]
                    if len(estudiante_tupla) > 2:
                        estudiante.lastname = estudiante_tupla[2]
                    estudiantes.append(estudiante)
           
            estudiante_options_html = ''
            for estudiante in estudiantes:
                estudiante_options_html += f'<option value="{estudiante.id}">{estudiante.firstname}</option>'
            
            # Agregar las opciones del select box de materias al contexto del template
            context = {'estudiante_options_html': estudiante_options_html}            
    
    elif request.GET.get('estudiante'):
            
            actividades = [
                Mdlm9Actividades(id=0, name='Foro'),
                Mdlm9Actividades(id=1, name='Chatt')
            ]

            actividad_options_html = ''                       
            for actividad in actividades:
                actividad_options_html += f'<option value="{actividad.id}">{actividad.name}</option>'
                            
            # Agregar las opciones del select box de actividades al contexto del template
            context = {'actividad_options_html': actividad_options_html}                        
    else:

        context = {'facultads': facultads}

    return render(request, 'index.html', context)

#Bar
def bar(request):
    estudianteg_id = request.GET.get('estudianteg')
    cursog_id = request.GET.get('cursog')
    if estudianteg_id:    
        #Se Generan los Graficos Analiticos
        name_user  = Mdlm9User.objects.using('other').filter(id=estudianteg_id).values('firstname').first()
        name_stud = name_user['firstname']
        foros = Mdlm9ForumDiscussions.objects.using('other').filter(course=cursog_id)
        forointerus = Mdlm9ForumPosts.objects.using('other').filter(userid=estudianteg_id).values('userid').distinct()   
        if forointerus.exists():
            forointersub = Mdlm9ForumPosts.objects.using('other').filter(userid=estudianteg_id).exclude(message__isnull=True).exclude(message='').values('message').distinct().count()
            forointermes = Mdlm9ForumPosts.objects.using('other').filter(discussion__in=foros).exclude(userid=estudianteg_id).values('message').distinct().count()

            #Se Inicia el Proceso de Machine Leraning
        
            #1. Limpiar la tabla 
            ForumPost.objects.using('default').filter(user_id=estudianteg_id).delete()
            
            #2.- Obtener los datos
            user_posts = Mdlm9ForumPosts.objects.using('other').filter(userid=estudianteg_id)
            
            #3.- Envio y limpieza hacia la Tabla de Operatividad
            for post in user_posts:
                
                new_post = ForumPost.objects.using('default').create(
                    message = clean_text(post.message),
                    user_id=post.userid,
                    discussion_id=post.discussion,
                    course_id=cursog_id,
                )
                new_post.save()        
            
            #4.- Entrenamiento del modelo
            predicciones_entrenamiento = entrenar_modelo(1, estudianteg_id, cursog_id)
            conteo_sentimientos = predicciones_entrenamiento.value_counts()
        
            #5.- Calcular las cantidades de cada sentimiento
            negativos = predicciones_entrenamiento.value_counts().get('Negativo', 0)
            neutrales = predicciones_entrenamiento.value_counts().get('Neutral', 0)
            positivos = predicciones_entrenamiento.value_counts().get('Positivo',0)

            # Validar cuál sentimiento tiene el mayor conteo
            if negativos > neutrales and negativos > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEGATIVO. Esto indica que la mayoría de los comentarios expresan una opinión desfavorable o insatisfacción.'
            elif neutrales > negativos and neutrales > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEUTRAL. Esto indica que la mayoría de los comentarios no expresan una inclinación clara hacia lo positivo o lo negativo, sino que se mantienen en un punto intermedio o indiferente.'
            else:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es POSITIVO. Esto indica que la mayoría de los comentarios expresan una opinión favorable o satisfacción.'     
            #pdb.set_trace()                      
            return render(request, 'bar.html', {'forointerus': forointerus, 'forointersub': forointersub, 'forointermes': forointermes, 'name_stud': name_stud, 'negativos': negativos, 'neutrales': neutrales, 'positivos': positivos, 'sentimiento_mayor': sentimiento_mayor})
        
        else:
            return redirect('/')  
    else:
        return redirect('/')  

#Pie
def pie(request):
    estudianteg_id = request.GET.get('estudianteg')
    cursog_id = request.GET.get('cursog')

    if estudianteg_id:   
        #Se Generan los Graficos Analiticos
        name_user  = Mdlm9User.objects.using('other').filter(id=estudianteg_id).values('firstname').first()
        name_stud = name_user['firstname']
        forodiscus = Mdlm9ForumDiscussions.objects.using('other').filter(Q(userid=estudianteg_id) & Q(course=cursog_id)).exclude(name__isnull=True).exclude(name='').values('name').distinct().count()
        
        if forodiscus > 0:
            forodiscmes = Mdlm9ForumDiscussions.objects.using('other').filter(course=cursog_id).exclude(userid=estudianteg_id).exclude(name__isnull=True).exclude(name='').values('name').distinct().count()            
        
            #Se Inicia el Proceso de Machine Leraning
        
            #1. Limpiar la tabla 
            ForumDiscussion.objects.using('default').filter(Q(user_id=estudianteg_id) & Q(course_id=cursog_id)).delete()

            #2.- Obtener los datos
            user_discu = Mdlm9ForumDiscussions.objects.using('other').filter(Q(userid=estudianteg_id) & Q(course=cursog_id))
            
            #3.- Envio y limpieza hacia la Tabla de Operatividad
            for discu in user_discu:
                
                new_discu = ForumDiscussion.objects.using('default').create(
                    name = clean_text(discu.name),
                    course_id=discu.course,
                    user_id=discu.userid,
                    forum_id=discu.forum,
                )
                new_discu.save()        
            
            #4.- Entrenamiento del modelo
            predicciones_entrenamiento = entrenar_modelo(2, estudianteg_id, cursog_id)
            conteo_sentimientos = predicciones_entrenamiento.value_counts()
        
            #5.- Calcular las cantidades de cada sentimiento
            negativos = predicciones_entrenamiento.value_counts().get('Negativo', 0)
            neutrales = predicciones_entrenamiento.value_counts().get('Neutral', 0)
            positivos = predicciones_entrenamiento.value_counts().get('Positivo',0)

            # Validar cuál sentimiento tiene el mayor conteo
            if negativos > neutrales and negativos > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEGATIVO. Esto indica que la mayoría de los comentarios expresan una opinión desfavorable o insatisfacción.'
            elif neutrales > negativos and neutrales > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEUTRAL. Esto indica que la mayoría de los comentarios no expresan una inclinación clara hacia lo positivo o lo negativo, sino que se mantienen en un punto intermedio o indiferente.'
            else:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es POSITIVO. Esto indica que la mayoría de los comentarios expresan una opinión favorable o satisfacción.'     

            
            return render(request, 'pie.html', {'forodiscus': forodiscus, 'forodiscmes': forodiscmes, 'name_stud': name_stud, 'negativos': negativos, 'neutrales': neutrales, 'positivos': positivos, 'sentimiento_mayor': sentimiento_mayor})
       

        else:
            return redirect('/')  
    else:
            return redirect('/')  

#Line
def line(request):

    estudianteg_id = request.GET.get('estudianteg')
    cursog_id = request.GET.get('cursog')
    if estudianteg_id:   
        name_user  = Mdlm9User.objects.using('other').filter(id=estudianteg_id).values('firstname').first()
        name_stud = name_user['firstname']
        chats = Mdlm9Chat.objects.using('other').filter(course=cursog_id)
        chattusu = Mdlm9ChatMessages.objects.using('other').filter(chatid__in=chats,userid=estudianteg_id).exclude(message__isnull=True).exclude(message='').values('message').distinct().count()    
        
        if chattusu > 0:
            chattenviado = Mdlm9ChatMessages.objects.using('other').filter(chatid__in=chats).exclude(userid=estudianteg_id).exclude(message__isnull=True).exclude(message='').values('message').distinct().count()
            
            #Se Inicia el Proceso de Machine Leraning
        
            #1. Limpiar la tabla 
            ChatMessage.objects.using('default').filter(Q(user_id=estudianteg_id) & Q(course_id=cursog_id)).delete()

            #2.- Obtener los datos
            user_chatt = Mdlm9ChatMessages.objects.using('other').filter(chatid__in=chats,userid=estudianteg_id)
            
            #3.- Envio y limpieza hacia la Tabla de Operatividad
            for chatt in user_chatt:
                
                new_chatt = ChatMessage.objects.using('default').create(
                    message = clean_text(chatt.message),
                    course_id=cursog_id,
                    user_id=chatt.userid,
                )
                new_chatt.save()        
            
            #4.- Entrenamiento del modelo
            predicciones_entrenamiento = entrenar_modelo(3, estudianteg_id, cursog_id)
            conteo_sentimientos = predicciones_entrenamiento.value_counts()
        
            #5.- Calcular las cantidades de cada sentimiento
            negativos = predicciones_entrenamiento.value_counts().get('Negativo', 0)
            neutrales = predicciones_entrenamiento.value_counts().get('Neutral', 0)
            positivos = predicciones_entrenamiento.value_counts().get('Positivo',0)

            # Validar cuál sentimiento tiene el mayor conteo
            if negativos > neutrales and negativos > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEGATIVO. Esto indica que la mayoría de los comentarios expresan una opinión desfavorable o insatisfacción.'
            elif neutrales > negativos and neutrales > positivos:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es NEUTRAL. Esto indica que la mayoría de los comentarios no expresan una inclinación clara hacia lo positivo o lo negativo, sino que se mantienen en un punto intermedio o indiferente.'
            else:
                sentimiento_mayor = 'El sentimiento predominante del estudiante al participar en los mensajes de los Foros Generales es POSITIVO. Esto indica que la mayoría de los comentarios expresan una opinión favorable o satisfacción.'     


            return render(request, 'apilada.html', {'chattusu': chattusu, 'chattenviado': chattenviado, 'name_stud': name_stud, 'negativos': negativos, 'neutrales': neutrales, 'positivos': positivos, 'sentimiento_mayor': sentimiento_mayor})
        
        else:
            return redirect('/')  
    else:
            return redirect('/')  

#Algoritmo de Limpieza de Caracteres
def clean_text(text):
    
    # Eliminar caracteres no alfabéticos
    text = re.sub(r'<.*?>', ' ', text)

    # Convertir a minúsculas
    text = text.lower()

    # Eliminar palabras comunes
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    text = ' '.join(filtered_words)

    return text

#Entrenador del modelo    
def entrenar_modelo(param, estud, curs):
    
    if param == 1:
        # Preprocesamiento de datos y extracción de características
        mensajes = ForumPost.objects.using('default').filter(user_id=estud, course_id=curs).values_list('message', flat=True)   
        
    elif param == 2:
        
        # Preprocesamiento de datos y extracción de características
        mensajes = ForumDiscussion.objects.using('default').filter(user_id=estud).values_list('name', flat=True)           
        
    elif param == 3:
        
        # Preprocesamiento de datos y extracción de características
        mensajes = ChatMessage.objects.using('default').filter(user_id=estud).values_list('message', flat=True)                   

    # Crear un DataFrame con los mensajes        
    dataframe = pd.DataFrame({'mensaje': mensajes})

    # Obtener los puntajes de sentimiento compuesto utilizando el analizador de sentimientos Vader de NLTK
    analyzer = SentimentIntensityAnalyzer()
    dataframe['sentimiento'] = dataframe['mensaje'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Discretizar los puntajes de sentimiento compuesto
    dataframe['sentimiento'] = pd.cut(dataframe['sentimiento'],  bins=3, labels=['Negativo', 'Neutral', 'Positivo'])
        
    # Tokenizar los mensajes
    vectorizer = CountVectorizer()
    X_train_features = vectorizer.fit_transform(dataframe['mensaje'])

    # Crear un clasificador Naive Bayes
    classifier = MultinomialNB()

    # Entrenar el clasificador utilizando las características y las etiquetas de sentimiento
    classifier.fit(X_train_features, dataframe['sentimiento'])

    # Realizar predicciones en los datos de entrenamiento
    train_predictions = classifier.predict(X_train_features)

    # Imprimir las predicciones
    #for mensaje, sentimiento in zip(dataframe['mensaje'], train_predictions):
    #    print(f"Mensaje: {mensaje} - Sentimiento: {sentimiento}")
        
    # Retornar las predicciones de entrenamiento
    # Convertir train_predictions en un objeto Series
    train_predictions_series = pd.Series(train_predictions)
     
    return train_predictions_series