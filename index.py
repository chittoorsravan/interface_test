from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [sg.text('Usuário'), sg.input(key='usuário', size=(20, 1))],
    [sg.text('Senha'), sg.input(key='senha', password_char='*', size=(20, 1))],
    [sg.checkbox('Salvar o login?')],
    [sg.button('Entrar')]
]
# janela
janela = sg.window('Tela de Login', layout)
# Eventos que iram acontecer (ler os eventos)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Andre' and valores ['senha'] == '123456' 
           print('Bem-vindo a interface Python!')
            