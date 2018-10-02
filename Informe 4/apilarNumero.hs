import System.IO
import Control.Monad

main = do
          pila <- readFile "numeros.txt"
          let listaString = words pila
          print listaString
          
          elem <- readFile "elem.txt"
          writeFile "numeros.txt" $ ( unwords $ (aString(apilar((words elem) ++ listaString))) )
          print ( unwords $ (aString(apilar((words elem) ++ listaString))) )
          
data Stack x = P String (Stack x)
             | Vacia
             
apilar :: [String] -> Stack x
apilar [] = Vacia
apilar (x:xs) = P x (apilar xs)

aString :: Stack x -> [String]
aString Vacia = []
aString (P x xs) = ([x] ++ aString(xs))
