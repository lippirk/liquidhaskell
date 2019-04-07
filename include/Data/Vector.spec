module spec Data.Vector where

import GHC.Base

data variance Data.Vector.Vector covariant


measure vlen    :: forall a. (Data.Vector.Vector a) -> Int

invariant       {v: Data.Vector.Vector a | 0 <= vlen v } 

!           :: forall a. x:(Data.Vector.Vector a) -> vec:{v:Nat | v < vlen x } -> a 

unsafeIndex :: forall a. x:(Data.Vector.Vector a) -> vec:{v:Nat | v < vlen x } -> a 

fromList  :: forall a. x:[a] -> {v: Data.Vector.Vector a  | vlen v = len x }

length    :: forall a. x:(Data.Vector.Vector a) -> {v : Nat | v = vlen x }

replicate :: n:Nat -> a -> {v:Data.Vector.Vector a | vlen v = n} 

imap :: (Nat -> a -> b) -> x:(Data.Vector.Vector a) -> {y:Data.Vector.Vector b | vlen y = vlen x }

map :: (a -> b) -> x:(Data.Vector.Vector a) -> {y:Data.Vector.Vector b | vlen y = vlen x }

head :: forall a. {xs:Data.Vector.Vector a | 0 < vlen xs} -> a

last :: forall a. {xs:Data.Vector.Vector a | 0 < vlen xs} -> a

iscanl' :: (Int -> a -> b -> a) -> a -> xs:(Data.Vector.Vector b) -> {ys:Data.Vector.Vector a | 1 + vlen xs == vlen ys}

postscanl' :: (a -> b -> a) -> a -> xs:(Data.Vector.Vector b) -> {ys:Data.Vector.Vector a | vlen xs == vlen ys}

splitAt
    :: n  : Nat
    -> xs : {xs: Data.Vector.Vector a | 0 <= vlen xs && vlen xs < n}
    -> ( { l : Data.Vector.Vector a | vlen l == n }
       , { r : Data.Vector.Vector a | vlen r == vlen xs - n }
       )

drop :: n:Nat -> xs:(Data.Vector.Vector a) -> {ys:Data.Vector.Vector a | vlen ys == vlen xs - n}
