grammar Objloc;

options {
	language=Python;
	output=AST;
	ASTLabelType=CommonTree;
}

tokens{
	NEWDEF;
}

file 
	:	defin+ 
	;

defin 
	:	a=NAME '@' b=NAME NEWLINE?-> ^(NEWDEF $a $b)
	;

//serverpath 
//	:	NAME '.' NAME
//	;

INT	:	'0'..'9'+ ;

NAME	:	('a'..'z'|'A'..'Z'|'_'|'.'|INT)+ ;

NEWLINE	:	'\r'? '\n' ;


COMMENT
    :   '\*' ( options {greedy=false;} : . )* '*/' {self.skip();}
    ;
    
LINE_COMMENT
    : '\\' ~('\n'|'\r')* '\r'? '\n' {self.skip();};


WS	:	(' '|'\t'|'\n'|'\r')+ {self.skip()}
	;
	
