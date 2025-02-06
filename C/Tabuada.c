#include <stdio.h>

main() {
	int i;
	int valor = 2;
	int resultado = 0;
	for(i = 0; i <= 10; i++){
		resultado = valor * i;
		printf("%d x %d = %d \n", valor, i, resultado);
	}
}
