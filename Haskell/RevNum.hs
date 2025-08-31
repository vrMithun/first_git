module RevNum (revnum) where


revd :: Int -> Int -> Int
revd x rev = 
  if x == 0 
  then rev  
  else revd (x `div` 10) (rev * 10 + x `mod` 10)  

revnum :: Int -> Int
revnum x = revd x 0

