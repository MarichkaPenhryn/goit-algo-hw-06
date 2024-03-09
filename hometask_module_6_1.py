from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.phones_str = set()

    def add_phone(self, phone: str):
        if phone.isdigit() and len(phone) == 10:
            if phone not in self.phones_str:
                self.phones.append(Phone(phone))
                self.phones_str.add(phone)  # Добавляем номер в множество
            else:
                raise ValueError('Phone is already exist')
        else:
            raise ValueError('Phone number must be 10 digits and contain only digits')

    def edit_phone(self, num_ex: str, num_new: str):
        num_ex = str(num_ex)  # Преобразуем к строке, чтобы избежать проблем
        num_new = str(num_new)
        if num_ex in self.phones_str:
            self.phones_str.remove(num_ex)
            self.phones_str.add(num_new)
            for i, phone in enumerate(self.phones):
                if phone.value == num_ex:
                    self.phones[i] = Phone(num_new)
                    return
        else:
            raise ValueError('Number does not exist')

    def remove_phone(self, phone: str):
        phone = str(phone)
        if phone in self.phones_str:
            self.phones_str.remove(phone)
            for i, phone_obj in enumerate(self.phones):
                if phone_obj.value == phone:
                    del self.phones[i]
                    return
        else:
            raise ValueError('Number does not exist')

    def find_phone(self, phone: str):
        phone = str(phone)
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        try:
            return self.data[name]
        except KeyError:
            raise ValueError(f'There is no {name} in AddressBook')

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f'There is no {name} in AddressBook')


#використання
#book = AddressBook()
#john_record = Record("John")
#john_record.add_phone("1234567890")
#john_record.add_phone("5555550555")
#john_record.add_phone("5555550555")

#book.add_record(john_record)

#jane_record = Record("Jane")
#jane_record.add_phone("9876543210")
#book.add_record(jane_record)

#
#try:
#    john = book.find("John")
#    john.edit_phone("1234567890", "1112223333")
#    for name, record in book.data.items():
#        print(name, record)
#    john.remove_phone("1112223333")
#    for name, record in book.data.items():
#        print(name, record)

#    found_phone = john.find_phone("5555550555")
#    if found_phone:
#        print(f"{john.name}: {found_phone}")
#    else:
#        print("Phone not found.")
#except ValueError as e:
#    print(e)
