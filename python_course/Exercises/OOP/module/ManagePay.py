class PaymentManager:
    
    def process_payment(self, payment_method, amount: float):
        return payment_method.process_payment(amount)