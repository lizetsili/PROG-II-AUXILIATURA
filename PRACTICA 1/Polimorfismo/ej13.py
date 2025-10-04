class MP4:
    def __init__(self):
        self.__canciones = [
            ["Back To Black", "Amy Winehouse", 100],
            ["Lost On You", "LP", 150]
        ]
        self.__videos = [
            ["Heathens", "twenty one pilots", 50],
            ["Harmonica", "KSHMR", 70],
            ["Without Me", "Halsey", 30]
        ]
        self.__max_canciones = 100
        self.__max_videos = 100
    def mostrar(self):
        print("Canciones:")
        for c in self.__canciones:
            print(f"Nombre: {c[0]}, Artista: {c[1]}, Peso: {c[2]} Kb")
        print("\nVideos:")
        for v in self.__videos:
            print(f"Nombre: {v[0]}, Artista: {v[1]}, Peso: {v[2]} Mg")
    def add_cancion(self, nombre, artista, peso):
        if len(self.__canciones) < self.__max_canciones:
            for c in self.__canciones:
                if c[0] == nombre and c[1] == artista:
                    print("La canción ya existe.")
                    return
            self.__canciones.append([nombre, artista, peso])
            print(f"Canción '{nombre}' añadida.")
        else:
            print("No hay espacio para más canciones.")
    def add_video(self, nombre, artista, peso):
        if len(self.__videos) < self.__max_videos:
            for v in self.__videos:
                if v[0] == nombre and v[1] == artista:
                    print("El video ya existe.")
                    return
            self.__videos.append([nombre, artista, peso])
            print(f"Video '{nombre}' añadido.")
        else:
            print("No hay espacio para más videos.")

    def borrar_cancion(self, nombre=None, artista=None, peso=None):
        nuevas = []
        for c in self.__canciones:
            if nombre and c[0] != nombre:
                nuevas.append(c)
            elif artista and c[1] != artista:
                nuevas.append(c)
            elif nombre and peso and not (c[0] == nombre and c[2] == peso):
                nuevas.append(c)
        self.__canciones = nuevas
        print("Canción(s) borrada(s) según criterios.")

    def capacidad_disponible(self):
        print(f"Canciones disponibles: {self.__max_canciones - len(self.__canciones)}")
        print(f"Videos disponibles: {self.__max_videos - len(self.__videos)}")

mp4 = MP4()
mp4.mostrar()

print("\n--- Añadir canción ---")
mp4.add_cancion("New Song", "New Artist", 120)
mp4.mostrar()

print("\n--- Añadir video ---")
mp4.add_video("New Video", "Artist Video", 80)
mp4.mostrar()

print("\n--- Borrar canción por nombre ---")
mp4.borrar_cancion(nombre="Back To Black")
mp4.mostrar()

print("\n--- Capacidad disponible ---")
mp4.capacidad_disponible()
