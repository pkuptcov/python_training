# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.contact.delete()