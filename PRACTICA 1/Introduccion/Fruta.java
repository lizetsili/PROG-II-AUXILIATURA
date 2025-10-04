import java.util.Arrays;

public class Fruta {
    public static void main(String[] args) {
        String[] nombres = {"Kiwi", "Mango", "Naranja"};
        String[] tipos = {"Subtropical", "Templado", "Cítrica"};
        String[][] vitaminas = {
            {"C", "E"},      
            {"A", "C"},     
            {"C", "B9"}      
        };
        int max = 0;
        int indexMax = 0;
        for (int i = 0; i < nombres.length; i++) {
            if (vitaminas[i].length > max) {
                max = vitaminas[i].length;
                indexMax = i;
            }
        }
        System.out.println("Fruta con más vitaminas: " + nombres[indexMax]);
        String vitMango = String.join(" ", vitaminas[1]);
        System.out.println("Vitaminas de Mango: " + vitMango);
        int citricas = 0;
        for (int i = 0; i < vitaminas.length; i++) {
            for (int j = 0; j < vitaminas[i].length; j++) {
                if (vitaminas[i][j].equals("C") || vitaminas[i][j].equals("B9")) {
                    citricas++;
                }
            }
        }
        System.out.println("Cantidad de vitaminas cítricas: " + citricas);
        for (int i = 0; i < nombres.length; i++) {
            String[] vitCopy = vitaminas[i].clone();
            Arrays.sort(vitCopy);
            System.out.println(nombres[i] + " → " + String.join(" ", vitCopy));
        }
    }
}
