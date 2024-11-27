from django.shortcuts import render, redirect
from .models import Paciente, Medico, Consulta


def cadastro_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        
        Paciente.objects.create(nome=nome, data_nascimento=data_nascimento, telefone=telefone, endereco=endereco)
        return redirect('cadastro_paciente')


    return render(request, 'consultas/cadastro_paciente.html')


def cadastro_medico(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        especialidade = request.POST['especialidade']
        crm = request.POST['crm']
        horarios_disponiveis = request.POST['horarios_disponiveis']
        
        Medico.objects.create(nome=nome, especialidade=especialidade, crm=crm, horarios_disponiveis=horarios_disponiveis)
        return redirect('cadastro_medico')


    return render(request, 'consultas/cadastro_medico.html')


def agendar_consulta(request):
    if request.method == 'POST':
        paciente_id = request.POST['paciente']
        medico_id = request.POST['medico']
        data_consulta = request.POST['data_consulta']


        paciente = Paciente.objects.get(id=paciente_id)
        medico = Medico.objects.get(id=medico_id)


        Consulta.objects.create(paciente=paciente, medico=medico, data_consulta=data_consulta)
        return redirect('agendar_consulta')


    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    return render(request, 'consultas/agendamento_consulta.html', {'pacientes': pacientes, 'medicos': medicos})
