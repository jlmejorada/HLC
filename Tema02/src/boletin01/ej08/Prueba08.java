package boletin01.ej08;

import static org.junit.jupiter.api.Assertions.*;

import java.util.stream.Stream;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import boletin01.ej08.Ejercicio08;

class Prueba08 {

	@ParameterizedTest
	@MethodSource("sucesion")
	void testResCalc(int num, int resEsperado) throws Exception {
		int resObtenido = 0;
		
		resObtenido = Ejercicio08.fibonacci(num);
		
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> sucesion(){
		return  Stream.of(Arguments.of(1, 1),
				Arguments.of(2, 1),
				Arguments.of(3, 2),
				Arguments.of(7, 13)
						);
	}
	
	@Test
	public void numNega() {
		Assertions.assertThrows(Exception.class, () -> Ejercicio08.fibonacci(4), "El número tiene que ser positivo");
	}

}