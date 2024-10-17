package boletin01.ej07;

public class Ejercicio07 {

	public static boolean fechaValida(int dia, int mes, int anno) {
		boolean esValida = false;

		switch (mes) {
		case 1, 3, 5, 7, 8, 10, 12 -> {
			if (dia > 0 && dia <= 31) {
				esValida = true;
			}
		}
		case 4, 6, 9, 11->{
			if (dia>0 && dia<=30) {
				esValida = true;
			}
		}
		case 2->{
			if ((anno % 4 == 0 && anno % 100 != 0) || (anno % 100 == 0 && anno % 400 == 0)) {
				if (dia>0 && dia<=29) {
					esValida = true;
				}
			} else {
				if (dia>0 && dia<=28) {
					esValida = true;
				}
			}
		}
		}

		return esValida;
	}
}
