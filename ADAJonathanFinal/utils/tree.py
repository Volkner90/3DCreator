from .baseClass import node


def writetofile(filename, string):
    file = open(filename, "a")
    file.write(string)
    file.close()


def createtree(nodes, filename):
    if(len(nodes) == 0):
        print("No se detectan formas")
        return

    subtree = []
    string = ''
    # Initializar el nodo raiz
    present = node()
    # Agregar el nodo al hijo izquierdo
    present.left = nodes[0]
    nodes[0].name()
    # Agregar el string generado al nodo actual
    present.string = nodes[0].string
    # Si solo hay un nodo,lo agregamos al archivo
    if(len(nodes) == 1):
        writetofile(filename, present.string)
    #Si el numero de nodos es mas de uno entramos a iterar
    for i, object in enumerate(nodes[1:]):
        # Generamos la funcion para la forma en openscad
        object.name()
        # Si el nodo es hijo de la forma
        if(object.operation != 'None'):
            # Si el hijo izquierdo esta disponible
            if(present.right == 'None'):
                # Le asignamos el padre derecho
                present.right = object
                # actualizamos el string
                present.string = object.operation + \
                    "() {\n\t" + present.string + \
                    '\n\t' + object.string + '}\n'
                # se almacena para concatenar
                string = present.string
            else:
                # Si el nodo derecho no esta libre, se crea uno nuevo y el anterior pasa a ser un hijo izquierdo
                temp = present
                present = node()
                present.left = temp
                present.string = temp.string
                # Se queda el actual como hijo derecho del nuevo nodo
                present.right = object
                # actualizamos el string
                present.string = object.operation + \
                    "() {\n\t" + present.left.string + \
                    '\n\t' + object.string + '}\n'
                
                string = present.string
        else:
            # Solo cuando hay 2 padres sin hijos consecutivos
            if(present.right == 'None'):
                # concatenamos el string
                writetofile(filename, present.string)

            # Recorremos la lista y si crean los subarboles
            subtree.append(present)
            writetofile(filename, string)
            # se crea un nuevo subarbol
            string = ''
            present = node()
            present.left = object
            present.string = object.string
            # si el ultimo nodo es un padre
            if(i == len(nodes)-2):
                writetofile(filename, present.string)
    # si es un hijo
    if(string != ''):
        writetofile(filename, string)
    # añadimos los subarboles
    subtree.append(present)
    print("Subtree:", len(subtree))
