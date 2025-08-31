module Limfilt (limfilt) where

limfilt :: (Int->Bool)->Int->[Int]->[Int]
limfilt _ _ [] = []
limfilt _ 0 list=list
limfilt f val (x:xs)=
    if f x
    then x:(limfilt f val xs)
    else
        limfilt f (val-1) xs