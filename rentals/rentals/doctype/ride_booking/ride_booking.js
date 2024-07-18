// Copyright (c) 2024, BHW and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},
	update_total_amount(frm){
		let total_d=0
		for(let item of frm.doc.ride_items){
			total_d+=item.distance
			console.log({'distance':item.distance})
		}
		const amount= total_d * frm.doc.rate
		frm.set_value('total_amount',amount)
	},
	rate(frm){
		frm.trigger('update_total_amount')
	}
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},
	distance(frm,doctype,id){
		//my_child=frappe.get_doc(doctype,id)
		//To change value of current child row
		//frappe.model.set_value(doctype,id,'source','updated')
		frm.trigger('update_total_amount')
	},
	ride_items_delete(frm){
		frm.trigger('update_total_amount')
	}
})
