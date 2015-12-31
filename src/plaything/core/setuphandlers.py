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
    # discussion settings
    NAMESPACE = 'plone.app.discussion.interfaces.IDiscussionSettings'
    discussion_settings = [
        {"name":"anonymous_email_enabled", "value":True},
        {"name":"anonymous_comments", "value":True},
        {"name":"captcha", "value":"norobots"},
        {"name":"globally_enabled", "value":True},
        {"name":"moderation_enabled", "value":True},
        {"name":"text_transform", "value":"text/x-web-intelligent"},
    ]
    for setting in discussion_settings:
        api.portal.set_registry_record(
          '%s.%s' % (NAMESPACE, setting['name']),
                     setting['value'])
    # set posts as the "default layout for the site"
    # portal = api.portal.get()
    # portal.setLayout("posts")
    # branding customizations
    logo = """filenameb64:cGxheXRoaW5nbG9nby5wbmc=;datab64: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"""
    api.portal.set_registry_record('plone.site_logo', str(logo))
    api.portal.set_registry_record('plone.site_title', u"PlayThing Site")
    api.portal.set_registry_record(
                              'plone.toolbar_logo', 
                              u"/++resource++plaything.core/playthinglogo.svg"
                              )

    
def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('playthingcore_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
