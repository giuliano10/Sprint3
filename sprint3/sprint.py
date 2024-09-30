import random
import tkinter as tk
from tkinter import messagebox

# Lista para armazenar resultados intermediários e resultados em matriz
resultados_intermediarios = []
resultados_matriz = []

# Função para armazenar os resultados intermediários
def armazenar_resultado(sessao, tempo):
    precisao = random.uniform(10.0, 100.0)  
    erros = random.randint(0, 20)  
    
    resultado = {
        'sessao': sessao,
        'tempo': tempo,
        'precisao': precisao,
        'erros': erros
    }
    resultados_intermediarios.append(resultado)

# Função para registrar as métricas na matriz
def registrar_metrica(sessao, tempo):
    precisao = random.uniform(10.0, 100.0)
    erros = random.randint(0, 20)
    
    resultados_matriz.append([sessao, tempo, precisao, erros])

# Função para salvar resultados em um arquivo .txt
def salvar_resultados():
    with open("resultados_simulacao.txt", "w") as file:
        file.write("Resultados intermediários:\n")
        for resultado in resultados_intermediarios:
            file.write(f"{resultado}\n")
        
        file.write("\nResultados em matriz:\n")
        for resultado in resultados_matriz:
            file.write(f"{resultado}\n")
        
        if resultados_intermediarios:
            media_tempo = sum(resultado['tempo'] for resultado in resultados_intermediarios) / len(resultados_intermediarios)
            media_precisao = sum(resultado['precisao'] for resultado in resultados_intermediarios) / len(resultados_intermediarios)
            total_erros = sum(resultado['erros'] for resultado in resultados_intermediarios)
            
            file.write(f"\nMédia de tempo: {media_tempo:.2f} segundos\n")
            file.write(f"Média de precisão: {media_precisao:.2f}%\n")
            file.write(f"Total de erros: {total_erros}\n")

    messagebox.showinfo("Salvo", "Os resultados foram salvos em 'resultados_simulacao.txt'.")

# Função para a tela de login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "admin" and senha == "12345":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        janela_login.destroy()  # Fechar a tela de login
        iniciar_simulacao_janela()  # Chama a função que cria a janela de simulação
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para criar a janela de simulação
def iniciar_simulacao_janela():
    global entry_sessao, entry_tempo, text_resultados
    
    janela_simulacao = tk.Tk()
    janela_simulacao.title("Simulação de Treinamento")

    # Widgets de entrada para a simulação
    tk.Label(janela_simulacao, text="Número da Sessão:").grid(row=0, column=0)
    entry_sessao = tk.Entry(janela_simulacao)
    entry_sessao.grid(row=0, column=1)

    tk.Label(janela_simulacao, text="Tempo da Simulação (segundos):").grid(row=1, column=0)
    entry_tempo = tk.Entry(janela_simulacao)
    entry_tempo.grid(row=1, column=1)

    # Botão para registrar métricas
    btn_registrar = tk.Button(janela_simulacao, text="Registrar Métricas", command=iniciar_simulacao)
    btn_registrar.grid(row=2, column=0, columnspan=2)

    # Text box para exibir resultados
    text_resultados = tk.Text(janela_simulacao, width=60, height=20)
    text_resultados.grid(row=3, column=0, columnspan=2)

    # Botão para salvar os resultados
    btn_salvar = tk.Button(janela_simulacao, text="Salvar Resultados", command=salvar_resultados)
    btn_salvar.grid(row=4, column=0, columnspan=2)

# Função para iniciar a simulação e exibir resultados
def iniciar_simulacao():
    try:
        sessao = int(entry_sessao.get())
        tempo = float(entry_tempo.get())
        
        armazenar_resultado(sessao, tempo)
        registrar_metrica(sessao, tempo)
        
        # Exibir os resultados intermediários e da matriz
        text_resultados.delete(1.0, tk.END)
        text_resultados.insert(tk.END, "Resultados intermediários:\n")
        for resultado in resultados_intermediarios:
            text_resultados.insert(tk.END, f"{resultado}\n")
        
        text_resultados.insert(tk.END, "\nResultados em matriz:\n")
        for resultado in resultados_matriz:
            text_resultados.insert(tk.END, f"{resultado}\n")
        
        # Exibir as médias e total de erros
        if resultados_intermediarios:
            media_tempo = sum(resultado['tempo'] for resultado in resultados_intermediarios) / len(resultados_intermediarios)
            media_precisao = sum(resultado['precisao'] for resultado in resultados_intermediarios) / len(resultados_intermediarios)
            total_erros = sum(resultado['erros'] for resultado in resultados_intermediarios)
            
            text_resultados.insert(tk.END, f"\nMédia de tempo: {media_tempo:.2f} segundos\n")
            text_resultados.insert(tk.END, f"Média de precisão: {media_precisao:.2f}%\n")
            text_resultados.insert(tk.END, f"Total de erros: {total_erros}\n")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")

# Criar a janela de login
janela_login = tk.Tk()
janela_login.title("Login")

# Widgets de login
tk.Label(janela_login, text="Usuário:").grid(row=0, column=0)
entry_usuario = tk.Entry(janela_login)
entry_usuario.grid(row=0, column=1)

tk.Label(janela_login, text="Senha:").grid(row=1, column=0)
entry_senha = tk.Entry(janela_login, show="*")
entry_senha.grid(row=1, column=1)

# Botão de login
btn_login = tk.Button(janela_login, text="Login", command=verificar_login)
btn_login.grid(row=2, column=0, columnspan=2)

# Exibir a tela de login
janela_login.mainloop()
