#Brian Ward
#Principal Systems
#06/09/2012


"""
A class to generate the appropriate pricing structure
"""


class Pricing_procedure:

    def __init__(self):
        self.car_park = 0
        self.currency = ''
        self.total = 0
        self.pricing_document = {}


    def set_pricing(self, currency):

            self.currency = currency
            #print('You are working in :', self.currency)
            #print(self.car_park)
            self.pricelist={'In-DEX Standard Version':    12500,
'In-DEX Enterprise Version':17500,
'In-DEX Third Party Logistics (3PL) Standard Version':17500,
'In-DEX Third Party Logistics (3PL) Enterprise Version':25000,
'Per Additional GUI/Desktop User - Concurrent User':2500,
'Per Additional RDT/Voice User - Concurrent User':1500,
'Per Additional Voice User - Concurrent User':1500,
'R D T (Radio Data Terminal - Scanning)':9500,
'Voice Module':9500,
'Integration Module':9500,
'Job Management':10000,
'Movex  IDB Integration Module':5000,
'Additional Site Licence - Per Physical Site':7500,
'Web Access - Includes 5 Named Accounts':7500,
'Number of Accounts - Web Module only - Per named Account':500,
'In-DEX After Imaging Resilience':5000,
'Digital Signature - Capture/attach customer signatures':5000,
'EDM - Electronic Document Management':5000,
'In-DEX Load Bay Scheduler':5000,
'PDF Mail - Automated email and fax':5000}

            return self.pricelist

#    def pricelist_import(self,):
#
#        filename = 'pricing_' + str(self.car_park) + '_\
#        ' + self.currency + '.csv'
#
#        filename = 'C:\eclipse for python\workspace\RECAP\src\static\pricing/' + filename
#        print (filename, ' is the pricing list being imported')
#        self.parse(filename)
#
#    """
#        parse the appropriate pricing document
#    """
#
#    def parse(self, filename):
#        f = open(filename, 'r')
#        for line in f.readlines():
#            if line != '':
#                line = line.strip()
#                for i, char in enumerate(line):
#                    if char == ',':
#                        comma = i
#                self.pricing_document[line[0:comma]] = line[comma + 1:]
#
#        print('pricing doc :', self.pricing_document)

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
        #print('\nThe Total cost of the project will be: ', self.total)
        return self.total


if __name__ == "__main__":
    pricing1 = Pricing_procedure()
    pricelist = pricing1.set_pricing('euro')
#pricing1.pricelist_import()
#pricing1.total_price()
#pricing1.price_print()



