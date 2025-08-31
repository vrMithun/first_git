module PartitionWithLimit (partitionWithLimit) where

partitionWithLimit :: Int->[Int]->[[Int]]
partitionWithLimit _ [] = []
partitionWithLimit val list= (take val list) : partitionWithLimit val (drop val list)