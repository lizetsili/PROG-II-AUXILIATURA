package Herencia;
class Empleado {
    protected int sueldoMes;
    protected String nombre;

    public Empleado(String nombre, int sueldoMes) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
    }

    public int SueldoTotal() {
        return sueldoMes;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Sueldo base: " + sueldoMes;
    }
}

class Administrativo extends Empleado {
    private String cargo;

    public Administrativo(String nombre, int sueldoMes, String cargo) {
        super(nombre, sueldoMes);
        this.cargo = cargo;
    }

    @Override
    public String toString() {
        return super.toString() + ", Cargo: " + cargo;
    }
}

class Chef extends Empleado {
    private int horaExtra;
    private String tipo;
    private int sueldoHora;

    public Chef(String nombre, int sueldoMes, int horaExtra, String tipo, int sueldoHora) {
        super(nombre, sueldoMes);
        this.horaExtra = horaExtra;
        this.tipo = tipo;
        this.sueldoHora = sueldoHora;
    }

    @Override
    public int SueldoTotal() {
        return sueldoMes + (horaExtra * sueldoHora);
    }

    @Override
    public String toString() {
        return super.toString() + ", Tipo: " + tipo + ", Horas extra: " + horaExtra +
               ", Sueldo total: " + SueldoTotal();
    }
}

class Mesero extends Empleado {
    private int horaExtra;
    private int sueldoHora;
    private int propina;

    public Mesero(String nombre, int sueldoMes, int horaExtra, int sueldoHora, int propina) {
        super(nombre, sueldoMes);
        this.horaExtra = horaExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    @Override
    public int SueldoTotal() {
        return sueldoMes + (horaExtra * sueldoHora) + propina;
    }

    @Override
    public String toString() {
        return super.toString() + ", Horas extra: " + horaExtra + ", Propina: " + propina +
               ", Sueldo total: " + SueldoTotal();
    }
}

public class Restaurante {
    public static void main(String[] args) {
        Chef chef1 = new Chef("Remy", 3000, 10, "Principal", 50);
        Mesero mesero1 = new Mesero("Linguini", 2000, 5, 30, 200);
        Mesero mesero2 = new Mesero("Colette", 2200, 8, 25, 150);
        Administrativo admin1 = new Administrativo("Skinner", 2500, "Gerente");
        Administrativo admin2 = new Administrativo("Anton", 2400, "Contador");

        Empleado[] empleados = {chef1, mesero1, mesero2, admin1, admin2};

        int X = 2500;
        System.out.println("\nEmpleados con sueldo igual a " + X + ":");
        for (Empleado e : empleados) {
            if (e.sueldoMes == X) {
                System.out.println(e);
            }
        }

        System.out.println("\n--- Sueldos Totales ---");
        for (Empleado e : empleados) {
            System.out.println(e);
        }
    }
}
