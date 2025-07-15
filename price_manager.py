# price_manager.py

from config import BASE_PRICE, CUSTOM_PASS_EXTRA, BACKUP_CODE_EXTRA, TWO_FA_EXTRA

def calculate_price(quantity, custom_pass, backup_code, two_fa):
    price = BASE_PRICE * quantity
    if custom_pass:
        price += CUSTOM_PASS_EXTRA * quantity
    if backup_code:
        price += BACKUP_CODE_EXTRA * quantity
    if two_fa:
        price += TWO_FA_EXTRA * quantity
    return round(price, 2)
