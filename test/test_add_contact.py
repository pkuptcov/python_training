# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address="address",
                            home="home", mobile="mobile", work="work", fax="fax", email="email", email_2="email2", email_3="email3", homepage="google.com", byear="1999", ayear="2000",
                            address_2="dostoevskiy prospekt", phone_2="Home", notes="Notes"))
    app.session.logout()