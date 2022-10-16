import math

def suma(  num_1, num_2 ):
	answ = [ num_1[ 0 ] + num_2[ 0 ],
			 num_1[ 1 ] + num_2[ 1 ] ]
	return answ


def sub( num_1, num_2 ):
	answ = [ num_1[ 0 ] - num_2[ 0 ],
			 num_1[ 1 ] - num_2[ 1 ] ]
	
	return answ

def multi_vectors(  num_1, num_2 ):
	answ = [ num_1[ 0 ] * num_2[ 0 ] - num_1[ 1 ] * num_2[ 1 ],
			  num_1[ 1 ] * num_2[ 0 ] + num_1[ 0 ] * num_2[ 1 ] ]
	
	return answ

def divComplexNumber(   num_1, num_2 ):
	div = ( num_2[0] ) **2 + ( num_2[1] ) **2
	
	try :
		answ =[ ( num_1[ 0 ] * num_2[ 0 ] + num_1[ 1 ] * num_2[ 1 ] )/div,
			   ( num_2[ 0 ] * num_1[ 1 ] - num_1[ 0 ] * num_2[ 1 ] ) /div ]

		return answ
		
	except ZeroDivisionError as error :
		print('Se produjo el siguiente error',error)
	
def conjugated( complexNumber ):
	answ = [ complexNumber[ 0 ], -complexNumber[ 1 ]]
	return answ

def module( complexNumber ):
	answ = math.sqrt( (complexNumber[ 0 ])**2 + (complexNumber[ 1 ]) **2 )
	return answ

def phase( complexNumber ):
        x, y = complexNumber[ 0 ], complexNumber[ 1 ]

        if ( x < 0 and y < 0 ) or ( x < 0 and y >= 0 ):
                return math.pi + (  math.atan( complexNumber[ 1 ] / complexNumber[ 0 ] ) ) 
        
        elif x >= 0 and y < 0:
                return 2 * math.pi +  (  math.atan( complexNumber[ 1 ] / complexNumber[ 0 ] ) ) 

        else:
                return  (  math.atan( complexNumber[ 1 ] / complexNumber[ 0 ] ) ) 
                
        

def cartesianToPolar( complexNumber ):
	angle = phase( complexNumber  )
	answ = [ module( complexNumber) ,
			angle ]
	return answ 