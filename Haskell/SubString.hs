module SubString (substring) where

substring :: String->String->IO()
substring [] _=print("no")
substring a b
    |take (length b) a==b =print("yes")
    |otherwise = substring (tail a) b
