# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="1", middlename="2", lastname="3", nickname="4", company="5", title="6", address="7",
                            home="8", mobile="9", work="10", fax="11", email="12", email_2="13", email_3="14", homepage="15", byear="16", ayear="17",
                            address_2="18", phone_2="19", notes="20"))