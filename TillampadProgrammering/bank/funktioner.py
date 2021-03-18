import config

# Beräknar saldo på ditt konto
def saldo():
    saldo = 0 
    for t in transactions:
        saldo += t
    return saldo


# Skriver ned alla transaktioner
def print_transactions():   
    line = 0
    summa = 0
    output = ("\n<=>   Transaktioner   <=>"
              "\n{:>3} {:>12} {:>12}"
              "\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖").format("Nr", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    
    return output

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

# Den kollar så att filen är tillgänglig. Är den inte det skapas en ny
def check_file_exists():
    try:
        with open(filename, "x"):
            print("Filen har skapats")

        with open(filename, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

# Den läser upp filens innerhåll
def read_file():
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
            
# Lagrar transaktioner till en lista
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

# Skriver transaktionen till filen
def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))
