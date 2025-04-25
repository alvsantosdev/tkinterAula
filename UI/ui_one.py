import tkinter as tk

def salvarNome():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome and endereco:
        with open("nomes.txt", "a") as arquivo:
            arquivo.write(nome)
            arquivo.write(endereco + "\n") 
        label_status.config(text = f'Nome "{nome}" | Endereço: {endereco}" salvos com sucesso', fg ="green")
    else:
        label_status.config(text="Digite um nome. ", fg ="red" )
        label_status.config(text="Digite um Endereço", fg="red")

root = tk.  Tk()
root.title("Nomes")
root.geometry("300x400")

Label_instrucaoN = tk.Label(root, text ="Digite um nome:")
Label_instrucaoN.pack(pady = 10)

Label_instrucaoE = tk.Label(root, text="Digite um endereco")
Label_instrucaoE.pack(pady = 10)

entry_endereco = tk.Entry(root)
entry_endereco.pack(pady =  5)

entry_nome = tk.Entry(root)
entry_nome.pack(pady = 5)

botao_salvar = tk.Button(root, text="Salvar", command = salvarNome)
botao_salvar.pack(pady = 10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)
root.mainloop()

