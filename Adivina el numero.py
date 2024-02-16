import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivinanza:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Adivina el número")
        self.ventana.geometry("500x500")
        self.ventana.configure(bg="#1e272e")  # Azul oscuro grisáceo

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.pistas_utilizadas = 0

        self.etiqueta_instruccion = tk.Label(ventana, text="Estoy pensando en un número entre 1 y 100.", bg="#1e272e", fg="#dcdde1", font=("Arial", 12))
        self.etiqueta_instruccion.pack(pady=10)

        self.entrada_numero = tk.Entry(ventana, font=("Arial", 12), width=10)
        self.entrada_numero.pack(pady=5)

        self.boton_adivinar = tk.Button(ventana, text="Adivinar", bg="#2ecc71", fg="white", font=("Arial", 12), command=self.verificar_numero)
        self.boton_adivinar.pack(pady=5)

        self.etiqueta_intentos = tk.Label(ventana, text="", bg="#1e272e", fg="#dcdde1", font=("Arial", 12))
        self.etiqueta_intentos.pack(pady=10)

        self.etiqueta_estado = tk.Label(ventana, text="", bg="#1e272e", fg="#dcdde1", font=("Arial", 12))
        self.etiqueta_estado.pack(pady=10)

        self.boton_pista = tk.Button(ventana, text="Obtener Pista", bg="#3498db", fg="white", font=("Arial", 12), command=self.obtener_pista)
        self.boton_pista.pack(pady=5)

        self.etiqueta_pistas = tk.Label(ventana, text="", bg="#1e272e", fg="#dcdde1", font=("Arial", 12))
        self.etiqueta_pistas.pack(pady=10)

        self.boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", bg="#e74c3c", fg="white", font=("Arial", 12), command=self.reiniciar_juego)
        self.boton_reiniciar.pack(pady=5)

        self.boton_salir = tk.Button(ventana, text="Salir", bg="#bdc3c7", fg="black", font=("Arial", 12), command=ventana.quit)
        self.boton_salir.pack(pady=5)

        self.etiqueta_ayuda = tk.Label(ventana, text=f"¡Pista! El número está entre {max(1, self.numero_secreto - 10)} y {min(100, self.numero_secreto + 10)}.", bg="#1e272e", fg="#dcdde1", font=("Arial", 12))
        self.etiqueta_ayuda.pack(pady=10)

    def verificar_numero(self):
        suposicion = self.entrada_numero.get()
        if suposicion.isdigit():
            suposicion = int(suposicion)
            self.intentos += 1

            if suposicion < self.numero_secreto:
                self.etiqueta_estado.config(text="Demasiado bajo. ¡Inténtalo de nuevo!")
            elif suposicion > self.numero_secreto:
                self.etiqueta_estado.config(text="Demasiado alto. ¡Inténtalo de nuevo!")
            else:
                messagebox.showinfo("Adivina el número", f"¡Felicidades! Adivinaste el número en {self.intentos} intentos.")
                self.reiniciar_juego()
        else:
            messagebox.showerror("Adivina el número", "Por favor, introduce un número válido.")

        self.actualizar_intentos()

    def obtener_pista(self):
        self.pistas_utilizadas += 1
        if self.pistas_utilizadas == 1:
            min_range = max(1, self.numero_secreto - 10)
            max_range = min(100, self.numero_secreto + 10)
            messagebox.showinfo("Pista", f"El número está entre {min_range} y {max_range}.")
        elif self.pistas_utilizadas == 2:
            last_digit = self.numero_secreto % 10
            messagebox.showinfo("Pista", f"El último dígito del número es {last_digit}.")
            self.boton_pista.config(state="disabled")
        self.etiqueta_pistas.config(text=f"Pistas utilizadas: {self.pistas_utilizadas}")

    def actualizar_intentos(self):
        self.etiqueta_intentos.config(text=f"Intentos: {self.intentos}")

    def reiniciar_juego(self):
        respuesta = messagebox.askyesno("Adivina el número", "¿Quieres jugar de nuevo?")
        if respuesta:
            self.numero_secreto = random.randint(1, 100)
            self.intentos = 0
            self.pistas_utilizadas = 0
            self.etiqueta_intentos.config(text="")
            self.etiqueta_estado.config(text="")
            self.etiqueta_pistas.config(text="")
            self.etiqueta_ayuda.config(text=f"¡Pista! El número está entre {max(1, self.numero_secreto - 10)} y {min(100, self.numero_secreto + 10)}.")
            self.boton_pista.config(state="active")
        else:
            self.ventana.quit()

ventana_principal = tk.Tk()
juego = JuegoAdivinanza(ventana_principal)
ventana_principal.mainloop()


