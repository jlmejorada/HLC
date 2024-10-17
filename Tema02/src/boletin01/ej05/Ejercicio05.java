package boletin01.ej05;

public class Ejercicio05 {
	public static boolean esCapicua(int num) {

		boolean esCapicua = false;
		int reves = 0;
		int resto=num;


		while (resto>0) {
				reves *= 10;
				reves += resto % 10;
				resto = resto / 10;

		}

		if (num == reves) {

			esCapicua = true;

		}

		return esCapicua;
	}

}
