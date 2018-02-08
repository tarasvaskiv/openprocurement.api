# -*- coding: utf-8 -*-
import unittest
from schematics.exceptions import ValidationError
from openprocurement.api.models import Location


class TestLocation(unittest.TestCase):

    location_test_data = [
        {
            'location': {'latitude': -90.43, 'longitude': 147.028153299393},
            'result': {'latitude': [
                u'Invalid value. Latitude must be between -90 and 90 degree.']}
        },
        {
            'location': {'latitude': 90.43, 'longitude': -100.43},
            'result': {'latitude': [
                u'Invalid value. Latitude must be between -90 and 90 degree.']}
        },
        {
            'location': {'latitude': "90.43", 'longitude': "100.43"},
            'result': {'latitude': [
                u'Invalid value. Latitude must be between -90 and 90 degree.']}
        },
        {
            'location': {'latitude': "-90.43", 'longitude': "-100.43"},
            'result': {'latitude': [
                u'Invalid value. Latitude must be between -90 and 90 degree.']}
        },
        {
            'location': {'latitude': "sixty", 'longitude': 100.0001},
            'result': {'latitude': [
                u"Invalid value. Required latitude format 12.0123456789"]}
        },
        {
            'location': {'latitude': "50'43'", 'longitude': -0.00001},
            'result': {'latitude': [
                u"Invalid value. Required latitude format 12.0123456789"]}
        },
        {
            'location': {'latitude': 90.00, 'longitude': -180.43},
            'result': {'longitude': [
                u"Invalid value. Longitude must be between -180 and 180 degree."]}
        },
        {
            'location': {'latitude': 90, 'longitude': 180.0000001},
            'result': {'longitude': [
                u"Invalid value. Longitude must be between -180 and 180 degree."]}
        },
        {
            'location': {'latitude': "89.00001", 'longitude': "180.000001"},
            'result': {'longitude': [
                u"Invalid value. Longitude must be between -180 and 180 degree."]}
        },
        {
            'location': {'latitude': "-87.01", 'longitude': "-180.01010101"},
            'result': {'longitude': [
                u"Invalid value. Longitude must be between -180 and 180 degree."]}
        },
        {
            'location': {'latitude': "60", 'longitude': "10.10.10"},
            'result': {'longitude': [
                u"Invalid value. Required longitude format 12.0123456789"]}
        },
        {
            'location': {'latitude': "47.028153299393", 'longitude': "0\"10'"},
            'result': {'longitude': [
                u"Invalid value. Required longitude format 12.0123456789"]}
        },
        {
            'location': {
                'latitude': 90.028153299393,
                'longitude': 180.028153299393
            },
            'result': {
                'latitude': [
                    u'Invalid value. Latitude must be between -90 and 90 degree.'],
                'longitude': [
                    u"Invalid value. Longitude must be between -180 and 180 degree."]
            }
        },
        {
            'location': {
                'latitude': "90.028153299393",
                'longitude': "180.028153299393"
            },
            'result': {
                'latitude': [
                    u'Invalid value. Latitude must be between -90 and 90 degree.'],
                'longitude': [
                    u"Invalid value. Longitude must be between -180 and 180 degree."]
            }
        },
        {
            'location': {
                'latitude': "90.02815.3299393",
                'longitude': "180.028.153299393"
            },
            'result': {
                'latitude': [
                    u"Invalid value. Required latitude format 12.0123456789"],
                'longitude': [
                    u"Invalid value. Required longitude format 12.0123456789"]
            }
        },
    ]

    def test_validate_location(self):
        for test_case in self.location_test_data:
            with self.assertRaises(ValidationError) as e:
                location = Location(test_case['location'])
                location.validate()
            self.assertEqual(e.exception.message, test_case['result'])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLocation))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
