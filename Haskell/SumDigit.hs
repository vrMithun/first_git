module SumDigit (sumdigit) where

sumdigit :: Int->Int
sumdigit 0=0
sumdigit x=x `mod` 10 + sumdigit (x `div` 10)