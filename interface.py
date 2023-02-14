# HOME: apresenta os botões para sub-telas (sobre, sobreNBA e tabela da NBA).
# SOBRE: apresenta informações sobre o projeto.
# SOBRENBA: apresenta informações e curiosidades sobre a NBA.
# TABELAS: apresenta os botões para sub-telas (NBAC e NBAG)
# NBAC: apresenta a tabela com base nas conferências (a OESTE) e o botão para NBAC1.
# NBAC1: apresenta a tabela com base nas conferências (a LESTE) e o botão para NBAC.
# NBAG: apresenta a tabaela geral da NBA.

import tkinter as tk

def main():
    def irSOBRE():
        home.destroy()
        sobre()    
        
    def irSOBRENBA():
        home.destroy()
        sobreNBA()   
         
    def irTABELAS():
        home.destroy()
        tabelas()    
        
    def irTABELASC():
        home.destroy()
        tabelaNBAC()    
        
    def irTABELASC1():
        home.destroy()
        tabelaNBAC1()    
        
    def irTABELASG():
        home.destroy()
        tabelaNBAG()    
        
    home = tk.Tk()
    home.geometry('600x300')
    home.wm_iconbitmap('nba.ico')
    home.resizable(False, False)
    home.title("TABELANBA05 | HOME")
    # conteúdo:
    tk.Label(master=home, text="TABELANBA05", font=('Montserrat', 20)).place(x=200, y= 5) # titulo
    tk.Label(master=home, text="O que deseja fazer hoje?", font=('Montserrat', 18)).place(x=50, y=50) # subtitulo
    tk.Button(fg="white", master=home, font=('Montserrat', 18), background="red", text="SOBRE TABELANBA05", command=irSOBRE).place(x=40, y=150) # botao para realizar acao1.1
    tk.Button(fg="white", master=home, font=('Montserrat', 18), background="red", text="SOBRE NBA", command=irSOBRENBA).place(x=320, y=150) # botao para realizar acao1.1
    tk.Button(fg="white", master=home, font=('Montserrat', 20), background="red", text="TABELAS DA NBA", command=irTABELAS).place(x=120, y=220) # botao para realizar acao2
    home.mainloop()
def sobre():
    def irCASA():
        sobre.destroy()
        casa()
    sobre = tk.Tk()
    sobre.geometry('600x300')
    sobre.wm_iconbitmap('nba.ico')
    sobre.resizable(False, False)
    sobre.title("TABELANBA05 | sobre")
    tk.Button(fg="white", master=sobre, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="SOBRE").place(x=450, y=10)
    sobre.mainloop()

def sobreNBA():
    def irCASA():
        sobreNBA.destroy()
        casa()
    sobreNBA = tk.Tk()
    sobreNBA.geometry('600x300')
    sobreNBA.wm_iconbitmap('nba.ico')
    sobreNBA.resizable(False, False)
    sobreNBA.title("TABELANBA05 | sobreNBA")
    tk.Button(fg="white", master=sobreNBA, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="SOBRE NBA").place(x=400, y=10)
    sobreNBA.mainloop()

def tabelas():
    def irCASA():
        tabelas.destroy()
        casa()
    tabelas = tk.Tk()
    tabelas.geometry('600x300')
    tabelas.wm_iconbitmap('nba.ico')
    tabelas.resizable(False, False)
    tabelas.title("TABELANBA05 | tabelas")
    tk.Button(fg="white", master=tabelas, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="TABELAS").place(x=450, y=10)
    tabelas.mainloop()

def tabelaNBAC():
    def irCASA():
        tabelaNBAC.destroy()
        casa()
    tabelaNBAC = tk.Tk()
    tabelaNBAC.geometry('600x300')
    tabelaNBAC.wm_iconbitmap('nba.ico')
    tabelaNBAC.resizable(False, False)
    tabelaNBAC.title("TABELANBA05 | tabela conferencia")
    tk.Button(fg="white", master=tabelaNBAC, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="TABELAS NBAC").place(x=450, y=10)
    tabelaNBAC.mainloop()

def tabelaNBAC1():
    def irCASA():
        tabelaNBAC1.destroy()
        casa()
    tabelaNBAC1 = tk.Tk()
    tabelaNBAC1.geometry('600x300')
    tabelaNBAC1.wm_iconbitmap('nba.ico')
    tabelaNBAC1.resizable(False, False)
    tabelaNBAC1.title("TABELANBA05 | tabela conferencia1")
    tk.Button(fg="white", master=tabelaNBAC1, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="TABELAS NBAC1").place(x=450, y=10)
    tabelaNBAC1.mainloop()

def tabelaNBAG():
    def irCASA():
        tabelaNBAG.destroy()
        casa()
    tabelaNBAG = tk.Tk()
    tabelaNBAG.geometry('600x300')
    tabelaNBAG.wm_iconbitmap('nba.ico')
    tabelaNBAG.resizable(False, False)
    tabelaNBAG.title("TABELANBA05 | tabela geral")
    tk.Button(fg="white", master=tabelaNBAG, font=('Montserrat', 20), background="red", text="VOLTAR A HOME", command=irCASA).place(x=10, y=10)
    tk.Label(font=('Montserrat', 20), text="TABELAS NBAG").place(x=450, y=10)
    tabelaNBAG.mainloop()

def casa():
    def irSOBRE():
        home.destroy()
        sobre()    
        
    def irSOBRENBA():
        home.destroy()
        sobreNBA()   
         
    def irTABELAS():
        home.destroy()
        tabelas()   
    home = tk.Tk()
    home.geometry('600x300')
    home.wm_iconbitmap('nba.ico')
    home.resizable(False, False)
    home.title("TABELANBA05 | HOME")

    # conteúdo:
    tk.Label(master=home, text="TABELANBA05", font=('Montserrat', 20)).place(x=200, y= 5) # titulo
    tk.Label(master=home, text="O que deseja fazer hoje?", font=('Montserrat', 18)).place(x=50, y=50) # subtitulo
    tk.Button(fg="white", master=home, font=('Montserrat', 18), background="red", text="SOBRE TABELANBA05", command=irSOBRE).place(x=40, y=150) # botao para realizar acao1.1
    tk.Button(fg="white", master=home, font=('Montserrat', 18), background="red", text="SOBRE NBA", command=irSOBRENBA).place(x=320, y=150) # botao para realizar acao1.1
    tk.Button(fg="white", master=home, font=('Montserrat', 20), background="red", text="TABELAS DA NBA", command=irTABELAS).place(x=120, y=220) # botao para realizar acao2
    home.mainloop()

main()