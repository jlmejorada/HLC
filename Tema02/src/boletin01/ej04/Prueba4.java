package boletin01.ej04;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba4 {

	@ParameterizedTest
	@MethodSource("primillo")
	void testEsPrimo(int num, boolean resEsperado) {
		boolean resObtenido = Ejercicio4.esPrimo(num);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> primillo(){
		return  Stream.of(Arguments.of(2, true),
				Arguments.of(3, true),
				Arguments.of(13, true),
				Arguments.of(50, false),
				Arguments.of(1, false)
						);
	}

}
