# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plaything.core.testing import PLAYTHING_CORE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plaything.core is properly installed."""

    layer = PLAYTHING_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plaything.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plaything.core'))

    def test_browserlayer(self):
        """Test that IPlaythingCoreLayer is registered."""
        from plaything.core.interfaces import (
            IPlaythingCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlaythingCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLAYTHING_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plaything.core'])

    def test_product_uninstalled(self):
        """Test if plaything.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plaything.core'))

    def test_browserlayer_removed(self):
        """Test that IPlaythingCoreLayer is removed."""
        from plaything.core.interfaces import IPlaythingCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlaythingCoreLayer, utils.registered_layers())
