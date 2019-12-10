from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def posts(request):
    return render(request, 'posts.html')

def cadastro(request):
    return render(request, 'cadastro.html')











    # nome = 'groger'
    # # posts = {
    # #     'Gabriel' : 'Narnia para projetos ágeis',
    # #     'Vinicius': 'IA para comer biscoitos',
    # #     'Ana Lu': 'BTS é muito bondoso',
    # #     'Downtown': 'Não seja maníaco'
    # # }
    # # lista = ['Roré', 'Generro', 'Anlu', 'DOwnT0wn']
    # # contexto = {
    # #     'nome': nome,
    # #     'lista': lista
    # # }