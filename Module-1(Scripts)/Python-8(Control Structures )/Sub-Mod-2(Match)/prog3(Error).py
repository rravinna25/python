# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #  Error :  case  _  can  not  be  in  the  middle  of  match
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
