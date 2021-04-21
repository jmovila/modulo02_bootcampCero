class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self):
        if self.peso >=8:
            print('GUAU, GUAU')
        else:
            print('guau, guau')
            
    def __str__(self):
        return 'Soy el Perro {}'.format(self.nombre)
        
salchicho = Perro('salchicho', 5, 9)
lola = Perro('lola', 3, 2)
salchicho.ladrar()
lola.ladrar()