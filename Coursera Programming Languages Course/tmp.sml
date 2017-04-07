syntax:
     if e1 then e2 else e3
     where if, then, and else are keywords and
     e1,e2,e3 are subexpressions

Type-checking:
     first e1 must have type bool
     e2 and e3 can have any type (let`s call it t)
     but they must have the same type t
     the type of the entire expression is also t

Evaluation rules:                                                                                   first evaluate e1 to a value call it v1                                                        if it`s true, evaluate e2 and that result is the whole expression`s result                     else, evaluate e3 and that result is the whole expression`s result 


(*********************************************************************************************) syntax:                                                                                              if e1<e2 then e3 else e4                                                                       where if, then and else are keywords                                                           and e1,e2,e3,e4 are subexpressions                                                       Type-checking:                                                                                       a1<e2 must have bool type                                                                      e3 and e4 have any type, but must have the same type                                           so the type of entire expression will be also the same type of e3 or e4                  Evaluation rules:                                                                                    evaluate e1<e2 to a value call it v1                                                           if v1 it`s true, evaluate e3 and that result is the whole expression`s result                  else, evaluate e4 and that result is the whole expression`s result
