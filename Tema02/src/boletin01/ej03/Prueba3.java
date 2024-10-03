package boletin01.ej03;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba3 {

	@ParameterizedTest
	@MethodSource("multiplo")
	void testEsMul(int num, String resEsperado) {
		String resObtenido = Ejercicio3.comprueba(num);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> multiplo(){
		return  Stream.of(Arguments.of(9, "fizz"),
				Arguments.of(2, ""),
				Arguments.of(10, "buzz"),
				Arguments.of(15, "fizzbuzz")
						);
	}

}
