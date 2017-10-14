from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None,
                       fax=None, email=None, email_2=None, email_3=None, homepage=None, byear=None, ayear=None, address_2=None, phone_2=None, notes=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int (self.id)
        else:
            return maxsize