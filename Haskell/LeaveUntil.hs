module LeaveUntil (leaveuntil) where

leaveuntil :: (Int->Bool)->[Int]->[Int]
leaveuntil _ [] = []
leaveuntil f (x:xs)=
    if f x
        then (x:xs)
    else
        leaveuntil f xs