from functions.get_files_info import get_files_info

def run_tests():
    # Testuje výpis obsahu aktuálneho adresára.
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    # Testuje výpis obsahu podadresára pkg.
    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    # Testuje, či sa správne zablokuje pokus o čítanie mimo povoleného priestoru.
    print("\nResult for '/bin' directory:")
    # Odsadenie podľa zadania
    print(f"    {get_files_info('calculator', '/bin')}")

    # Testuje, či sa zablokuje cesta vyššie v adresárovej štruktúre.
    print("\nResult for '../' directory:")
    print(f"    {get_files_info('calculator', '../')}")

if __name__ == "__main__":
    run_tests()