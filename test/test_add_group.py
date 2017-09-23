# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="123123123", header="123123123123", footer="123123123123"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))