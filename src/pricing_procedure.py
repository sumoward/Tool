#Brian Ward
#Principal Systems
#06/09/2012


"""
A class to generate the appropriate pricing structure
"""


class Pricing_procedure:

    def __init__(self):
        self.car_park = 0
        self.pricelist = {}
        self.currency = ''
        self.total = 0
        self.pricing_document = {}

        #        self.pricelist1={'In-DEX':17500,
#        'Radio_DataTerminal_Module':10000,
#        'Integration_Module':2500,
#        'Auto_Report_Scheduler':0,
#        'Additional_site _Licence':0,
#        'Digital_Signature_Capture':2500,
#        'Diary_Book_System':6000,
#        'InDEX_Document_Imaging_Scanning' :7500}

    def set_pricing(self, pricing_modifier, currency):

            self.car_park = pricing_modifier
            print('The pricing modifier is :', self.car_park)
            #'check the sales person analysis of the company
            self.currency = currency
            print('You are working in :', self.currency)
            #print(self.car_park)
            if self.car_park == 2:
                self.total_price()
            else:
                print('\nSorry no pricing model \
                exists for this type of company')

    """
      check which price ist to import
    """

    def pricelist_import(self,):

        filename = 'pricing_' + str(self.car_park) + '_\
        ' + self.currency + '.csv'

        filename = 'C:\eclipse for python\workspace\RECAP\src\static\pricing/' + filename
        print (filename, ' is the pricing list being imported')
        self.parse(filename)

    """
        parse the appropriate pricing document
    """

    def parse(self, filename):
        f = open(filename, 'r')
        for line in f.readlines():
            if line != '':
                line = line.strip()
                for i, char in enumerate(line):
                    if char == ',':
                        comma = i
                self.pricing_document[line[0:comma]] = line[comma + 1:]

        print('pricing doc :', self.pricing_document)

    def total_price(self):
        #the quantity of each price
        quantity = 1
        #print(self.pricing_document)

        for value in self.pricing_document.values():
            #print(value)
            value = value * quantity
            self.total = self.total + float(value)
        return self.pricing_document

    def price_print(self):
        print('\nThe Total cost of the project will be: ', self.total)
        return self.total

pricing1 = Pricing_procedure()
pricing1.set_pricing(2, 'euro')
pricing1.pricelist_import()
pricing1.total_price()
pricing1.price_print()

        

