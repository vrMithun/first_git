module Map (othermap) where

othermap :: (Int->Int)->(Int->Int)->[Int]->[Int]
othermap _ _ [] = []
othermap f g (x:xs)=
    if (length (x:xs) `mod` 2/=0)
        then (f x):othermap f g xs
    else
        (g x):othermap f g xs