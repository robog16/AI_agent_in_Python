from functions.get_files_info import get_files_info

def run_tests():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nResult for '/bin' directory:")
    # Odsadenie podľa zadania
    print(f"    {get_files_info('calculator', '/bin')}")

    print("\nResult for '../' directory:")
    print(f"    {get_files_info('calculator', '../')}")

if __name__ == "__main__":
    run_tests()