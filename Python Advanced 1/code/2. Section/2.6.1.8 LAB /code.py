# You are about to create a multifunction device (MFD) that 

# the system consists of a scanner and a printer;
# your task is to create blueprints for it and deliver 
# the implementations;

# create an abstract class representing a scanner that
# enforces the following methods:
# - scan_document – returns a string 
#   indicating that the document has been scanned;
# - get_scanner_status – returns information about 
#   the scanner (max. resolution, serial number)

# Create an abstract class representing a printer that 
# enforces the following methods:
# - print_document – returns a string indicating 
#   that the document has been printed;
# - get_printer_status – returns information 
#   about the printer (max. resolution, serial number)
from datetime import datetime
import abc

class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document():
        # just make the implementation read some input from a regular text file
        return "Returns some imaginary output from some document"

    @abc.abstractmethod
    def get_scanner_status():
        resolution = [1280, 720]
        serial_number = "1111-1111-1111"
        return 

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document():
        return "Document has been printed"

    @abc.abstractmethod
    def get_printer_status():
        resolution = [1280, 720]
        serial_number = "1111-1111-1111"
        return resolution, serial_number

# Create MFD1, MFD2 and MFD3 classes that inherit the 
# abstract classes responsible for scanning and printing:

# MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, 
# so device capabilities (resolution) should be low;
class MFD1(Printer, Scanner):
    resolution = [440, 220]
    serial_number = "34J3-434J-333F"
    def scan_document(self):
        return "The document has been scanned in poor quality"
    def print_document(self):
        return "The document has been printed in poor quality"
    def get_printer_status(self):
        device = "Printer"
        print("Status: The printer is clanking... much clanking")
        return device, MFD1.resolution, MFD1.serial_number 
    def get_scanner_status(self):
        device = "Scanner"
        print("Status: The scanners is clanking... much clanking")
        return device, MFD1.resolution, MFD1.serial_number
        
# MFD2 – should be a medium-priced device allowing additional operations 
# like printing operation history, and the resolution is better than the lower-priced device;
def logger(own_function):
    def internal_wrapper(self, *args, **kwargs):
        result = own_function(self, *args, **kwargs)

        date = datetime.now()
        self.history.append(
            f"{own_function.__name__} function ran. AT TIME: {date}"
        )

        return result

    return internal_wrapper

class MFD2(Printer, Scanner):
    resolution = [1280, 720]
    serial_number = "DEAD-BEEF-UWUF"

    def __init__(self):
        self.history = [f"Printer created at: {datetime.now()}"]
        
    @logger
    def scan_document(self):
        return "The document has been scanned in decent quality"

    @logger
    def print_document(self):
        return "The document has been printed in decent quality"

    @logger
    def get_printer_status(self):
        device = "Printer"
        print("Status: The printer is whooming... much whooming")
        return device, MFD2.resolution, MFD2.serial_number 

    @logger
    def get_scanner_status(self):
        device = "Scanner"
        print("Status: The scanners is whooming... much whooming")
        return device, MFD2.resolution, MFD2.serial_number

    @logger
    def print_history(self):
        for event in self.history:
            print(event)

# MFD3 – should be a premium device allowing additional operations like printing 
# operation history and fax machine. 
class MFD3(Printer, Scanner):
    resolution = [4096, 2048]
    serial_number = "6969-6969-6969"
    def scan_document(self):
        return "The document has been scanned in good quality"
    def print_document(self):
        return "The document has been printed in good quality"
    def get_printer_status(self):
        device = "Printer"
        print("Status: The printer is booming... much booming")
        return device, MFD3.resolution, MFD3.serial_number 
    def get_scanner_status(self):
        device = "Scanner"
        print("Status: The scanners is booming... much booming")
        return device, MFD3.resolution, MFD3.serial_number


mfd1 = MFD1()
print(mfd1.scan_document())
print(mfd1.print_document())
print(mfd1.get_printer_status())
print(mfd1.get_scanner_status())


mfd2 = MFD2()
print(mfd2.scan_document())
print(mfd2.print_document())
print(mfd2.get_printer_status())
print(mfd2.get_scanner_status())
print(mfd2.print_history())

mfd3 = MFD3()
print(mfd3.scan_document())
print(mfd3.print_document())
print(mfd3.get_printer_status())
print(mfd3.get_scanner_status())