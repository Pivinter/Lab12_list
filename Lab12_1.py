class InvalidSurnameError(Exception):
    pass

class InvalidNameError(Exception):
    pass

class InvalidPhoneNumberError(Exception):
    pass

class InvalidBirthDateError(Exception):
    pass

class Note:
    def __init__(self, surname, name, phone_number, birth_date):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.birth_date = birth_date

def days_in_month(month, year):
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return 29
        else:
            return 28
    else:
        return 31

def input_data():
    while True:
        try:
            surname = input("Введіть прізвище: ")
            if not surname:
                raise InvalidSurnameError("Прізвище не може бути порожнім.")
            name = input("Введіть ім'я: ")
            if not name:
                raise InvalidNameError("Ім'я не може бути порожнім.")
            phone_number = input("Введіть номер телефону: ")
            if not phone_number:
                raise InvalidPhoneNumberError("Номер телефону не може бути порожнім.")
            birth_date = list(map(int, input("Введіть день народження (дд/мм/рррр): ").split('/')))
            if len(birth_date) != 3:
                raise InvalidBirthDateError("День народження повинен складатися з трьох чисел, розділених символом '/'.")
            day, month, year = birth_date
            if not (1 <= month <= 12):
                raise InvalidBirthDateError("Місяць повинен бути від 1 до 12.")
            if not (1 <= day <= days_in_month(month, year)):
                raise InvalidBirthDateError(f"День народження повинен бути від 1 до {days_in_month(month, year)} для місяця {month}.")
            return Note(surname, name, phone_number, birth_date)
        except InvalidSurnameError as e:
            print(e)
        except InvalidNameError as e:
            print(e)
        except InvalidPhoneNumberError as e:
            print(e)
        except InvalidBirthDateError as e:
            print(e)
        except ValueError:
            print("День народження повинен складатися з трьох чисел, розділених символом '/'.")


def add_note(notes):
    notes.append(input_data())
    print("Запис успішно додано!")

def view_notes(notes):
    for note in notes:
        print(f"{note.surname} {note.name}, телефон: {note.phone_number}, дата народження: {note.birth_date[0]}/{note.birth_date[1]}/{note.birth_date[2]}")

def save_notes_to_file(notes, filename):
    with open(filename, 'w') as f:
        for note in notes:
            f.write(f"{note.surname},{note.name},{note.phone_number},{','.join(map(str, note.birth_date))}\n")
    print("Записи збережено в файл.")

def load_notes_from_file(filename):
    try:
        with open(filename, 'r') as f:
            notes = []
            for line in f.readlines():
                values = line.strip().split(',')
                if len(values) != 6:
                    continue
                surname, name, phone_number = values[:3]
                birth_date = list(map(int, values[3:]))
                notes.append(Note(surname, name, phone_number, birth_date))
        print("Записи завантажено з файлу.")
        return notes
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []


def find_note_by_criteria(notes, search_by, value):
    if search_by == 'name':
        attribute = 'name'
    elif search_by == 'phone_number':
        attribute = 'phone_number'
    elif search_by == 'birth_date':
        attribute = 'birth_date'

    result = []
    for note in notes:
        if getattr(note, attribute) == value:
            result.append(note)
    return result

def sort_notes(notes, sort_by, reverse=False):
    if sort_by == 'name':
        attribute = 'name'
    elif sort_by == 'phone_number':
        attribute = 'phone_number'
    elif sort_by == 'birth_date':
        attribute = 'birth_date'

    notes.sort(key=lambda x: getattr(x, attribute), reverse=reverse)
    print(f"Записи відсортовані за {sort_by}.")

def remove_note_by_criteria(notes, search_by, value):
    if search_by == 'name':
        attribute = 'name'
    elif search_by == 'phone_number':
        attribute = 'phone_number'
    elif search_by == 'birth_date':
        attribute = 'birth_date'

    removed_count = 0
    notes_copy = notes.copy()
    for note in notes_copy:
        if getattr(note, attribute) == value:
            notes.remove(note)
            removed_count += 1

    if removed_count:
        print(f"Видалено {removed_count} записів.")
    else:
        print("Записів з таким критерієм не знайдено.")

def search_menu():
    while True:
        print("1. Шукати за ім'ям")
        print("2. Шукати за номером телефону")
        print("3. Шукати за датою народження")
        print("0. Назад")

        choice = input("Введіть номер операції: ")

        if choice == '1':
            return 'name', input("Введіть ім'я: ")
        elif choice == '2':
            return 'phone_number', input("Введіть номер телефону: ")
        elif choice == '3':
            value = list(map(int, input("Введіть день народження (дд/мм/рррр): ").split('/')))
            return 'birth_date', value
        elif choice == '0':
            return None, None
        else:
            print("Невірний вибір, спробуйте ще раз.")

def sort_menu():
    while True:
        print("1. Сортувати за ім'ям")
        print("2. Сортувати за номером телефону")
        print("3. Сортувати за датою народження")
        print("4. Сортувати за ім'ям в зворотньому порядку")
        print("5. Сортувати за номером телефону в зворотньому порядку")
        print("6. Сортувати за датою народження в зворотньому порядку")
        print("0. Назад")

        choice = input("Введіть номер операції: ")

        if choice in ('1', '2', '3'):
            return ('name', False) if choice == '1' else ('phone_number', False) if choice == '2' else ('birth_date', False)
        elif choice in ('4', '5', '6'):
            return ('name', True) if choice == '4' else ('phone_number', True) if choice == '5' else ('birth_date', True)
        elif choice == '0':
            return None, None
        else:
            print("Невірний вибір, спробуйте ще раз.")

def remove_menu():
    while True:
        print("1. Видалити за ім'ям")
        print("2. Видалити за номером телефону")
        print("3. Видалити за датою народження")
        print("0. Назад")

        choice = input("Введіть номер операції: ")

        if choice == '1':
            return 'name', input("Введіть ім'я: ")
        elif choice == '2':
            return 'phone_number', input("Введіть номер телефону: ")
        elif choice == '3':
            value = list(map(int, input("Введіть день народження (дд/мм/рррр): ").split('/')))
            return 'birth_date', value
        elif choice == '0':
            return None, None
        else:
            print("Невірний вибір, спробуйте ще раз.")

notes = []

while True:
        print("1. Додати запис")
        print("2. Видалити запис")
        print("3. Переглянути записи")
        print("4. Сортувати записи")
        print("5. Знайти запис")
        print("6. Зберегти записи в файл")
        print("7. Завантажити записи з файлу")
        print("0. Вихід")

        choice = input("Введіть номер операції: ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
                search_by, value = remove_menu()
                if search_by:
                    remove_note_by_criteria(notes, search_by, value)
        elif choice == '3':
            view_notes(notes)
        elif choice == '4':
            sort_by, reverse = sort_menu()
            if sort_by:
                sort_notes(notes, sort_by, reverse)
        elif choice == '5':
            search_by, value = search_menu()
            if search_by:
                result = find_note_by_criteria(notes, search_by, value)
                if result:
                    for note in result:
                        print(f"{note.surname} {note.name}, телефон: {note.phone_number}, дата народження: {note.birth_date[0]}/{note.birth_date[1]}/{note.birth_date[2]}")
                else:
                    print("Записів з таким критерієм не знайдено.")
        elif choice == '6':
            filename = input("Введіть ім'я файлу: ")
            save_notes_to_file(notes, filename)
        elif choice == '7':
            filename = input("Введіть ім'я файлу: ")
            notes = load_notes_from_file(filename)
        elif choice == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")