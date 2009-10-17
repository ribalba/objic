grammar Expr;

//Some options for the generator
options {
	language=Java;
	output=AST;
	ASTLabelType=CommonTree;
}

//Tokens for the AST (see bottom for more)
tokens {
	BLOCK;
	EQ;
	PARAMS;
	NEWOBJ;
	CALL;
	IFTEST;
	CLASS;
	PTRASS;
	BOOL;
	WHILE;
	BREAK;
	DOWHILE;
	ELSE;
	PRINTSTM;
	OSTRING;
	SERVERNAME;
	METHDEF;
	DEBUGFLAG;
	RETURNSTM;
}

//Every program has one class 
prog	: classdef ;

// A class is defined through the class keyword, name and a block
// Ex  : class test { print ("hello") }
classdef 
	: 	'class' NAME  block    -> ^(CLASS NAME block )
	;

//A block is alwasy encapsulated between { and } and has n statements
block 
	:	'{'  (   stat  )*  '}' -> ^(BLOCK stat*)
	;
	
//A list of all the different statements there can be in a block
stat	
	:	iftest  
	|	methdef
	|	forloop
	| 	newvar
	|	call
	| 	block
	|	whileloop
	|	loopbreak
	|	printstm
	|	returnstm
	|	NEWLINE
	;

//Handels a return in the code
//Ex : return(a) 
returnstm
	: 	'return' '(' NAME ')' -> ^( RETURNSTM NAME)
	;

//Defines a new method in a class
// Ex : def printHelp { print ("HELP") }
methdef
	:	'def' NAME block -> ^(METHDEF NAME block)
	;

//A soimple mehtod call 
// Ex : object.add(otherobject)
call 
	:	a=NAME '.' b=NAME paramlist -> ^(CALL $a $b paramlist)
	;

//The print statement
//Ex : print("This is printed")
printstm
	:	'print' '(' printparams ')' -> ^(PRINTSTM printparams)
	;

//A list of things that can be printed
printparams
	:	call
	|	NAME
	|	STRINGTPL -> ^(OSTRING STRINGTPL)
	;

//The definition of a while loop
//Ex : while (a.value() == a.value()){print ("looping")}
whileloop
	:	'while' '(' boolexp ')' a=block -> ^(WHILE boolexp $a)
	;

//The break statement to stop executing a loop
loopbreak	
	:	'break' -> ^(BREAK)
	;

//The if definition
//Ex : if (a.value() == b.value()){
//	print("equa")
//	}else{
//	print("not equal")}
iftest 	:	'if' '(' boolexp ')' a=block ('else' b=block)? ->
			 ^(IFTEST boolexp $a ( ELSE $b)?) 
	;

//Defines a new variable ptr, 3 main different possibilities
//Ex : a = new Int()
newvar
	:	a=NAME '=' 'new' b=NAME paramlist ('@' servername)? ->
			 ^(EQ  $a NEWOBJ (servername)?  $b paramlist)
	|	a=NAME '=' b=NAME -> ^(EQ  $a PTRASS $b )
	|	NAME '=' call -> ^(EQ  NAME call )
	; 

//Defines a for loop quite clever as it creates the AST for an while loop
//they byte-code doesn't know what a for is 
forloop
	:	'for' '('  a=newvar ';' boolexp ';'  b=newvar ')' block ->
			 ^(BLOCK $a ^(WHILE  boolexp ^(BLOCK block $b)))
	;

//A boolean expression used in while and if
boolexp 
	:
	|	a=booltype cmp_operator b=booltype ->
			 ^(BOOL cmp_operator $a $b)
	;

//A list of comparement operators that are valid
cmp_operator
	: '=='
	| '!='
	| '<='
	| '>='
	| '<'
	| '>'
	;

//A boolena type can be a call or a method objcect
booltype
	:	call
	|	NAME
	;

//Defines how parameters should look like
paramlist 
	:	'(' ( atom  (',' atom)* )?  ')' -> ^(PARAMS atom* )
	;

//Defines the syntax for a server 
//Ex : ptrtovoid.net
servername 
	:	a=NAME '.' b=NAME -> ^(SERVERNAME $a  '.' $b)
	;

//The smallest entity
atom	
	:	INT
	|	NAME
	|	STRINGTPL
	;


// MORE TOKENS

INT	:	('+' | '-')? '0'..'9'+ 
	;


NAME	:	('a'..'z'|'A'..'Z'|'_'|INT)+ 
	;

STRINGTPL
	:	('"' (~'"')* '"')
	;

NEWLINE	:	'\r'? '\n' ;


COMMENT
    :   '\*' ( options {greedy=false;} : . )* '*/' {skip();}
    ;
    
LINE_COMMENT
    : '\\' ~('\n'|'\r')* '\r'? '\n' {skip();};


WS	:	(' '|'\t'|'\n'|'\r')+ {skip();} ;


