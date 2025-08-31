module Reverse (rev) where

rev :: [Int]->[Int]
rev []=[]
rev (x:xs)=rev xs ++ [x]