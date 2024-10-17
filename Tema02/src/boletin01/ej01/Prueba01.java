package boletin01.ej01;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Prueba01 {

	@ParameterizedTest
	@MethodSource("vocalista")
	void testEsVocal(char caracter, boolean resEsperado) {
		boolean resObtenido = Ejercicio01.esVocal(caracter);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> vocalista(){
		return  Stream.of(Arguments.of('a', true),
						Arguments.of('E', true),
						Arguments.of('i', true),
						Arguments.of('O', true),
						Arguments.of('U', true),
						Arguments.of('c', false)
						);
	}
	
	
	/*
	@Test
	public void testEsVocalAMinuscula() {
		boolean res = Ejercicio1.esVocal('a');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalAMayuscula() {
		boolean res = Ejercicio1.esVocal('A');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalEMinuscula() {
		boolean res = Ejercicio1.esVocal('e');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalEMayuscula() {
		boolean res = Ejercicio1.esVocal('E');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalIMinuscula() {
		boolean res = Ejercicio1.esVocal('i');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalIMayuscula() {
		boolean res = Ejercicio1.esVocal('I');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalOMinuscula() {
		boolean res = Ejercicio1.esVocal('o');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalOMayuscula() {
		boolean res = Ejercicio1.esVocal('O');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalUMinuscula() {
		boolean res = Ejercicio1.esVocal('u');
		assertTrue(res);
	}
	
	@Test
	public void testEsVocalUMayuscula() {
		boolean res = Ejercicio1.esVocal('U');
		assertTrue(res);
	}

	@Test
	public void testEsConsonante() {
		boolean res = Ejercicio1.esVocal('c');
		assertFalse(res);
	}*/
}
