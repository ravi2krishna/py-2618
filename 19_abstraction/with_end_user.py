# With Abstraction - End User Is Seeing Only necessary Details  (RECOMMENDED)

# End User Buying Dell Laptop
print("=" * 30)
print("     Customer Buying Dell Laptop")
print("=" * 30)

from with_two import Dell

dell_object = Dell()

dell_object.should_have_processor()
dell_object.should_have_ram()
# TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 'should_have_hard_disk', 'should_have_network'
dell_object.should_have_hard_disk()
dell_object.should_have_network()

# atm_object = ATM()
# atm_object.check_balance()
# atm_object.withdraw()
# atm_object.get_statement()
# atm_object.change_pin()