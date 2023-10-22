from scraper import Parser
if __name__ == '__main__':
    # my_parser = Parser(type_of_schedule='Departures', day='Today')
    # my_parser.run()
    my_parser = Parser(type_of_schedule='Departures', day='Tomorrow', city='Tir')
    my_parser.run()
    print(my_parser.list_of_flights)
    # my_parser.run()
    # my_parser = Parser(type_of_schedule='Departures', day='Yesterday')
    # my_parser.run()
    # my_parser = Parser(type_of_schedule='Arrivals', day='Today')
    # my_parser.run()
    # for flight in my_parser.all_flights:
    #     print(flight.text)
    # my_parser = Parser(type_of_schedule='Arrivals', day='Tomorrow')
    # my_parser.run()
    # my_parser = Parser(type_of_schedule='Arrivals', day='Yesterday')
    # my_parser.run()
