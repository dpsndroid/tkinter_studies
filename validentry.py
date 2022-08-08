class Validators():
    def validate_entry2(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99