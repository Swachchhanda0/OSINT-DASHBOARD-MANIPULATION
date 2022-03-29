# test_sfp_email.py
import pytest
import unittest

from modules.sfp_email import sfp_email
from sflib import SpiderFoot
from osint import SpiderFootEvent, SpiderFootTarget


@pytest.mark.usefixtures
class TestModuleEmail(unittest.TestCase):
    """
    Test modules.sfp_email
    """

    def test_opts(self):
        module = sfp_email()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        """
        Test setup(self, sfc, userOpts=dict())
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_email()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_email()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_email()
        self.assertIsInstance(module.producedEvents(), list)

    def test_handleEvent(self):
        """
        Test handleEvent(self, event)
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_email()
        module.setup(sf, dict())

        target_value = 'example target value'
        target_type = 'IP_ADDRESS'
        target = SpiderFootTarget(target_value, target_type)
        module.setTarget(target)

        event_type = 'ROOT'
        event_data = 'example data'
        event_module = ''
        source_event = ''
        evt = SpiderFootEvent(event_type, event_data, event_module, source_event)

        result = module.handleEvent(evt)

        self.assertIsNone(result)