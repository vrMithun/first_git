module RepeatUntil (repeatuntil) where

repeatuntil :: (Num a, Fractional a, Eq a)=>(a->a)->(a->Bool)->a->a
repeatuntil ffun sfun start=
    if sfun start
    then repeatuntil ffun sfun (ffun start)
    else start