# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()