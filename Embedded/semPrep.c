#include "stm32f4xx.h"

volatile uint16_t val=0;

void adc_init(void){
	RCC->AHB1ENR |= (1<<0);
	RCC->APB2ENR |= (1<<8);
	
	GPIOA->MODER &= ~(3<<0);
	GPIOA->MODER |= (3<<0);
	
	ADC1->SQR3=0;
	ADC1->CR1 |= (1<<5);
	ADC1->CR2 |= (1<<1);
	ADC1->CR2 |= (1<<0);
	ADC1->CR2 |= (1<<30);
	
	NVIC_EnableIRQ(ADC_IRQn);
}

void ADC_IRQHandler(void){
	if(ADC1->SR & (1<<1)){
		val=ADC1->DR;
		ADC1->SR &= ~(1<<1);
	}
}

void delay(uint32_t ms){
	SysTick->LOAD=16000-1;
	SysTick->VAL=0;
	SysTick->CTRL=0x5;
	
	for(uint32_t i=0;i<ms;i++){
		while((SysTick->CTRL & (1<<16))==0);
	}
	SysTick->CTRL =0;
}