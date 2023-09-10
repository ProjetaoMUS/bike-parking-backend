from enum import Enum

class PaymentMethodChoices(Enum):
    CREDIT = "Credit Card"
    DEBIT = "Debit Card"
    CASH = "Cash"
    PIX = "Pix"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]