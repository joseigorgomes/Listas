public class BubbleSort {

    private int[] lista;

    public BubbleSort(int[] lista){
        this.lista = lista;
    }

    public int[] bubbleSort(){
        boolean trocou = true;
        while(trocou){
            trocou = false;
            for (int i = 0; i < lista.length - 1; i ++) {
                for (int j = i + 1; j < lista.length; j++) {
                    if (lista[i] > lista[j]) {
                        int aux = lista[i];
                        lista[i] = lista[j];
                        lista[j] = aux;
                        trocou = true;
                    }
                }
            }
        }
        return lista;
    }
}
