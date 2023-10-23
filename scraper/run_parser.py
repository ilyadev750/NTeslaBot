from scraper import Parser
if __name__ == '__main__':
    my_parser = Parser(type_of_schedule='Departures', day='Tomorrow', city='Tir')
    my_parser.run()

