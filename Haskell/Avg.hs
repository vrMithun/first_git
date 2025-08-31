module Avg (avg) where

avg :: [(String,Int)]->Int->Int->Int
avg [] c l=c `div` l
avg (x:xs) c l= avg xs (c+snd x) (l+1)
