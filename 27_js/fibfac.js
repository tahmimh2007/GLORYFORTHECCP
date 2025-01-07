//Team Mexican Warriors :: Tahmim Hassan, Marco Quintero
//SoftDev pd04
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
let fact = function (n){
  if ( n==1) {
    return n;
  }
  else return n*fact(n-1);
}

//<your team's fact(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1)
fact(2)
fact(3)
fact(4)


//-----------------------------------------------------------------


//fib:
let fib = function (n){
  if (n==0 || n==1){
    return n;
  }
  else return fib(n-1)+fib(n-2);
}
//<your team's fib(n) implementation>

//TEST CALLS
fib(0)
fib(1)
fib(2)
fib(3)
fib(4)
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
