import odoorpc 
odoo = odoorpc.ODOO('localhost', port=8069)
if odoo:
    print(f"Available databases: {odoo.db.list()}")
else:
    print("Failed to connect to the Odoo server.")
try:
    odoo.login('my_database2', 'admin', 'admin')
    print("Login successful.")
except Exception as e:
    print(f"Login failed: {e}")
print("crud opearation by odoorpc")
input_opearation=input("Enter (c to create) or enter(s to search) or enter(u to ubdate) or enter (d to delete): ").lower().strip().lower()
while input_opearation != 'c' and input_opearation != 's' and input_opearation != 'u' and input_opearation != 'd':
    input_opearation=input("Error input......try again...... enter (c to create) or enter(s to search) or enter(u to ubdate) or enter (d to delete): ").lower().strip().replace(" ","")
if input_opearation == 'c':
    try:
        input_title = input("Enter the title (Mr) or (Mrs): ").strip().replace(" ","").lower()
        while input_title != "mr" and input_title != "mrs":
            input_title = input("The title must be (mr) or (mrs). Enter the title again: ").strip().replace(" ","").lower()       
        input_first_name = input("Enter the first name: ").strip().replace(" ","").lower()
        input_last_name = input("Enter the last name: ").strip().replace(" ","").lower()
        input_phone = input("Enter the phone number: ").strip().replace(" ","").lower()
        input_email = input("Enter the email: ").strip().replace(" ","").lower()
        create_new_rec = {
                'title':input_title,
                'first_name' : input_first_name,
                'last_name' : input_last_name,
                'phone' : input_phone,
                'email' : input_email
            }
        lead_rec_to_create = odoo.env['event.organizer'].create(create_new_rec)
        print(f"New record created.")
    except Exception as e:
            print(f"Failed to create record: {e}.")
if input_opearation == 's':
    serach_by_name = input("Enter the first name to search: ").strip().replace(" ","").lower()
    rec_to_search = odoo.env['event.organizer'].search([('first_name', '=', serach_by_name)])
    if rec_to_search:
        print(f"Records found: {rec_to_search}")
        lead_rec_to_search = odoo.env['event.organizer'].browse(rec_to_search)
        print(f"First name: {lead_rec_to_search.title}: {lead_rec_to_search.first_name}")
        print( f"Last name: {lead_rec_to_search.last_name}")
        print( F"Phone: {lead_rec_to_search.phone}")
        print(f"Email: {lead_rec_to_search.email}")      
    else:
        print("No records found.")
if input_opearation == 'u':
 try:
    input_first_name=input("Enter the first name of the record you want to update: ").strip().replace(" ","").lower()
    rec_to_ubdate = odoo.env['event.organizer'].search([('first_name', '=', input_first_name)])
    if rec_to_ubdate:
        print(f"Records found: {rec_to_ubdate}")
        ubdate_first_name = input("Enter the new first name: ").strip().replace(" ","").lower()
        ubdate_last_name = input("Enter the new last name: ").strip().replace(" ","").lower()
        ubdate_phone = input("Enter the new phone number: ").strip().replace(" ","").lower()
        ubdate_email = input("Enter the new email: ").strip().replace(" ","").lower()
        lead_rec_to_ubdate = odoo.env['event.organizer'].browse(rec_to_ubdate)
        lead_rec_to_ubdate.first_name = ubdate_first_name
        lead_rec_to_ubdate.last_name = ubdate_last_name
        lead_rec_to_ubdate.phone = ubdate_phone
        lead_rec_to_ubdate.email = ubdate_email
        print("Records updated.")
    else:
        print("record not found.")
 except Exception as e:
     print(f"Record not updated{e}")
if input_opearation == 'd':
    rec_name=input("Enter the first name of the record you want to delete: ").strip().replace(" ","").lower()
    rec_to_delete = odoo.env['event.organizer'].search([('first_name', '=', rec_name)])
    if rec_to_delete:
        print(f"Records found: {rec_to_delete}")
        lead_rec_to_delete = odoo.env['event.organizer'].browse(rec_to_delete)
        lead_rec_to_delete.unlink()
        print("Records deleted.")
    else:
        print("No records found.")
