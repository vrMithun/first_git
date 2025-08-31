module NumDigit (numdigit) where

numdigit :: Int->Int
numdigit 0=0
numdigit x=1+numdigit (x `div` 10)