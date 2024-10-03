package boletin01.ej06;

public class Ejercicio06 {

	public static double ResCalc(int num1, int num2, int opc) throws Exception {
		double res=0;
		
		switch (opc) {
		case 1->{
			res=num1+num2;
		}
		case 2->{
			res=num1-num2;
		}
		case 3->{
			res=num1*num2;
		}
		case 4->{
			res=num1/num2;
		}
		default ->{
			throw new Exception("Opción no valida");
			
		}
		}
		
		return res;
	}
}
