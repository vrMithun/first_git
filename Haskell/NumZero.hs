module NumZero (numzero) where

numzero :: Int->Int
numzero x= helper (abs x,0)
    where 
        helper (0,c)=c
        helper (x,c)=if x `mod` 10 ==0 then helper (x `div` 10,c+1) else helper (x `div` 10,c)