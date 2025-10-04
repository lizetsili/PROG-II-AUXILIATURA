package Herencia;

class Persona {
    protected String nombre;
    protected int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }
}
interface Empleado {
    double getSueldo();
    int getAntiguedad();
}
interface Policia {
    String getGrado();
    String getUnidad();
}
class JefePolicia extends Persona implements Empleado, Policia {
    private double sueldo;
    private int antiguedad;
    private String grado;
    private String unidad;

    public JefePolicia(String nombre, int edad, double sueldo, int antiguedad, String grado, String unidad) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.antiguedad = antiguedad;
        this.grado = grado;
        this.unidad = unidad;
    }

    @Override
    public double getSueldo() {
        return sueldo;
    }

    @Override
    public int getAntiguedad() {
        return antiguedad;
    }

    @Override
    public String getGrado() {
        return grado;
    }

    @Override
    public String getUnidad() {
        return unidad;
    }

    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad +
                ", Sueldo: " + sueldo + ", Antigüedad: " + antiguedad +
                ", Grado: " + grado + ", Unidad: " + unidad);
    }
}

public class Ejercicio11 {
    public static void main(String[] args) {
        JefePolicia jefe1 = new JefePolicia("Carlos", 45, 5000, 20, "Comandante", "Antinarcóticos");
        JefePolicia jefe2 = new JefePolicia("Luis", 50, 5500, 25, "Comandante", "Tránsito");

        System.out.println("=== DATOS JEFES POLICIA ===");
        jefe1.mostrarDatos();
        jefe2.mostrarDatos();
        System.out.println("\n=== MAYOR SUELDO ===");
        if (jefe1.getSueldo() > jefe2.getSueldo()) {
            System.out.println("Mayor sueldo: " + jefe1.getNombre());
        } else if (jefe1.getSueldo() < jefe2.getSueldo()) {
            System.out.println("Mayor sueldo: " + jefe2.getNombre());
        } else {
            System.out.println("Ambos tienen el mismo sueldo.");
        }
        System.out.println("\n=== COMPARAR GRADO ===");
        if (jefe1.getGrado().equalsIgnoreCase(jefe2.getGrado())) {
            System.out.println("Ambos tienen el mismo grado: " + jefe1.getGrado());
        } else {
            System.out.println("Tienen diferentes grados: " +
                    jefe1.getGrado() + " vs " + jefe2.getGrado());
        }
    }
}
