def write_report(users,books):
    with open("report.txt", 'w') as txt_file:
                txt_file.write("Library Management System Report\n\n")
                txt_file.write("User Information:\n")
                for user in users:
                    txt_file.write(f"\nUser ID: {user['user_id']}\n")
                    txt_file.write(f"Name: {user['name']}\n")
                    txt_file.write(f"Borrowed Books:\n")
                    for book in user['books']:
                        txt_file.write(f"  - Book ID: {book['id']}\n")
                        txt_file.write(f"    Book Name: {book['name']}\n")
                        txt_file.write(f"    Borrowed Date: {book['borrowed']}\n")
                    txt_file.write("-" * 30 + "\n")

                txt_file.write("\nBook Information:\n")
                for book in books:
                    txt_file.write(f"\nBook ID: {book['id']}\n")
                    txt_file.write(f"Book Name: {book['name']}\n")
                    txt_file.write(f"Quantity Available: {book['quantity']}\n")
                    txt_file.write("-" * 30 + "\n")

                print("\nReport.txt generated successfully.")