import System.IO
import Control.Monad

main = do
          pila <- readFile "numeros.txt"
          let listaString = words pila
          print listaString
          
          writeFile "numeros.txt" $ ( unwords $ (aString(desapilar(listaString))) )
          print ( unwords $ (aString(desapilar(listaString))) )
          
data Stack x = P String (Stack x)
             | Vacia

apilar :: [String] -> Stack x
apilar [] = Vacia
apilar (x:xs) = P x (apilar xs)
             
desapilar :: [String] -> Stack x
desapilar [] = Vacia
desapilar (x:xs) = apilar(xs)

aString :: Stack x -> [String]
aString Vacia = []
aString (P x xs) = ([x] ++ aString(xs))
