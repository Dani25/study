datatype mytype = TwoInts of int*int
		| Str of string
		| Pizza
		      
fun f (x:mytype) = (* f has type mytype -> int *)
  case x of
  Pizza => 3
  | TwoInts(i1,i2) => i1 + i2
  | Str s => 8
