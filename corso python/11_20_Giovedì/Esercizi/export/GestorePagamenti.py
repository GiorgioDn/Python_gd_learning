class GestorePagamenti:
    
    def pagamento(self, pagamento, importo:float):
        return pagamento.effettua_pagamento(importo)