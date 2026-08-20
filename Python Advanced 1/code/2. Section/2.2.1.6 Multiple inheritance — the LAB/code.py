# Your task is to build a multifunction device (MFD) class consisting of methods 
# responsible for document scanning, printing, and sending via fax.

# The methods are delivered by the following classes:

#    scan(), delivered by the Scanner class;
#    print(), delivered by the Printer class;
#    send() and print(), delivered by the Fax class.


# wait was i supposed to make those custom classes myself to this
import Scanner
import Printer
import fax

class MDF_SFP:
    def scan():
        return Scanner.scan()
    
    def print():
        return Printer.print()

    def send():
        return Fax.send()


mfd1 = MDF_SFP()
mfd2 = MDF_SFP()

mfd1.scan()
mfd1.print()
mfd1.send()

mfd2.scan()
mfd2.print()
mfd2.send()
