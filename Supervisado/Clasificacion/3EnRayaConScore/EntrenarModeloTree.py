#!/usr/bin/python3

#Biblioteca para usar JSON
import json
#Biblioteca para modelos tipo "arbol"
from sklearn import tree
#Biblioteca para importar/exportar modelo entrenado
import joblib
#Biblioteca para realizar operaciones de sistema
import sys

#MAIN
#Si hay un segundo argumento, lo tomamos como el numero del JSON a leer (y modelo a entrenar)
if len(sys.argv)==2:
    numPart=int(sys.argv[1])
#Si no ponemos valor por defecto, tomamos valor 1000
else:
    numPart=1000
    
print("Entrenando Arbol con modelo de "+str(numPart)+" partidas")

#Cargamos el JSON de las partidas generadas
with open('../data'+str(numPart)+'.json') as file:
    data = json.load(file)


#En base a las partidas, creamos una lista de las features que queremos para cada ejemplo
# Ahi metemos los elementos de la partida del 0 al 10
features=[]
for i in range(len(data)):
    features.append(data[i][:11])
#En base a cada partida, creamos una etiqueta con el valor almacenado en la posicion 11
#0 Derrota, 1 Victoria
labels=[]
for i in range(len(data)):
    labels.append(data[i][11])

#Creamos clasificador basado en arbol de decision https://en.wikipedia.org/wiki/Decision_tree_learning
classif = tree.DecisionTreeClassifier()
#Entrenamos el clasificador
classif.fit(features, labels)

#Salvamos el modelo entrenado
joblib.dump(classif, 'modelTree3EnRaya'+str(numPart)+'.pkl') 

print('Salvamos el modelo en :modelTree3EnRaya'+str(numPart)+'.pkl') 


#Comentado, para probar rapido el clasificador, la probabilidad y imprimir el arbol
# print (classif.predict([[0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 1]]))
# print (classif.predict_proba([[0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 1]]))
# Para obtener el arbol asociado
#textoTree = tree.export_text(classif)
#print(textoTree)
