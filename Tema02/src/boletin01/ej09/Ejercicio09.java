package boletin01.ej09;

public class Ejercicio09 {

	public static String binario(int num){
		String res="";
		String prov="";
		int inter=num;
		while (inter>=2) {
			prov+=inter%2;
			inter/=2;
		}
		prov+=inter;

		for (int i=prov.length()-1; i>=0 ; i--) {
			res+=prov.charAt(i);
		}
		return res;
	}
}
