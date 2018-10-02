import System.IO
import Control.Monad

main = do
          pila <- readFile "symbol.txt"
          let listaString = words pila
          print listaString
          
          writeFile "cima.txt" $ ( unwords $ (cima(apilar listaString)) )
          print ( unwords $ (cima(apilar listaString)) )
          
data Stack x = P String (Stack x)
             | Vacia
             
apilar :: [String] -> Stack x
apilar [] = Vacia
apilar (x:xs) = P x (apilar xs)

cima :: Stack x -> [String]
cima Vacia = error "ERROR"
cima (P x _) = [x]
