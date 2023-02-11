import firebase_admin
import json
from firebase_admin import db
from firebase_admin import credentials

#Obtenemos la secret key de la plataforma de firebase

SECRET_KEY = 'serviceAccountKey.json'

#creamos un objeto que cargarà el certificado de la secret key
cred = credentials.Certificate(SECRET_KEY)

#inicializamos la app de la plataforma pasando como paràmetros al mètodo de abajo, el objeto instanciado "cred" y un diccionario con la key 'databaseURL' y el value serà la direcciòn de la base de datos en tiempo real que nos ofrece firebase

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bookstoreproject-bd253-default-rtdb.firebaseio.com'
})

#Importamos el modulo db para realizar una ruta donde crearemos nuestra db e indicamos dentro de ella la ruta.

ref = db.reference('/Books')

#Creamos un archivo json para este caso, con una serie de libros e importamos el modulo json para poder leerlo y guardarlo en file_contents.
with open("books.json", "r") as f:
	file_contents = json.load(f)

#Finalmente usamos el mètodo set para cargar el json leìdo a las base de datos en tiempo real.

ref.set(file_contents)

ref = db.reference('/Books/Best_Sellers')


for key, value in file_contents.items():
    ref.push().set(value)

best_sellers = ref.get()

for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		value["Price"] = 90
		ref.child(key).update({"Price":80})




