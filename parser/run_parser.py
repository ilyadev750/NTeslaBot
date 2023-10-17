from parser.parser import Parser


my_parser = Parser(type_of_schedule='Departures', day='Today')
my_parser.run()
# my_parser = Parser(type_of_schedule='Departures', day='Tomorrow')
# my_parser.run()
# my_parser = Parser(type_of_schedule='Departures', day='Yesterday')
# my_parser.run()
# my_parser = Parser(type_of_schedule='Arrivals', day='Today')
# my_parser.run()
# my_parser = Parser(type_of_schedule='Arrivals', day='Tomorrow')
# my_parser.run()
# my_parser = Parser(type_of_schedule='Arrivals', day='Yesterday')
# my_parser.run()