module ApplyNTimes (applyNTimes) where


applyNTimes :: Int -> (a -> a) -> a -> a
applyNTimes 0 _ val = val
applyNTimes n f val = applyNTimes (n-1) f (f val)