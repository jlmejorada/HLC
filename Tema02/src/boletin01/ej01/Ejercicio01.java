package boletin01.ej01;

public class Ejercicio01 {

	public static boolean esVocal(char caracter) {
		boolean res=false;
		char chara = Character.toLowerCase(caracter);
		
		switch (chara) {
		case 'a', 'e', 'i', 'o', 'u' -> {
			res=true;
		}
		}
		
		/*if (Character.toLowerCase(caracter) == 'a') {
			res = true;
		}*/
		return res;
	}
}
