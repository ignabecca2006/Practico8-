
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from conexion import conectar 

# Configuración de apariencia
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Ventana principal
app = ctk.CTk()
app.title("Práctico 8 - Registro de Pacientes")
app.geometry("650x650")
app.resizable(False, False)

# Título
titulo = ctk.CTkLabel(
    app,
    text="Registro de Pacientes",
    font=("Arial", 26, "bold")
)
titulo.pack(pady=25)

# Contenedor del formulario
formulario = ctk.CTkFrame(app)
formulario.pack(padx=30, pady=10, fill="both", expand=True)

# ID
ctk.CTkLabel(formulario, text="ID del paciente:").pack(pady=(15, 5))
entrada_id = ctk.CTkEntry(
    formulario,
    width=300,
    placeholder_text="Ingrese el ID"
)
entrada_id.pack()

# Nombre
ctk.CTkLabel(formulario, text="Nombre completo:").pack(pady=(15, 5))
entrada_nombre = ctk.CTkEntry(
    formulario,
    width=300,
    placeholder_text="Ingrese el nombre"
)
entrada_nombre.pack()

# Fecha de nacimiento
ctk.CTkLabel(formulario, text="Fecha de nacimiento:").pack(pady=(15, 5))
entrada_fecha = ctk.CTkEntry(
    formulario,
    width=300,
    placeholder_text="DD/MM/AAAA"
)
entrada_fecha.pack()

# Sexo
ctk.CTkLabel(formulario, text="Sexo:").pack(pady=(15, 5))
combo_sexo = ctk.CTkComboBox(
    formulario,
    width=300,
    values=["Masculino", "Femenino", "Otro"],
    state="readonly"
)
combo_sexo.pack()
combo_sexo.set("Masculino")

# Donador de órganos
check_donador = ctk.CTkCheckBox(
    formulario,
    text="Donador de órganos"
)
check_donador.pack(pady=20)

# Cobertura médica
ctk.CTkLabel(
    formulario,
    text="Tipo de cobertura médica:"
).pack(pady=(5, 10))

tipo_cobertura = ctk.StringVar(value="Particular")

radio_particular = ctk.CTkRadioButton(
    formulario,
    text="Particular",
    variable=tipo_cobertura,
    value="Particular"
)
radio_particular.pack(pady=5)

radio_obra_social = ctk.CTkRadioButton(
    formulario,
    text="Obra social",
    variable=tipo_cobertura,
    value="Obra social"
)
radio_obra_social.pack(pady=5)

# Funciones de los botones

def guardar():
    try:
        # 1. Obtener los datos del formulario
        id_paciente = int(entrada_id.get())
        nombre = entrada_nombre.get().strip()
        fecha = datetime.strptime(
            entrada_fecha.get(), "%d/%m/%Y"
        ).date()
        sexo = combo_sexo.get()
        donador = check_donador.get()
        cobertura = tipo_cobertura.get()

        # 2. Validar el nombre
        if not nombre:
            messagebox.showwarning(
                "Datos incompletos",
                "Debe ingresar el nombre del paciente."
            )
            return

        # 3. Conectarse con SQL Server
        conexion = conectar()

        try:
            cursor = conexion.cursor()

            # 4. Insertar el paciente
            cursor.execute("""
                INSERT INTO Pacientes
                (id, nombre, fecha_nacimiento,
                 sexo, donador_organos, cobertura)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                id_paciente,
                nombre,
                fecha,
                sexo,
                donador,
                cobertura
            ))

            # 5. Confirmar los cambios
            conexion.commit()

        finally:
            conexion.close()

        # 6. Mostrar mensaje de éxito
        messagebox.showinfo(
            "Éxito",
            "Paciente guardado correctamente."
        )

        # 7. Limpiar el formulario
        cancelar()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Verifique el ID y la fecha (DD/MM/AAAA)."
        )

    except Exception as error:
        messagebox.showerror(
            "Error al guardar",
            str(error)
        )



def cancelar():
    entrada_id.delete(0, "end")
    entrada_nombre.delete(0, "end")
    entrada_fecha.delete(0, "end")
    combo_sexo.set("Masculino")
    check_donador.deselect()
    tipo_cobertura.set("Particular")


# Contenedor de botones
botones = ctk.CTkFrame(formulario, fg_color="transparent")
botones.pack(pady=20)

boton_guardar = ctk.CTkButton(
    botones,
    text="Guardar",
    command=guardar
)
boton_guardar.pack(side="left", padx=10)

boton_cancelar = ctk.CTkButton(
    botones,
    text="Cancelar",
    fg_color="gray",
    command=cancelar
)
boton_cancelar.pack(side="left", padx=10)

# Ejecutar aplicación
app.mainloop()
