package boletin01.ej03;

public class Ejercicio3 {

	public static String comprueba(int num) {
		String linea="";
		if (num%3==0) {
			linea+="fizz";
		}
		if (num%5==0) {
			linea+="buzz";
		}
		return linea;
	}
}
