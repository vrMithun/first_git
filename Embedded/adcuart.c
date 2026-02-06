#include "stm32f4xx.h"
#include <stdio.h>

uint16_t adcData;

void USART2_Init(void);
void USART2_SendChar(char c);
void USART2_SendString(char *str);
void delayMs(uint32_t ms);

int main(void)
{
    char buffer[30];

    // --- GPIOA Clock enable ---
    RCC->AHB1ENR |= (1U << 0); // GPIOA clock ON

    // --- ADC1 Clock enable ---
    RCC->APB2ENR |= (1U << 8); // ADC1 clock ON

    // --- Configure PA0 as Analog mode ---
    GPIOA->MODER |= (3U << 0); // PA0 analog

    // --- Configure ADC1 ---
    ADC1->SMPR2 &= ~(0x7 << 0);  // 3 cycles sample time for channel 0
    ADC->CCR &= ~(0x3 << 16);    // ADC prescaler = /2
    ADC1->CR1 = 0;
    ADC1->CR2 = 0;
    ADC1->CR2 |= (1U << 1);      // Continuous conversion mode
    ADC1->SQR3 &= ~(0x1F);       // Channel 0 selected
    ADC1->SQR1 &= ~(0xF << 20);  // Only one conversion in sequence
    ADC1->CR2 |= 1;              // ADC ON
    while ((ADC1->CR2 & 1) == 0); // Wait until ADC ready
    ADC1->CR2 |= (1 << 30);      // Start conversion (SWSTART)

    // --- Initialize USART2 ---
    USART2_Init();

    while (1)
    {
        while (!(ADC1->SR & (1 << 1))); // Wait till conversion complete
        adcData = ADC1->DR;             // Read ADC value

        sprintf(buffer, "ADC Value: %u\r\n", adcData);
        USART2_SendString(buffer);

        delayMs(500);
    }
}

void USART2_Init(void)
{
    // --- Enable GPIOA and USART2 clocks ---
    RCC->AHB1ENR |= (1U << 0);   // GPIOA clock
    RCC->APB1ENR |= (1U << 17);  // USART2 clock

    // --- Set PA2 (TX) and PA3 (RX) to AF7 ---
    GPIOA->MODER &= ~((3U << 4) | (3U << 6)); // Clear mode
    GPIOA->MODER |= (2U << 4) | (2U << 6);    // AF mode
    GPIOA->AFR[0] |= (7U << 8) | (7U << 12);  // AF7 (USART2)

    // --- Configure USART2 (9600 baud, 8N1) ---
    USART2->BRR = 0x0683; // Baud rate = 9600 for 16MHz
    USART2->CR1 = (1U << 13) | (1U << 3) | (1U << 2); // UE, TE, RE
}

void USART2_SendChar(char c)
{
    while (!(USART2->SR & (1 << 7))); // Wait until TXE (Transmit Data Register Empty)
    USART2->DR = c;
}

void USART2_SendString(char *str)
{
    while (*str)
    {
        USART2_SendChar(*str++);
    }
}

void delayMs(uint32_t ms)
{
    for (uint32_t i = 0; i < (ms * 1600); i++)
        __NOP();
}
