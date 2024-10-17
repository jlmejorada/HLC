package boletin01.ej10;

import static org.junit.jupiter.api.Assertions.*;

import java.util.stream.Stream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import boletin01.ej09.Ejercicio09;

class Prueba10 {

	@ParameterizedTest
	@MethodSource("pal")
	void testResCalc(String palabra1, String palabra2,  boolean resEsperado){
		boolean resObtenido;
		
		resObtenido = Ejercicio10.palindromo(palabra1,palabra2);
		
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> pal(){
		return  Stream.of(Arguments.of("si", "is", true),
				Arguments.of("si", "no", false),
				Arguments.of("casa", "asac", true),
				Arguments.of("palabra", "arbalap", true),
				Arguments.of("menganito", "pedro", false)
						);
	}

}