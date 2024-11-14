import tkinter as tk
from tkinter import messagebox

def fibonacci(n):
    """Gera a sequência de Fibonacci até o enésimo termo."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def mostrar_fibonacci():
    """Obtém o número do usuário e exibe a sequência de Fibonacci."""
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError("O número deve ser não negativo.")
        seq = fibonacci(n)
        resultado_var.set(", ".join(map(str, seq)))
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sequência de Fibonacci")

# Alterando o fundo da janela principal
root.config(bg="#f0f8ff")

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

# Alterando a cor do texto do label
label = tk.Label(frame, text="Digite um número:", font=("Helvetica", 12, "bold"), bg="#f0f8ff", fg="#2e8b57")
label.pack()

# Configurando a caixa de entrada com borda arredondada e cor suave
entry = tk.Entry(frame, font=("Helvetica", 12), width=15, bd=2, relief="solid", fg="#333", bg="#e0f7fa")
entry.pack(pady=5)

# Configurando o botão com cor de fundo chamativa e bordas arredondadas
botao = tk.Button(frame, text="Mostrar Fibonacci", font=("Helvetica", 12, "bold"), command=mostrar_fibonacci, 
                  bg="#32cd32", fg="#fff", relief="raised", padx=10, pady=5)
botao.pack(pady=10)

# Alterando a aparência do label do resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(frame, textvariable=resultado_var, font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
resultado_label.pack()

root.mainloop()
