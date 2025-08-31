module BaseExp (baseexp) where

base :: Int->Int->Int->[Int]
base 1 d c=[d,c]
base x d c=
    if (x `mod` d)==0
    then base (x `div` d) d (c+1)
    else base x (d+1) c

baseexp :: Int->[Int]
baseexp x=base x 2 0