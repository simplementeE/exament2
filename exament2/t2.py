import random
import math

def generate_coordinates(n):
    """Generate n random coordinate pairs with x, y in [-81, 81]."""
    return [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

def distance_from_origin(x, y):
    """Calculate Euclidean distance from (0,0) using Pythagorean theorem."""
    return math.sqrt(x**2 + y**2)

def find_max_distance(coordinates, left, right):
    """Divide and conquer to find coordinate with max distance where x > 0 and y < 0."""
 
    if left == right:
        x, y = coordinates[left]
        if x > 0 and y < 0:
            return coordinates[left], distance_from_origin(x, y)
        return None, 0
    
   
    if right - left == 1:
        max_coord, max_dist = None, 0
        for i in range(left, right + 1):
            x, y = coordinates[i]
            if x > 0 and y < 0:
                dist = distance_from_origin(x, y)
                if dist > max_dist:
                    max_coord, max_dist = coordinates[i], dist
        return max_coord, max_dist
    
    # Divide
    mid = (left + right) // 2
    left_coord, left_dist = find_max_distance(coordinates, left, mid)
    right_coord, right_dist = find_max_distance(coordinates, mid + 1, right)
    
    # Conquer: compare distances
    if left_coord is None and right_coord is None:
        return None, 0
    elif left_coord is None:
        return right_coord, right_dist
    elif right_coord is None:
        return left_coord, left_dist
    else:
        return (left_coord, left_dist) if left_dist > right_dist else (right_coord, right_dist)

def main():
    
    n = int(input("Introduzca el número de pares de coordenadas: "))
    
    
    coordinates = generate_coordinates(n)
    
   
    print("\nCoordenadas generadas:")
    for coord in coordinates:
        print(coord)
    
  
    max_coord, max_dist = find_max_distance(coordinates, 0, len(coordinates) - 1)
    
   
    print("\nCoordenada con distancia máxima (x > 0, y < 0):")
    if max_coord is None:
        print("No se encontraron coordenadas con x > 0 y y < 0")
    else:
        print(f"Coordenada: {max_coord}, Distancia: {max_dist:.2f}")

if __name__ == "__main__":
    
    n = int(input("Introduzca el número de pares de coordenadas para la prueba: "))
    print(f"\nPrueba con {n} pares de coordenadas:")
    coordinates = generate_coordinates(n)
    print("\nCoordenadas generadas:")
    for coord in coordinates:
        print(coord)
    max_coord, max_dist = find_max_distance(coordinates, 0, n - 1)
    print("\nCoordenada con distancia máxima (x > 0, y < 0):")
    if max_coord is None:
        print("No se encontraron coordenadas con x > 0 y y < 0")
    else:
        print(f"Coordenada: {max_coord}, Distancia: {max_dist:.2f}")