module Example where

import           Data.Vector as V

badFunc :: Int -> Int
badFunc x = undefined

myHead :: Vector Int -> Int
myHead xs = V.head xs
