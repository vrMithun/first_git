#include "stm32f4xx.h"
#include "stdio.h"

char str[30];
volatile uint16_t val;
void adc_init(void){
	RCC->AHB1ENR |= (1<<0);
	RCC->APB2ENR |= (1<<8);
	
	GPIOA->MODER &= ~(3<<0);
	GPIOA->MODER |= (3<<0);
	
	ADC1->SQR3=0;
	ADC1->CR1 |= (1<<5);
	ADC1->CR2 |= (1<<0);
	
	NVIC_EnableIRQ(ADC_IRQn);
}

void ADC_IRQHandler(void){
	if((ADC1->SR & (1<<1))){
		sprintf(str,"adc value:%u\r\n",ADC1->DR);
		send_string(str);
	}
}

void uart_init(void){
	RCC->AHB1ENR |= (1<<0);
	RCC->APB1ENR |= (1<<17);
	
	GPIOA->MODER &= ~((3<<4) | (3<<6));
	GPIOA->MODER |= ((2<<4) | (2<<6));
	
	GPIOA->AFR[0] |= ((7<<8) | (7<<12));
	
	USART2->BRR=0x0683;
	USART2->CR1 |= ((1<<2) | (1<<3));
	USART2->CR1 |= (1<<13);
}

void send_string(char *str){
	while(*str){
		while((USART2->SR & (1<<7))==0);
		USART2->DR=*str++;
	}
}

int main(void){
	adc_init();
	uart_init();
	while(1){
		ADC1->CR2 |= (1<<30);
		for (volatile int i = 0; i < 100000; i++);
	}
}