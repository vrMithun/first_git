#include "stm32f4xx.h"
#include <stdio.h>

volatile uint16_t adcValue;
char buffer[50];

void UART2_Init(void);
void ADC1_Init(void);
void UART2_SendString(char *str);

int main(void)
{
    UART2_Init();
    ADC1_Init();

    while (1)
    {
        // Trigger ADC conversion manually
        ADC1->CR2 |= (1 << 30); // SWSTART bit: start conversion
        for (volatile int i = 0; i < 100000; i++); // small delay
    }
}

void UART2_Init(void)
{
    RCC->AHB1ENR |= (1 << 0);   // Enable GPIOA clock
    RCC->APB1ENR |= (1 << 17);  // Enable USART2 clock

    // PA2 -> TX (AF7), PA3 -> RX (AF7)
    GPIOA->MODER &= ~((3 << 4) | (3 << 6));
    GPIOA->MODER |= ((2 << 4) | (2 << 6));    // Alternate function
    GPIOA->AFR[0] |= (7 << 8) | (7 << 12);    // AF7 for USART2

    USART2->BRR = 0x0683;       // 9600 baud @16MHz
    USART2->CR1 |= (1 << 2) | (1 << 3);  // RX, TX enable
    USART2->CR1 |= (1 << 13);   // USART enable
}

void ADC1_Init(void)
{
    RCC->AHB1ENR |= (1 << 0);   // Enable GPIOA clock
    GPIOA->MODER |= (3 << 0);   // PA0 analog mode

    RCC->APB2ENR |= (1 << 8);   // Enable ADC1 clock

    ADC1->SQR3 = 0;             // Channel 0
    ADC1->CR1 |= (1 << 5);      // Enable EOC interrupt
    ADC1->CR2 |= (1 << 0);      // ADC ON

    NVIC_EnableIRQ(ADC_IRQn);   // Enable ADC interrupt in NVIC
}

void UART2_SendString(char *str)
{
    while (*str)
    {
        while (!(USART2->SR & (1 << 7))); // Wait until TXE = 1
        USART2->DR = *str++;
    }
}

// ⚡ ADC interrupt handler
void ADC_IRQHandler(void)
{
    if (ADC1->SR & (1 << 1))    // Check EOC flag
    {
        adcValue = ADC1->DR;    // Read ADC result
        sprintf(buffer, "ADC Value: %u\r\n", adcValue);
        UART2_SendString(buffer);
    }
}
