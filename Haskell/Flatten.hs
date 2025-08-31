module Flatten (flatten) where

flatten :: [[a]]->[a]
flatten [] = []
flatten list = foldl (++) [] list 