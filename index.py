from tkinter import *
from tkinter import ttk
from tkinter import messagebox as message
import consultas
class app:
	def __init__(self, windows):
		self.wind = windows
		self.wind.title("CRUD Tabla")
		self.query = consultas.query()
		#Frame Label
		frame = LabelFrame(self.wind, text="Agregar")
		frame.grid(row=0, column=0, columnspan=3,ipadx=20)
		Label(frame,text="Nombre Empresa: ").grid(row=1, column=1)
		self.nombre = Entry(frame)
		self.nombre.grid(row=1, column=2, pady=5)

		Label(frame,text="Tipo Empresa: ").grid(row=2, column=1)
		self.tipo = ttk.Combobox(frame, values = ["Publico", "Privado"])
		self.tipo.current(0)
		self.tipo.grid(row=2, column=2, pady=5)

		#Btn enviar
		ttk.Button(frame, text="Guardar", command= self.guardar).grid(row=3, columnspan=3, sticky=W + E)


		#CReacion de la Tabla
		self.tabla0 = ttk.Treeview(height=10, column=("#0", "#1", "#2"))
		self.tabla0.grid(row=4, column=0, columnspan=2)
		self.tabla0.heading("#0",text="Id",anchor='center')
		self.tabla0.heading("#1",text="Nombre Empresa",anchor='center')
		self.tabla0.heading("#2",text="Tipo Empresa",anchor='center')
		
		self.mostrar()
		#Btn
		ttk.Button(text="Eliminar", command=self.eliminar).grid(row=5, column = 0, sticky = W + E)
		ttk.Button(text="Editar",command=self.actualizar).grid(row=5, column = 1, sticky = W + E)
	
	def guardar(self):
		nombre = self.nombre.get()
		tipo = self.tipo.get()
		if(nombre !='' and tipo !=''):
			self.query.save(nombre,tipo)
			message.showinfo(message="Datos almacenados", title="Guardados")
			self.nombre.delete(0,END)
			self.tipo.delete(0,END)

			self.mostrar()
		else:
			message.showinfo(message="Ingrese los datos", title="Por favor")
	
	def mostrar(self):
		delete = self.tabla0.get_children()
		for elemento in delete:
			self.tabla0.delete(elemento)
		rows = self.query.read()
		print(rows)
		for row in rows:
			print(row)
			self.tabla0.insert( parent='', index=0,text=row[0], values=row[1:])
	
	def eliminar(self):
		try:
			id_empresa = self.tabla0.item(self.tabla0.selection())['text']
			self.query.delete(id_empresa)
			self.mostrar()
		except IndexError:
			message.showinfo(message="Por favor selecciona un dato de la tabla", title="Error")

	def actualizar(self):
		try:
			self.previous_id_empresa = self.tabla0.item(self.tabla0.selection())['text']
			self.previous_nombre_empresa = self.tabla0.item(self.tabla0.selection())['values'][0]
			self.previous_tipo_empresa = self.tabla0.item(self.tabla0.selection())['values'][1]
			nombre_empresa = StringVar()
			tipo_empresa  = StringVar()
			nombre_empresa.set(self.previous_nombre_empresa)
			print(self.previous_tipo_empresa)
			tipo_empresa.set(self.previous_tipo_empresa)
			self.edit_window = Toplevel()
			self.edit_window.title("Actualizar")
			frame = LabelFrame(self.edit_window, text='Actualizar')
			frame.grid(row=0, column=0, ipadx=20)
			Label(frame, text="Nombre Empresa: ").grid(row=1, column=1)
			self.new_id = Entry(frame, textvar=nombre_empresa)
			self.new_nombre = Entry(frame, textvar=nombre_empresa)
			self.new_nombre.grid(row=1,column=2,ipadx=20)

			Label(frame, text='Tipo Empresa: ').grid(row=2, column=1)
			self.new_tipo = ttk.Combobox(frame, values = ["Publico", "Privado"])
			if (self.previous_tipo_empresa =="Publico"):
				self.new_tipo.current(0)
			else:
				self.new_tipo.current(1)
			
			self.new_tipo.grid(row=2, column=2, pady=5)

			ttk.Button(frame, text="Guardar", command=self.edit).grid(row=3, columnspan=2, sticky=W + E)
		except IndexError:
			message.showinfo(message="Por favor selecciona un dato de la tabla", title="Error")
			
	def edit(self):
		self.id_empresa = self.previous_id_empresa
		self.nombre_empresa=self.new_nombre.get()
		self.tipo_empresa = self.new_tipo.get()

		if(self.nombre_empresa !='' and self.tipo_empresa !=''):
			self.query.update(self.nombre_empresa,self.tipo_empresa,self.id_empresa)
			self.mostrar()
			self.edit_window.destroy()
if __name__=="__main__":
	root = Tk()
	Aplicacion = app(root)
	root.mainloop()