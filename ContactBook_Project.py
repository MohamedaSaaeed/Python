while True:
    from datetime import date
    filename = str("contactbook_" + str((date.today()).strftime("%d-%m-%Y")) + ".csv")
    #take input from user upon his need
    q = input('Create(c) Delete (d) Update(u) Quit(q)')
    if q == 'c':
        #take inputs to create contact
        with open(filename, 'a') as f:
            name = (input('Name:'))
            phone = (input('Phone:'))
            email = (input('Email:'))
            address = (input('Address:'))
            insertion_Date = (date.today()).strftime("%d/%m/%Y")
            f.writelines((name, ',', phone, ',', email, ',', address, ',', insertion_Date, '\n'))
    elif q == 'd':
        #take contact input to delete the record
        delete_contact = input("Delete:")
        with open(filename, 'r') as f:
            file = f.readlines()
        with open(filename, "w") as f:
            for line in file:
                if not line.strip("\n").startswith(delete_contact):
                    f.write(line)
    elif q == 'u':
        #take the new input to replace the old one
        old_contact = input('Enter the old (Name,Phone,Email,Address) you want to change:')
        new_contact = input('Enter the new (Name,Phone,Email,Address):')
        with open(filename, 'r') as f:
            newline = []
            file = f.readlines()
            for word in file:
                newline.append(word.replace(old_contact, new_contact))
        with open(filename, "w") as f:
            for line in newline:
                f.writelines(line)
    #exit the loop
    else:
        break