path_to_bot = ""
import sikuli.Sikuli


class DataStorage(object):
    #object that will handle exporting transaction history
    #you must have the program that you want to send the transaction to, open
    #methods of storage being considered, xml, excel, mysql
    
    def __init__(self, program):
        """ program parameter is the format to write the file in, e.g. Notepad, or Excel"""
        self._program = program
        
    def write(self, transaction):
        #write the transaction record to a text file
        transaction_file = open(path_to_bot + "transaction_records/transactions.txt", "w")
        current_transaction = self.convert_trans_to_string(transaction)
        #now write the transaction to the file
        
    def convert_trans_to_string(self, transaction):
        """takes the transaction variable created in Session class and converts it to string"""
        #note, repr will not work because it doesn't remove curly brackets and colons
        record_list = []
        for mode, trans in transaction.iteritems():
            record_list.append(str("mode: " + mode + "  "))
            for product,quantity in trans.iteritems():
                record_list.append(str(product + ":"))
                record_list.append(str(quantity) + " ")
            
        record_string = "".join(record_list) + "\n"
        return record_string