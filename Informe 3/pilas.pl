%------PILAS------%

pila_vacia([]).

apilar(E,[],[E]):-!.
apilar(E,Xs,[E|Xs]).

desapilar(_,[]):-false.
desapilar([_|Xs],Xs).

cima([],_):-false.
cima([X|_],X).

es_pila_vacia([]):-true.

profundidad([],X):- X is 0.
profundidad([_|Xs],L):- profundidad(Xs,R), L is R + 1.

fondo([],_):-false.
fondo([X],X):-!.
fondo([_|Xs],E):- fondo(Xs,E).


apilar_inversa([],Xs,Xs).
apilar_inversa([X|Xs],Ys,Zs):- apilar(X,Ys,R), apilar_inversa(Xs,R,Zs).


inversa([],[]):-!.
inversa(Xs,R):- apilar_inversa(Xs,[],R),!.

duplicar([],[]):-!.
duplicar([X|Xs],Ys):- duplicar(Xs,R), apilar(X,[X|R],Ys).

concatenar(Xs,[],Xs):-!.
concatenar(Xs,[Y|Ys],Zs):- concatenar(Xs,Ys,R), apilar(Y,R,Zs).

entremezclar(Ys,[],Ys):-!.
entremezclar([],Ys,Ys):-!.
entremezclar([X|Xs],[Y|Ys],[X,Y|L]):-	entremezclar(Xs,Ys,L), profundidad(Xs,A), profundidad(Ys,B), A >= B, !.
entremezclar([X|Xs],[Y|Ys],[Y,X|L]):-	entremezclar(Xs,Ys,L), profundidad(Xs,A), profundidad(Ys,B), A < B, !.

%--------SECUENCIAS----------
crear([],Xs,Xs):-!.
crear([X|Xs],Ys,R):- apilar(X,Ys,L), crear(Xs,L,R).

insertar(Xs,Ys,E,R):- apilar(E,Xs,L), crear(L,Ys,R).

eliminar(_,[],false):-!.
eliminar(Xs,[_|Ys],R):-  crear(Xs,Ys,R).

actual(_,[],false):-!.
actual(_,[Y|_],Y).

avanzar(_,[],false):-!.
avanzar(Ys,[X|Xs],R):- crear([X|Ys],Xs,R).

reiniciar([],Ys,R):- crear([],Ys,R).
reiniciar([X|Xs],Ys,R):- apilar(X,Ys,L), reiniciar(Xs,L,R).

fin(_,[],true).

es_sec_vacia([],[],true).
