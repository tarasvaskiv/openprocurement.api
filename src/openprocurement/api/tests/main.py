# -*- coding: utf-8 -*-

import unittest

from openprocurement.api.tests import (
    auth, spore, migration, models, test_regexps
)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(auth.suite())
    suite.addTest(spore.suite())
    suite.addTest(migration.suite())
    suite.addTest(models.suite())
    suite.addTest(test_regexps.suite())
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
