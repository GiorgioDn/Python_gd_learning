from .module.ManagePay import GestorePagamenti
from .module.Pay import *
from .module.PayMethod import *

def main():
    while True:
        
        print("\n Selezionare il metodo di pagamento")
        print("1. Carta di Credito")
        print("2. Paypal")
        print("3. Iban")
        print("4. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                numero_carta = input("Numero della carta: ")
                data = input("Data di scadenza: ")
                cvv = int(input("cvv: "))
                
                carta = CartaDiCredito(numero_carta, data, cvv)
                
                importo = float(input("selezionare l'importo: "))
                pay = GestorePagamenti()
                print(pay.pagamento(carta, importo))
            case 2:
                account = input("Email account: ")
                
                paypal = PayPal(account)
                
                importo = float(input("selezionare l'importo: "))
                pay = GestorePagamenti()
                print(pay.pagamento(paypal, importo))
            case 3:
                iban = input("Iban: ")
                swift = input("Swift: ")
                
                conto = BonificoBancario(iban, swift)
                
                importo = float(input("selezionare l'importo: "))
                pay = GestorePagamenti()
                print(pay.pagamento(conto, importo))
            case 4:
                break
            case _:
                print("Scelta non valida")

if __name__ == "__main__":
    main()
else: 
    print("È stato importato")