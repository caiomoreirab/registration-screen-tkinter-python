import getpass
from tkinter import *
from tkinter import messagebox

janela = Tk() #Inicialização da Janela 
janela.title("Cadastro de Usuario") #Titulo da Janela
janela.geometry("350x330") #Dimensões da Janela

janela.config(bg="#bdb295") #background 
janela.iconphoto(False, PhotoImage(file="login.png")) #Alterando o icone da Janela 



#Back-and: 
dados_do_usuario = []


def cadastro_do_usuario():
    usuarios = {}
    nome_de_usuario = entrada_usuario.get()
    senha_do_usuario = entrada_senha.get()

    for usuario in usuarios:
        if usuario['nome'] == nome_de_usuario:
            print("Este nome de usuário já existe. Tente novamente.")
            return


    novo_usuario = {
        'nome': nome_de_usuario,
        'senha': senha_do_usuario
    }
    usuarios.update(novo_usuario)
    messagebox.showinfo("Informações do Usuário", f"Nome: {nome_de_usuario}\nSenha: {senha_do_usuario}")





#InterFace >> Front-end: 

texto_cadastro_usuario = Label(janela,   text = "Cadastro de Usuário:", font = ("Arial 12 "), fg="black", bg="#bdb295" )
texto_cadastro_usuario.place(x=105 , y=95)

texto_usuario = Label(janela,   text = "Usuario: ", font = ("Arial 7 "), fg="black", bg="#bdb295" )
texto_usuario.place(x=65, y=130)


texto_senha = Label(janela,   text = "Senha: ", font = ("Arial 7 "), fg="black", bg="#bdb295" )
texto_senha.place(x=65 , y=155)

entrada_usuario = Entry(janela, font = ("Arial 9 "), fg="black", bg="#f0ece6" )
entrada_usuario.place(x=110 , y=130)

entrada_senha = Entry(janela, show="*", font = ("Arial 9 "), fg="black", bg="#f0ece6" )
entrada_senha.place(x=110 , y=155)


botao_cadastro = Button(janela, command=cadastro_do_usuario,   text = "Cadastrar", font = ("Arial 9 "), fg="black", bg="#f0ece6" )
botao_cadastro.place(x=145 , y= 185)


janela.mainloop() 
















