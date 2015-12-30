# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'plaything.core:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if context.readDataFile('playthingcore_default.txt') is None:
        return
    # set routes in the portal registry
    NAMESPACE = 'collective.routes.controlpanel.IRoutesSettings'
    api.portal.set_registry_record('%s.routes' % NAMESPACE,
                                   set(['Tagged', 'Blog Posts']))
    # disable folderish tabs
    api.portal.set_registry_record('plone.nonfolderish_tabs', False)

    # set posts as the "default view"
    portal = api.portal.get()
    portal.setDefaultPage("posts")


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('playthingcore_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
