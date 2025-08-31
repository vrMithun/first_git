module HailSeq (hailseq) where

hail :: Int -> Int
hail x=
    if x `mod` 2==0
    then x `div` 2
    else 3*x+1

hailseq :: Int->[Int]
hailseq x=[hail x|x<-[1..x]]