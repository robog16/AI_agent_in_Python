from functions.write_file import write_file

def run_test():
    # Testuje prepísanie existujúceho súboru v pracovnom priestore.
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # Testuje vytvorenie nového súboru v podadresári.
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # Testuje, či sa zablokuje pokus o zápis mimo povoleného adresára.
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    
if __name__ == "__main__":
    run_test()