from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass 
    def receipt(self):
        print("Receipt generated") 
class CreditCardPayment(Payment):
    def process(self):
        print("Processing credit card payment")
payment = CreditCardPayment()
payment.process()
payment.receipt()
