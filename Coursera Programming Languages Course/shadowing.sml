(*Exemples to demonstrate shadowing*)
val a = 10
	    (*a: int in static env and a-> 10 in dynamic env*)
val b = a * 2
		(*a->10,b-> 20*)
val a = 5(*this is not an assignment statement*)
(*a->5, b->20*)
val c = b	    
(*a->5, b->20, c->20*)

val d = a
	    (*..., d-> 5*)
val a = a+1
	      (*...,a->6*)
(*val g = f-3*)
	      
val f = a*2
