package boletin01.ej08;

public class Ejercicio08 {

	public static int fibonacci(int num) throws Exception {
		int res = 0;

		if (num < 1) {
			
			throw new Exception("El número tiene que ser positivo");

		} else {
			
			if (num == 1 || num == 2) {

				res = 1;

			} else {
				
				res = (fibonacci(num - 1)) + (fibonacci(num - 2));
			}

		}

		return res;
	}
}
