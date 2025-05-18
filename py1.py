import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Función para calcular el producto punto
def producto_punto(vec1, vec2):
    return np.dot(vec1, vec2)

# Función para calcular la similitud del coseno
def cosine_similarity(vec1, vec2):
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0
    return np.dot(vec1, vec2) / (norm1 * norm2)

# Parámetros
np.random.seed(42)
num_usuarios = 3
num_contenidos = 4
dim = 2  # Cambia a 2 para graficar

usuarios = {f'Usuario {i+1}': np.random.randint(0, 6, dim) for i in range(num_usuarios)}
contenidos = {f'Contenido {chr(65+i)}': np.random.randint(0, 6, dim) for i in range(num_contenidos)}

# Mostrar vectores generados
print("Vectores de usuarios:")
for nombre, vec in usuarios.items():
    print(f"  {nombre}: {vec}")

print("\nVectores de contenidos:")
for nombre, vec in contenidos.items():
    print(f"  {nombre}: {vec}")

# Mostrar recomendaciones por usuario
for usuario, vec_usuario in usuarios.items():
    print(f"\nRecomendaciones para {usuario}:")
    similitudes = {}
    for contenido, vec_contenido in contenidos.items():
        prod_punto = producto_punto(vec_usuario, vec_contenido)
        similitud = cosine_similarity(vec_usuario, vec_contenido)
        print(f"  {contenido}: producto punto = {prod_punto}, similitud coseno = {similitud:.2f}")
        similitudes[contenido] = similitud
    
    # Ordenar de mayor a menor similitud
    recomendaciones = sorted(similitudes.items(), key=lambda x: x[1], reverse=True)
    print("  Orden de recomendación:")
    for contenido, score in recomendaciones:
        print(f"    {contenido}: similitud = {score:.2f}", end='')
        if score > 0.7:
            print(" → Contenido recomendado")
        else:
            print()
    # Validación automática: mejor contenido
    mejor_contenido, mejor_score = recomendaciones[0]
    print(f"  Mejor recomendación para {usuario}: {mejor_contenido} (similitud = {mejor_score:.2f})")

# Graficar si la dimensión es 2
if dim == 2:
    colors = ['r', 'g', 'b', 'c', 'm', 'y']
    plt.figure(figsize=(7, 7))
    # Graficar usuarios
    for i, (nombre, vec) in enumerate(usuarios.items()):
        plt.arrow(0, 0, vec[0], vec[1], head_width=0.2, color='r', length_includes_head=True)
        plt.text(vec[0]+0.1, vec[1]+0.1, nombre, fontsize=12, color='r')
    # Graficar contenidos
    for i, (nombre, vec) in enumerate(contenidos.items()):
        plt.arrow(0, 0, vec[0], vec[1], head_width=0.2, color='c', linestyle='dashed', length_includes_head=True)
        plt.text(vec[0]+0.1, vec[1]+0.1, nombre, fontsize=12, color='c')
    # Leyenda
    user_patch = mpatches.Patch(color='r', label='Usuarios')
    content_patch = mpatches.Patch(color='c', label='Contenidos')
    plt.legend(handles=[user_patch, content_patch])
    plt.xlim(-1, 6)
    plt.ylim(-1, 6)
    plt.grid(True)
    plt.title("Vectores de usuarios y contenidos")
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    plt.show()