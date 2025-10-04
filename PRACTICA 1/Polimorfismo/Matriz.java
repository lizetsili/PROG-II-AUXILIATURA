public class Matriz {
    private float[][] matriz;
    public Matriz() {
        matriz = new float[10][10];
        for (int i = 0; i < 10; i++) {
            matriz[i][i] = 1.0f;
        }
    }
    public Matriz(float[][] valores) {
        matriz = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                matriz[i][j] = valores[i][j];
            }
        }
    }
    public Matriz sumar(Matriz otra) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] + otra.matriz[i][j];
            }
        }
        return resultado;
    }
    public Matriz restar(Matriz otra) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] - otra.matriz[i][j];
            }
        }
        return resultado;
    }
    public boolean igual(Matriz otra) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (this.matriz[i][j] != otra.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    public void mostrar() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("------------------------");
    }
    public static void main(String[] args) {
        Matriz identidad = new Matriz();
        System.out.println("Matriz Identidad:");
        identidad.mostrar();
        float[][] datos = new float[10][10];
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < 10; j++)
                datos[i][j] = i + j;

        Matriz personalizada = new Matriz(datos);
        System.out.println("Matriz Personalizada:");
        personalizada.mostrar();

        Matriz suma = identidad.sumar(personalizada);
        System.out.println("Suma:");
        suma.mostrar();

        Matriz resta = personalizada.restar(identidad);
        System.out.println("Resta:");
        resta.mostrar();

        System.out.println("¿Personalizada == Identidad? " + personalizada.igual(identidad));
    }
}
