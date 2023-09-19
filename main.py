###  imppotrtação

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pynput.keyboard import Key, Listener
import sqlite3
import time
import datetime
import os
import asyncio


class Win_main:
    def __init__(self):
        self.janela_main = Tk()
        self.janela_main.geometry("700x600")
        self.janela_main.maxsize(700, 600)
        self.janela_main.minsize(500, 450)
        self.janela_main.title("Cadasto e gerenciamento de usuarios")

        # janela de cadastro
        def pagina_log():
            self.janela_main.destroy()
            janela_log = Tk()
            janela_log.geometry("600x450")
            janela_log.maxsize(600, 450)
            janela_log.minsize(600, 450)
            # 600 largura X 450 altura
            janela_log.title("Login do usuario")

            texto_log = Label(text="Digite o cpf abaixo(SOMENTE NUMEROS)")
            texto_log.pack()

            def limitar_tamanho(p):
                if len(p) > 11:
                    return False
                return True

            vcmd = janela_log.register(func=limitar_tamanho)

            cpf_log_entrada = Entry(
                janela_log, validate="key", validatecommand=(vcmd, "%P")
            )
            cpf_log_entrada.pack(side="bottom")

            def seg_log_cpf():
                pegar_cpf = cpf_log_entrada.get()
                lista_soma = list(str(pegar_cpf))
                valores = [int(val) for val in lista_soma]
                soma_cpf = sum(valores)

                cpfs_validos = [
                    10,
                    11,
                    12,
                    21,
                    22,
                    23,
                    32,
                    33,
                    34,
                    43,
                    44,
                    45,
                    54,
                    55,
                    56,
                    65,
                    66,
                    67,
                    76,
                    77,
                    78,
                    87,
                    88,
                ]

                if soma_cpf in cpfs_validos:
                    for filename in os.listdir("./"):
                        if filename == ("users.db"):
                            curso.execute("SELECT")

                        else:
                            conector = sqlite3.connect("transações.db")
                            curso = conector.cursor()

                            curso.execute(
                                "CREATE TABLE transações (Cpf integer, Nome text, Funcao text)"
                            )
                else:
                    error_cpf = messagebox.showinfo(
                        title="Erro", message="Cpf invalido!"
                    )

        # paginqa de cadastro
        def pagina_cad():
            self.janela_main.destroy()
            janela_cad = Tk()
            janela_cad.geometry("600x450")
            janela_cad.maxsize(600, 450)
            janela_cad.minsize(600, 450)
            # 600 largura X 450 altura
            janela_cad.title("Cadastramento de usuario")

            # self.error_name = messagebox.showwarning(title="erro", message="Por favor digite pelo menos nome e sobrenome")
            # self.error_cpf = messagebox.showinfo(title="Erro", message="Cpf invalido!" )

            conteiner_name = Frame(janela_cad, width=200, height=150)
            
            conteiner_cpf = Frame(janela_cad, width=200, height=150)

            conteiner_funcao = Frame(janela_cad, width=200, height=150)

            nome_text = Label(
                janela_cad,
                text="Digite abaixo o nome completo do usuario(nome completo):",
            )
            nome_text.grid(row=0, column=0)

            # pegar o nome do  usuario
            nome_entrada = Entry(janela_cad)
            nome_entrada.grid(row=1, column=0)

            # funções  pra verificar se o que o usuario esta correto
            def seg_cad_name():
                pegar_nome = nome_entrada.get()
                conerter_nome = len(pegar_nome)
                result_nome = int(conerter_nome)

                # nums = ['0','1', '2','3','4', '5','6','7', '8', '9']
                # lista_soma =list(str(nums))

                if result_nome < 8:
                    self.error_name = messagebox.showinfo(
                        title="erro",
                        message="Por favor digite pelo menos nome e sobrenome",
                    )

                else:
                    cpf_text = Label(
                        janela_cad, text="insira seu cpf abaixo (apenas numeros)"
                    )
                    cpf_text.grid(row=2)

                    def limitar_tamanho(p):
                        if len(p) > 11:
                            return False
                        return True

                    vcmd = janela_cad.register(func=limitar_tamanho)

                    cpf_entrada = Entry(
                        janela_cad, validate="key", validatecommand=(vcmd, "%P")
                    )
                    cpf_entrada.grid(row=3)

                    # verificar se o cpf que o usuario esta correto

                    def seg_cad_cpf():
                        pegar_cpf = cpf_entrada.get()
                        lista_soma = list(str(pegar_cpf))
                        valores = [int(val) for val in lista_soma]
                        soma_cpf = sum(valores)

                        cpfs_validos = [
                            10,
                            11,
                            12,
                            21,
                            22,
                            23,
                            32,
                            33,
                            34,
                            43,
                            44,
                            45,
                            54,
                            55,
                            56,
                            65,
                            66,
                            67,
                            76,
                            77,
                            78,
                            87,
                            88,
                        ]

                        if soma_cpf in cpfs_validos:
                            pass

                        else:
                            error_cpf = messagebox.showinfo(
                                title="Erro", message="Cpf invalido!"
                            )

            # botão pra confirmar as informacoes passadas pelo usuario
            conf_but = Button(janela_cad, command=seg_cad_name, text="proximo")
            conf_but.grid(row=1, column=1, pady=40)

            janela_cad.mainloop()
            pagina_log.mainloop()

        self.botao_log = Button(
            self.janela_main,
            text="clique aqui caso deseja fazer login ",
            command=pagina_log
        )
        self.botao_log.pack(side="bottom")

        self.botao_cad = Button(
            self.janela_main,
            text="clique aqui para fazer o cadastro",
            command=pagina_cad,
        )
        self.botao_cad.pack()
        self.janela_main.mainloop()


win_main = Win_main()
