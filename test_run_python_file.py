from functions.run_python_file import run_python_file

def run_test():
    # Testuje spustenie základného skriptu v pracovnom priestore.
    print(run_python_file("calculator", "main.py"))
    # Testuje, či sa skript dokáže spustiť s argumentmi.
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # Testuje spustenie iného skriptu z rovnakého priestoru.
    print(run_python_file("calculator", "tests.py"))
    # Testuje, či sa zablokuje pokus o spustenie súboru mimo povoleného adresára.
    print(run_python_file("calculator", "../main.py"))
    # Testuje spracovanie neexistujúceho súboru.
    print(run_python_file("calculator", "nonexistent.py"))
    # Testuje, či sa odmietne spustiť súbor, ktorý nie je Python skript.
    print(run_python_file("calculator", "lorem.txt"))
    
if __name__ == "__main__":
    run_test()