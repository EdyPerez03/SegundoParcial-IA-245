import cx_Oracle
from flask import Flask, render_template, request

usuario = 'CONCESIONARIO'      
clave = '123'                   
host = 'localhost'             
puerto = '1521'                
sid = 'xe'                   
dsn = cx_Oracle.makedsn(host, puerto, sid)  
conexion_str = f"{usuario}/{clave}@{dsn}"

app = Flask(__name__)

def buscar_comparativa(precio_min, precio_max):
    try:
        connection = cx_Oracle.connect(conexion_str)
        cursor = connection.cursor()
        
        query = '''
            SELECT id_auto, modelo, descripcion, precio, stock
            FROM Autos
            WHERE precio BETWEEN : precio_min AND :precio_max
            ORDER BY precio
        '''
        cursor.execute(query, {'precio_min': precio_min, 'precio_max': precio_max})
        resultados = cursor.fetchall()
        
        for i in range(len(resultados)):
            descripcion = resultados[i][2]
            if isinstance(descripcion, cx_Oracle.LOB):  
                resultados[i] = list(resultados[i])  
                resultados[i][2] = descripcion.read()  

        cursor.close()
        connection.close()
        return resultados
    except cx_Oracle.DatabaseError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return []


@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    if request.method == 'POST':
        precio_min = float(request.form['precio_min'])
        precio_max = float(request.form['precio_max'])
        resultados = buscar_comparativa(precio_min, precio_max)
    
    return render_template('autos.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
