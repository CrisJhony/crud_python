import sqlite3

class query():
	def __init__(self):
		self.db = "database.db"
	def ejecutar_consultar(self,sql,parametros=()):
		with sqlite3.connect(self.db) as conn:
			cursor = conn.cursor()
			result = cursor.execute(sql,parametros)
			conn.commit()
			return result

	def save(self,nombre,tipo):
		sql = "INSERT INTO TBL_EMPRESA('nombre_empresa', 'tipo_empresa' ) VALUES(?,?)"
		parametros =(nombre,tipo)
		self.ejecutar_consultar(sql, parametros)

	def read(self):
		sql = "SELECT * FROM TBL_EMPRESA ORDER BY id_empresa DESC"
		results = self.ejecutar_consultar(sql)
		return results
		
	def delete(self,id_empresa):
		sql = "DELETE FROM TBL_EMPRESA WHERE id_empresa=?"
		parametros = (id_empresa,)
		results = self.ejecutar_consultar(sql,parametros)

	def update(self,nombre_nuevo,tipo_nuevo,id_empresa):#Le pasamos los 4 parametros para actualizar el registro
		sql = "UPDATE TBL_EMPRESA SET nombre_empresa=?,tipo_empresa=? WHERE id_empresa=?"
		parametros = (nombre_nuevo,tipo_nuevo,id_empresa)
		self.ejecutar_consultar(sql,parametros)
	
