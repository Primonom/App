from ttkbootstrap import ttk

def create_section(parent, title, buttons, danger=False):
    frame = ttk.Frame(parent, padding=20, bootstyle="secondary")
    frame.pack_propagate(False)
    frame.grid_propagate(False)

    # Título da seção
    ttk.Label(frame, text=title, font=("Arial", 16, "bold"), anchor="center").pack(pady=10)

    # Adicionar botões
    for text, command in buttons:
        style = "danger.TButton" if danger else "success.Outline.TButton"
        ttk.Button(frame, text=text, command=command, style=style).pack(pady=10, ipadx=10, ipady=5, fill='x')

    return frame