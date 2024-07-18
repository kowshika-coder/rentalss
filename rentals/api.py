import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
    return '😳'


def throw_emoji(self,method):
    frappe.throw('emojiiii Hehehe')


def send_emoji_mail():
    print('Wednesday.............................')
    return 
# api secret: d2d3f9ac56a3460
#api key: e247596d31cc984

def get_query_condition(user):
    return "name = 2"


#To set background job
#frappe.enqueue('rentals.api.send_emoji_mail')
#op : Job('icabs::5d62d4e6-0906-45a1-ad8b-190093cab4df', enqueued_at=datetime.datetime(2024, 7, 17, 7, 40, 2, 108331))