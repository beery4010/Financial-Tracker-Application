class Utils:
    @staticmethod
    def currency_format(amount: float) -> str:
        """
        Format a currency string to a more readable format.
        """
        return f"Rs. {amount:,.2f}"
    @staticmethod
    def reverse_currency_format(amount: str) -> float:
        """
        Reversing the currency format from str to float
        """
        return float(amount.replace("Rs.", "").replace(",", "").strip())
