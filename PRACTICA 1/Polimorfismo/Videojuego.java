public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;
    public Videojuego() {
        this.nombre = "Sin nombre";
        this.plataforma = "Desconocida";
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre) {
        this.nombre = nombre;
        this.plataforma = "Genérica";
        this.cantidadJugadores = 1;
    }
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }
    public void agregarJugadores() {
        this.cantidadJugadores += 1;
    }
    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
    }
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de jugadores: " + cantidadJugadores);
        System.out.println("------------------------------");
    }
    public static void main(String[] args) {
        Videojuego v1 = new Videojuego();
        Videojuego v2 = new Videojuego("FIFA 25");
        Videojuego v3 = new Videojuego("Minecraft", "PC", 5);
        v1.mostrarDatos();
        v2.mostrarDatos();
        v3.mostrarDatos();

        v2.agregarJugadores();      
        v3.agregarJugadores(3);      
        
        System.out.println("Después de agregar jugadores:");
        v2.mostrarDatos();
        v3.mostrarDatos();
    }
}

