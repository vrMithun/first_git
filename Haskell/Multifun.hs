module Multifun (multifun) where

multifun :: (Fractional a,Num a)=>[(a->a)]->a->a
multifun [] val = val
multifun (x:xs) val= multifun xs (x val)