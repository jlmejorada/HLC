package boletin01.ej10;

public class Ejercicio10 {

	public static boolean palindromo(String palabra1, String palabra2){
		boolean esPalindromo=false;
		String otroOrden="";
		for (int i=palabra2.length()-1 ; i>=0 ;i--) {
			otroOrden+=palabra2.charAt(i);
		}
		if (palabra1.equals(otroOrden)) {
			esPalindromo=true;
		}
		return esPalindromo;
	}
}
