import frappe

def execute():
    vehicles=frappe.db.get_all('Vehicle',pluck="name")
    print(f'v {vehicles}')
    for i in vehicles:
        vehicle=frappe.get_doc("Vehicle",i)
        print(vehicle,'yuio')
        vehicle.set_title()
        vehicle.save()
    
    frappe.db.commit()