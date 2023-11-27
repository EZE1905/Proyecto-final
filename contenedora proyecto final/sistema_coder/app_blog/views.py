from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

from app_blog.models import Articulo
from app_blog.forms import ArticuloFormulario


def listar_articulos(request):
    contexto = {
        "Articulos": Articulo.objects.all()
        }
    http_response = render(
        request=request,
        template_name='app_blog/articulos.html',
        context=contexto,
    )
    return http_response

@login_required
def crear_articulos(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            autor = data["autor"]
            fecha = data["fecha"]
            
            articulo = Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, creador=request.user)
            articulo.save()

            url_exitosa = reverse('listar_articulos')
            return redirect(url_exitosa)
    else: 
        formulario = ArticuloFormulario()

    return render(
        request=request,
        template_name='app_blog/formulario_articulo.html',
        context={'formulario': formulario}
    )

def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda", "")
        campo_busqueda = data.get("campo_busqueda", "titulo")  # Valor predeterminado a 'titulo'

        # Crear un diccionario para mapear los campos del modelo con los campos del formulario
        campos_modelo = {
            "titulo": "titulo",
            "autor": "autor",
        }

        # Obtener el campo del modelo correspondiente al campo de búsqueda seleccionado
        campo_modelo = campos_modelo.get(campo_busqueda, "titulo")

        # Realizar la búsqueda en el modelo utilizando el campo adecuado
        articulo = Articulo.objects.filter(
            Q(**{f"{campo_modelo}__icontains": busqueda})
        )

        contexto = {
            "Articulos": articulo,
        }

        return render(
            request=request,
            template_name='app_blog/articulos.html',
            context=contexto,
        )

    return render(request, 'app_blog/articulos.html')

def detalle_articulo(request, id):
    # Recuperar el artículo usando su ID
    articulo = get_object_or_404(Articulo, id=id)

    # Puedes agregar lógica adicional aquí si es necesario

    # Renderizar la plantilla con el artículo
    return render(request, 'app_blog/detalle_articulo.html', {'articulo': articulo})

@login_required
def eliminar_articulo(request, id):
    # Obtener el artículo de la base de datos
    articulo_instance = Articulo.objects.get(id=id)

    if request.method == "POST":
        # Borrar el artículo de la base de datos
        articulo_instance.delete()
        # Redireccionar a la URL exitosa
        url_exitosa = reverse('listar_articulos')
        return redirect(url_exitosa)

@login_required    
def editar_articulo(request, id):
    articulo_editado = Articulo.objects.get(id=id)

    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST, instance=articulo_editado)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('listar_articulos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario(instance=articulo_editado)

    return render(
        request=request,
        template_name='app_blog/formulario_articulo.html',
        context={'formulario': formulario},
    )