public class Buzon {
    public static void main(String[] args) {

        String[] codigos = {"c001", "c002", "c003"};
        String[] remitentes = {"Juan", "Ana", "Luis"};
        String[] destinatarios = {"Pedro", "Pedro", "Maria"};
        String[] descripciones = {
            "Querido amigo, te escribo sobre amor",
            "Hola, recuerda la reunión",
            "Feliz cumpleaños, mucho amor"
        };
        int cartasPedro = 0;
        for (int i = 0; i < destinatarios.length; i++) {
            if (destinatarios[i].equals("Pedro")) {
                cartasPedro++;
            }
        }
        System.out.println("Pedro recibió " + cartasPedro + " carta(s)");
        for (int i = 0; i < codigos.length; i++) {
            if (codigos[i].equals("c002")) {
                codigos[i] = "";
                remitentes[i] = "";
                destinatarios[i] = "";
                descripciones[i] = "";
            }
        }
        System.out.println("Se eliminó la carta c002");
        System.out.println("Remitentes con cartas:");
        for (int i = 0; i < remitentes.length; i++) {
            if (!remitentes[i].equals("")) {
                System.out.println(remitentes[i]);
            }
        }

        System.out.println("Búsqueda de la palabra 'amor':");
        for (int i = 0; i < descripciones.length; i++) {
            if (descripciones[i].contains("amor")) {
                System.out.println("Palabra 'amor' encontrada:");
                System.out.println("Código: " + codigos[i]);
                System.out.println("Remitente: " + remitentes[i]);
                System.out.println("Destinatario: " + destinatarios[i]);
                System.out.println("--------------------");
            }
        }
    }
}
