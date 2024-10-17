package boletin01.ej04;

public class Ejercicio4 {

	public static boolean esPrimo(int num) {
		boolean esPrimo= (num>1);
		int indice=2;
		while (indice <= Math.sqrt(num) && esPrimo) {
			if (num%indice==0) {
				esPrimo=false;
			}
			indice++;
		}
		return esPrimo;
	}
}
