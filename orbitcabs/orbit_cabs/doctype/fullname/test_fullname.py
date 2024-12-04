# Copyright (c) 2024, Mr.Rohan and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestFullName(UnitTestCase):
	"""
	Unit tests for FullName.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestFullName(IntegrationTestCase):
	"""
	Integration tests for FullName.
	Use this class for testing interactions between multiple components.
	"""

	pass
