package boletin01.ej05;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba05 {

	@ParameterizedTest
	@MethodSource("capicua")
	void testEsCapicua(int num, boolean resEsperado) {
		boolean resObtenido = Ejercicio05.esCapicua(num);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> capicua(){
		return  Stream.of(Arguments.of(-2, false),
				Arguments.of(2, true),
				Arguments.of(10, false),
				Arguments.of(11, true),
				Arguments.of(100, false),
				Arguments.of(1010, false),
				Arguments.of(10101, true)
						);
	}

}
