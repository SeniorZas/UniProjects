from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

#Easter Egg
def test(request):
    
    return HttpResponse("Página de prueba lol XD chúpalo Seba")

#Registro
def register(request):
    if request.user.is_authenticated:
        return redirect('home.html')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect('/home.html')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "register.html",
        context={"form": form}
    )

#Logout y Login
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home.html")

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("home.html")

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("home.html")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )

#Home
@login_required
def home(request):
    
    docExterno=loader.get_template('home.html')
    Bienvenida = docExterno.render()
    
    return HttpResponse(Bienvenida)    

@login_required
def carreras(request):
    
    docExterno=loader.get_template('carreras/carreras.html')
    Carreras=docExterno.render()
    
    return HttpResponse(Carreras)

@login_required
def ramos(request):
    
    docExterno=loader.get_template('ramos/ramos.html')
    ramos=docExterno.render()
    
    return HttpResponse(ramos)

#Mat021
@login_required
def mat021(request):
    
    docExterno=loader.get_template('ramos/General/Mate/mat021.html')
    mat021=docExterno.render()
    
    return HttpResponse(mat021)

def notasSemestrales(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Notas Semestrales.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    
def c120141(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Certamen1-2014-1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    
def c120142(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Certamen1-2014-2.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response    
    
def c120151(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Certamen1-2015-1-SJ.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response    
    
def c220152(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/PautaCert2-2015-Problemas1,2 y 4.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response 
    
def c320142(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Pauta Certamen3_S2_2014.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response       
    
def cgmat021(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/PautaGlobal.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response      
    
def co120151(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Control1-2015-1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response     

def co120151(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Control1-2015-1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response 
    
def ejerciciosInduccion(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Ejercicios de Inducción.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response  
    
def guiaSumyPro(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Guia de Sumatorias y Progresiones.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response    
    
def pautaTallerC2(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/PautaTallerC2-1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response   
    
def Taller1Mat021(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Taller 1 Dasarrollado.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response   
    
def Taller2Mat021(request):
    with open('SansaCloud/FILES(PDFS)/Mat021/Taller 2 Desarrollado.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response                

#Iwi131
@login_required
def iwi131(request):
    
    docExterno=loader.get_template('ramos/General/iwi131.html')
    iwi131=docExterno.render()
    
    return HttpResponse(iwi131)

def UVA1(request):
    with open('SansaCloud/FILES(PDFS)/Iwi131/Tarea UVA 1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response        
    
def UVA9(request):
    with open('SansaCloud/FILES(PDFS)/Iwi131/Tarea UVA 9_ Archivos de Texto.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response        



#Fis100
def fis100(request):
    
    docExterno=loader.get_template('ramos/General/Fisica/fis100.html')
    fis100=docExterno.render()
    
    return HttpResponse(fis100)


#Hrw130
def hrw130(request):
    
    docExterno=loader.get_template('ramos/General/Humanistas/hrw130.html')
    hrw130=docExterno.render()
    
    return HttpResponse(hrw130)

def ResumenHrw130(request):
    with open('SansaCloud/FILES(PDFS)/Hrw130/Resumen Parte adán texto Qué es la ética apartado saber-poder.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response 
    
def Taller1Etica(request):
    with open('SansaCloud/FILES(PDFS)/Hrw130/Taller 1 Etica.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response 

#Carreras
@login_required
def ingCivilInf(request):
    docExterno=loader.get_template('carreras/IngenieriaCivilInformatica.html')
    ingCivilInf=docExterno.render()
    
    return HttpResponse(ingCivilInf)

