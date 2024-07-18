# Copyright (c) 2024, BHW and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns= [{
		"fieldname":'make',
		'label':'Make',
		'fieldtype':'Data'
	},
	{
		"fieldname":"total_revenue",
		'label':'Total Revenue',
		'fieldtype':'Currency',
		'options':'AED'

	}]
	data=frappe.get_all("Ride Booking",
				fields=["sum(total_amount) AS total_revenue","vehicle.make"],
				filters={"docstatus":1},
				group_by="make")
	chart={
		'data':{
			'labels':[i.make for i in data],
			'datasets':[{'values':[i.total_revenue for i in data]}]

		},
		'type':'pie',
	}
	return columns, data,"Here is the report",chart