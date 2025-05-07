from django.shortcuts import render , get_object_or_404,redirect
from .models import Curso

# Create your views here.
def criar_curso(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        professor = request.POST.get('professor')
        imagem = request.FILES.get('imagem')        
        
        # Criando e salvando o curso diretamente com o create
        Curso.objects.create(nome=nome, descricao=descricao, professor=professor, imagem=imagem)

        # Redirecionando para a página principal (ou lista de cursos)
        return redirect('/')

    return render(request, 'criar.html')

def lista_cursos(request):
    cursos= Curso.objects.all()
    return render(request, 'lista.html', {'cursos': cursos})

def detalhes_curso(request, curso_id):
    # Usando get_object_or_404 para buscar um único curso pelo id
   curso = get_object_or_404(Curso, id=curso_id)

   return render(request, 'detalhes_curso.html', {'curso': curso})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso

def excluir_curso(request, curso_id):
    # Obter o curso que será excluído
    curso = get_object_or_404(Curso, id=curso_id)

    # Excluir o curso
    if request.method == 'POST':
        curso.delete()
        return redirect('/')  # Redireciona para a lista de cursos

    # Caso não seja um POST, apenas exibe a página de confirmação de exclusão
    return render(request, 'excluir_curso.html', {'curso': curso})

    