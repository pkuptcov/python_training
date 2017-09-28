# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", company="", title="", address="",
                            home="", mobile="", work="", fax="", email="", email_2="", email_3="", homepage="", byear="", ayear="",
                            address_2="", phone_2="", notes=""))
    app.contact.delete()