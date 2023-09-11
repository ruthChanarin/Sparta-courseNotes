
class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []
    
    def order(self, item:str, price:float, quantity:int=1):

        new_order = {
            'item': item,
            'price': price,
            'quantity': quantity
            }
        
        first_time_ordering_item = True

        for existing_order in self.bill:
            if new_order == existing_order:
                existing_order['quantity'] += new_order['quantity']
                first_time_ordering_item = False

        if first_time_ordering_item:
            self.bill.append(new_order)


    def remove(self, item:str, price:float, quantity:int=1):

        new_order = {
            'item': item,
            'price': price,           
            'quantity': quantity
            }

        for existing_order in self.bill: 
            if new_order['item'] == existing_order['item']:
                if existing_order['quantity'] >= new_order['quantity']:
                    existing_order['quantity'] -= new_order['quantity']
                    if new_order['quantity'] == 0:
                         self.bill.remove(existing_order)

            
    def get_subtotal(self):

        subtotal = 0

        for order in self.bill:
            subtotal += order['price'] * order['quantity']
            formatted_subtotal = format(subtotal, '.2f')

        return formatted_subtotal
    
    def get_total(self, service_charge:int=0.10):
        
        total = {
            'Sub Total': '',
            'Service Charge': '',
            'Total': ''
        }

        sub_total = float(self.get_subtotal())
        formatted_sub = format(sub_total, '.2f')
        total['Sub Total'] = f'£{formatted_sub}'

        service_charge = round((sub_total * float(service_charge)),2)
        total['Service Charge'] = f'£{service_charge}'
        
        final_total = sub_total + service_charge
        total['Total'] = f'£{final_total}'


        return total
    
    def split_bill(self):

        subtotal = float(self.get_subtotal())

        diners = self.number_of_diners

        charge_per_person = subtotal/diners
        rounded_charge_per_person = round(charge_per_person,2)


        return rounded_charge_per_person


