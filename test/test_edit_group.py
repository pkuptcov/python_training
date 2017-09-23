# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit(Group(name="11111111", header="11111111", footer="11111111"))