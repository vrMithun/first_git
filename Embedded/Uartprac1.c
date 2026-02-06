#include "stm32f4xx.h"

void UART_init(void){
	RCC->AHB1ENR |= (1<<0);
	RCC->APB1ENR |= (1<<17);
	
	GPIOA->MODER &= ~((3<<4) | (3<<6));
	GPIOA->MODER |= ((2<<4) | (2<<6));
	
	GPIOA->AFR[0] |= ((7<<8) | (7<<12));
	
	USART2->BRR = 0x0683;
	USART2->CR1 |= ((1<<2) | (1<<3));
	USART2->CR2 |= (1<<13);
}

void send_char(char c){
	while((USART2->SR & (1<<7))==0);
	USART2->DR=c;
}

void send_string(char *str){
	while(*str){
		send_char(*str++);
	}
}

void timer(uint32_t ms){
	SysTick->LOAD=16000-1;
	SysTick->VAL=0;
	SysTick->CTRL=0x5;
	for(uint32_t i=0;i<ms;i++){
		while(SysTick->CTRL & (1<<16) == 0);
	}
	SysTick->CTRL=0;
}