package boletin01.ej07;

import static org.junit.jupiter.api.Assertions.*;

import java.util.stream.Stream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import boletin01.ej06.Ejercicio06;

class Prueba07 {

	@ParameterizedTest
	@MethodSource("fecha")
	void testResCalc(int num1, int num2, int num3, boolean resEsperado) {
		boolean resObtenido = false;
		
		resObtenido = Ejercicio07.fechaValida(num1, num2, num3);
		
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> fecha(){
		return  Stream.of(Arguments.of(31, 8, 1974 , true),
				Arguments.of(31,11,2000, false),
				Arguments.of(22,11,2000, true),
				Arguments.of(29,2,2000, true),
				Arguments.of(29,2,2001, false),
				Arguments.of(28,2,2001, true)
						);
	}

}
