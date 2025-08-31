#include "stm32f4xx.h"
int adcData;
int main(void) {
    RCC->AHB1ENR |= (1U << 0);  //turns on the clock in GPIOA
    
    RCC->APB2ENR |= (1 << 8); // power up ADC1
    
    GPIOA->MODER |= (3U << 0); // setting PA0 to analog mode
	
    ADC1->SMPR2 &= ~(0x7 << 0); // setting the 3 cycles for channel 0. tells how long the capacitor should spend time in matching the potentiometer voltage

    ADC->CCR &= ~(0x3 << 16);    // sets ADC clock. it tells how fast the ADC should do the sampling and conversion.

    ADC1->CR1 = 0; // clearing the setting of CR1
    ADC1->CR2 = 0; // clearing the setting of CR2
    ADC1->CR2 |= (1U << 1);  // makes the ADC to keep converting without stoping
    ADC1->SQR3 &= ~(0x1F); // sets channel 0 (PA0) as first conversation
	
    ADC1->SQR1 &= ~(0xF << 20); // sets conversation sequence to 1 channel i.e only one channel is there to communicate
    
    ADC1->CR2 |= 1; // turning on the ADC
		
    while((ADC1->CR2 & 1) == 0) {} // waiting loop for turning on. reduces the error
			 
    ADC1->CR2 |= (1 << 30); // triggers conversation. sets SWSTART bit

    while (1) {
       
        
        while (!(ADC1->SR & (1 << 1))) {} // SR(Status register) is a flag that says wheather the conversation is finished(1) or not(1)
        
        adcData = ADC1->DR; // read and store the data
    }
}
