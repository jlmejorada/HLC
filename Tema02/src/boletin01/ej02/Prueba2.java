package boletin01.ej02;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba2 {

	@ParameterizedTest
	@MethodSource("pareado")
	void testEsPar(int num, boolean resEsperado) {
		boolean resObtenido = Ejercicio2.esPar(num);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> pareado(){
		return  Stream.of(Arguments.of(2, true),
				Arguments.of(1, false),
				Arguments.of(4, true),
				Arguments.of(3, false),
				Arguments.of(2020202, true)
						);
	}

}
