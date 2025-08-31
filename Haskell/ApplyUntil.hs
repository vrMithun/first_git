module ApplyUntil (applyUntil) where

applyUntil :: (Ord a,Eq a)=>(a -> Bool) -> (a -> a) -> a -> a
applyUntil f g val=
    if (not (f val))
    then applyUntil f g (g val)
    else
        val