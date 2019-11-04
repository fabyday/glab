refactoring rule

naming rule
	use CamelCase
		ex ) 
			class name : 
				TestClass():
			variables :
				minScope

			functions : 
				addVariables(...)


variables
	form : {access modifier}{prefix}{variable_name}
	access modifier { __, _ ,{nothing} } :
		_         : protected variables in class 
		__        : private variables in class or file scope variables
		{nothing} : public methods or functions
	prefix : {g, s}
		g         : for global variables.
		s         : static variables in class.
	variable_name : 
		explicit name to represent the variable


functions or meothods
	form : {access modifier}{prefix}{action verb}{Object}
	
	access modifier : { __, _, {nothing} }
		__        : private method in class or file scope functions.
		_         : protected method in class 
		{nothing} : public methods or functions
	
	prefix			: {}
	action verb		: {add, remove, set, get, read, write, is}
		add		:	when using iterable datastructure like list, dict, etc.
		remove	:	when using iterable datastructure like list, dict, etc.
		next 		: get next element from iterable object.
		set		:	set flag or set variables value.
		get		:	get a flag value or get a variables value.
		read	:	smillar like a file I/O
		write	:
		is		:
		
		

	
