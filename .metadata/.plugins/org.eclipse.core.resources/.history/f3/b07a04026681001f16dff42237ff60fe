package boletin01.ej09;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

public class Prueba09 {
	@ParameterizedTest
	@MethodSource("bin")
	void testResCalc(int num, String resEsperado){
		String resObtenido = "";
		
		resObtenido = Ejercicio09.binario(2);
		
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> bin(){
		return  Stream.of(Arguments.of(2, "10"),
				Arguments.of(7, "111"),
				Arguments.of(8, "1000")
						);
	}
}
