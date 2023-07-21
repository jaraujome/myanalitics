from django.shortcuts import render
from .utils.naive_bayes import MultinomialNB
from django.db.models import Count
from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
from django.db import connections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from .moodle import Mdlm9CourseCategories, Mdlm9Course, Mdlm9User, Mdlm9ForumPosts, Mdlm9ForumDiscussions, Mdlm9ChatMessages
#from .models import 
# Create your views here.

#Index
def index(request):
    carreras = Mdlm9CourseCategories.objects.using('other').exclude(idnumber='').all()
    cursos = Mdlm9CourseCategories.objects.using('other').filter(idnumber='').all()
    materias = Mdlm9Course.objects.using('other').all()
    alumnos = Mdlm9User.objects.using('other').all()
    #with connections['other'].cursor() as cursor:
     #   cursor.execute('SELECT * FROM mdlm9_user')
        #PENDIENTE MEJORAR
        #SELECT mdlm9_user.*
            #FROM mdlm9_user
            #JOIN mdlm9_role_assignments ON mdlm9_role_assignments.userid = mdlm9_user.id
            #JOIN mdlm9_role ON mdlm9_role.id = mdlm9_role_assignments.roleid
            #WHERE mdlm9_role.id = 5;
    #alumnos = cursor.fetchall()
    return render(request, 'index.html', {'carreras': carreras, 'cursos': cursos, 'materias': materias, 'alumnos': alumnos})

#Bar
def bar(request):
    forointerus = Mdlm9ForumPosts.objects.using('other').filter(userid=3765).values('userid').distinct()    
    forointersub = Mdlm9ForumPosts.objects.using('other').filter(userid=810).exclude(subject__isnull=True).exclude(subject='').values('subject').distinct().count()
    forointermes = Mdlm9ForumPosts.objects.using('other').filter(userid=810).exclude(subject__isnull=True).exclude(message='').values('message').distinct().count()
    return render(request, 'bar.html', {'forointerus': forointerus, 'forointersub': forointersub, 'forointermes': forointermes})

#Pie
def pie(request):
    forodiscus = Mdlm9ForumDiscussions.objects.using('other').filter(userid=810).distinct().all()   
    forodiscmes = Mdlm9ForumDiscussions.objects.using('other').filter(userid=810).exclude(name__isnull=True).exclude(name='').values('name').distinct().count()
    forodiscrest = (10 - forodiscmes)
    return render(request, 'pie.html', {'forodiscus': forodiscus, 'forodiscmes': forodiscmes, 'forodiscrest' : forodiscrest})

#Line
def line(request):
    chattusu = Mdlm9ChatMessages.objects.using('other').filter(userid=3445).values('userid').distinct()    
    chattenviado = Mdlm9ChatMessages.objects.using('other').filter(userid=3445).exclude(message__isnull=True).exclude(message='').values('message').distinct().count()
    chattenvcrest = (100 - chattenviado)
    return render(request, 'apilada.html', {'chattusu': chattusu, 'chattenviado': chattenviado, 'chattenvcrest': chattenvcrest})

def get_cursos(request):
    carrera_id = request.GET.get('carrera_id')
    cursos = Mdlm9CourseCategories.objects.filter(carrera_id=carrera_id)
    options = ''
    for curso in cursos:
        options += f'<option value="{curso.id}">{curso.name}</option>'
    return JsonResponse({'options': options})
    
    #Aplico Machine Learning
def load_data(request):
    # obtener la conexión a la base de datos "other"
    connection = connections['other']

    # ejecutar una consulta SQL en la tabla "messages" de la base de datos "other"
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM Mdlm9ChatMessages')
        data = cursor.fetchall()

    # realizar preprocesamiento de los datos
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    X = []
    y = []

    for row in data:
        message = row[1]
        label = row[2]

        tokens = word_tokenize(message.lower())
        filtered_tokens = [token for token in tokens if token not in stop_words]
        lemmas = [lemmatizer.lemmatize(token) for token in filtered_tokens]
        X.append(' '.join(lemmas))
        y.append(label)

    # continuar con el procesamiento de los datos...
    # guardar los datos procesados en la base de datos
    for i in range(len(X)):
        processed = Mdlm9ChatMessages(text=X[i], label=y[i])
        processed.save()
    
    return render(request, 'load_data.html')