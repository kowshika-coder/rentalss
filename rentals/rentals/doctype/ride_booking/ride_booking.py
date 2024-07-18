# Copyright (c) 2024, BHW and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			self.rate=frappe.db.get_single_value('Rentals Settings','standard_rate')
		total_distance=0
		for i in self.ride_items:
			total_distance+= i.distance
		self.total_amount= total_distance * self.rate
	pass
