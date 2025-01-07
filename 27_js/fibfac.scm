;Team Phantom Tollbooth :: Tahmim Hassan, Marco Quintero
;SoftDev pd04
;K27 - Basic functions in JavaScript
;2025-01-06m

;Scheme antecedents for JavaScript work


;factorial:
(define fact (lambda (n)
  (if (= n 1)
    n
    (* n fact(- n 1)))))
;<your team's fact(n) implementation>

;TEST CALLS
(fact 1) ;"...should be  1"
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;-----------------------------------------------------------------


;fib:
;<your team's fib(n) implementation>

(define fib(lambda (n)
  (if (= n 0)
    n
    (if (= n 1)
      n
      (+ fib((- n 1)) fib((- n 2)))))))
;<your team's fib(n) implementation>

;TEST CALLS
(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"

;=================================================================
