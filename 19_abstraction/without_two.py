# Implementations -> Companies who wants to manufacture laptops 

# Dell Wants To Build Laptops

from without_one import Laptop

class Dell(Laptop):
    def should_have_processor(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("Processor")
        print("Functionality")
        print("Present") 

    def should_have_ram(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("RAM")
        print("Functionality")
        print("Present")
        
    # NOTE: Dell Doesn't have Hard Disk adn Wifi Functionalities, 
    # But Still will be able to sell laptops 
    

# Without Abstraction - End User Is Seeing Unnecessary Details (NOT RECOMMENDED)

# End User Buying Dell Laptop
print("=" * 30)
print("     Customer Buying Dell Laptop")
print("=" * 30)

dell_object = Dell()

dell_object.should_have_processor()
dell_object.should_have_ram()

