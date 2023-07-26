import csv 

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

# load the entries with statement
def load_entries():
  entries = []
  with open(DATA_FILE, 'r') as csvfile: 
    reader = csv.DictReader(csvfile, FIELDNAMES)
    for row in reader:
      entries.append(row)
    return entries

# define functions
def view_previous_entries(entries):
  for entrie in entries: 
    print( ("entry['date']"), ("entry['transaction']"), ("entry['note']"))

# enter for profit loss 
def display_profit_loss(entries):
  income = 0 
  expenses = 0 

  for entry in entries:
    if entry['transaction'] == 'Income':
      income += int(entry['amount'])
    elif entry['transaction'] == 'Expense':
      expenses += int(entry['amount'])  


  print(f'The total income is ${income}')
  print(f'The total expenses are ${expenses}')
  print(f'The current profit is ${income - expenses}')


def add_new_entry(entries):
    date = input("Enter the date (yyyy-mm-dd): ")
    transaction = input("Enter the transaction type (Income or Expense): ")
    amount = input("Enter the amount: ")
    note = input("Enter a note: ")

    new_entry = {'date': date, 'transaction': transaction, 'amount': amount, 'note': note}
    entries.append(new_entry)

    with open(DATA_FILE, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)


def show_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Quit\n')

def get_menu_choice():
  choice = None
  
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError:
      print('That was not a valid number, please try again!')
      continue

    if choice < 1 or choice > 4:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_entries()

  while True:
    show_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      print('\nGoodbye!\n\n')
      break

if __name__ == '__main__':
  main()
