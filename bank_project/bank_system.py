from bank_function.bank_storage import BankStorage
from bank_function.bank_personal import BankPersonal
from bank_function.bank_account import BankAccount
from bank_util.bank_interface import BankInterface
from bank_util.bank_main import Main

if __name__ == "__main__":
    storage = BankStorage("bank.json")
    per = BankPersonal(storage)
    acc = BankAccount(storage, per)
    main = Main(per, acc)
    ui = BankInterface(per, acc, main)
    ui.main_interface()