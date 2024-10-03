package boletin01.ej06;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba06 {

	@ParameterizedTest
	@MethodSource("calcula")
	void testResCalc(int num1, int num2, int opc, double resEsperado) {
		double resObtenido = Ejercicio06.ResCalc(num1, num2, opc);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> calcula(){
		return  Stream.of(Arguments.of(2, 2, 1 , 4),
				Arguments.of(2, 2, 2, 0),
				Arguments.of(2, 3, 3 , 6),
				Arguments.of(6, 2, 4 , 3),
				Arguments.of(0, 0, 6 , Integer.MIN_VALUE)
						);
	}

}
