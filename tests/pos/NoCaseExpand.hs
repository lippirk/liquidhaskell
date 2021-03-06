module NoCaseExpand where

-- time 3.6s w/ "--no-case-expand" flag VS  8.5 s w/o

{- LIQUID "--max-case-expand=0" @-}

data TokenType =
  Space | Keyword | Keyglyph | Layout | Comment | Conid | Varid |
  Conop | Varop   | String   | CChar   | Number  | Cpp   | Error |
  Definition


context ::  [(TokenType, String)] -> [(TokenType, String)]
context stream@((Keyglyph,"="):_) = stream
context stream@((Keyglyph,"=>"):_) = stream
context stream@((Keyglyph,"⇒"):_) = stream
context (_:stream) = context stream
context [] = []
