// Copyright (c) 2024, BHW and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},
    show_the_summary(frm){
        frm.get_field('summary').$wrapper.html('<h1>Hello</h1>')
    }
});
