# Create a Plone site. This is a "run" script.

from Products.CMFPlone.factory import _DEFAULT_PROFILE
from Products.CMFPlone.factory import addPloneSite
from zope.component import getMultiAdapter
from Acquisition import aq_inner
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from plone import api
from Testing.makerequest import makerequest
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy, OmnipotentUser
from travelkingstonjamaica.site.browser import utils
from zope.component.hooks import setSite


import sys
import transaction

def spoofRequest(app):
    """
    Make REQUEST variable to be available on the Zope application server.

    This allows acquisition to work properly
    """
    _policy=PermissiveSecurityPolicy()
    _oldpolicy=setSecurityPolicy(_policy)
    newSecurityManager(None, OmnipotentUser().__of__(app.acl_users))
    return makerequest(app)


def getView(context, request, name):
    # Remove the acquisition wrapper (prevent false context assumptions)
    context = aq_inner(context)
    # May raise ComponentLookUpError
    view = getMultiAdapter((context, request), name=name)
    # Add the view to the acquisition chain
    view = view.__of__(context)
    return view


# admin_username = 'admin'

site_id = sys.argv[3]
#language = "en-jm"
default_extension_profiles = (
    'plone.app.caching:default',
    'plonetheme.barceloneta:default',
    'travelkingstonjamaica.site:default',
#    '{{ addon }}',
)

if site_id in app.objectIds():
    print "A Plone site already exists"
    sys.exit(1)

site = addPloneSite(
    app, site_id,
    title='TravelKingston',
    profile_id=_DEFAULT_PROFILE,
    extension_ids=default_extension_profiles,
    setup_content=True,
#    default_language=language,
    )
    
# setup the site
app = spoofRequest(app)
site_import = utils.SetupSite(site, app)
site_import()

# Sets the current site as the active site
setSite(app[site_id])

# switch on the theme
NAMESPACE = 'plone.app.theming.interfaces.IThemeSettings'
api.portal.set_registry_record('%s.absolutePrefix' % NAMESPACE,
                               u'/++theme++travelkingstonjamaica.theme')
api.portal.set_registry_record('%s.currentTheme' % NAMESPACE,
                               u'travelkingstonjamaica.theme')
api.portal.set_registry_record('%s.doctype' % NAMESPACE, '<!doctype html>')
api.portal.set_registry_record('%s.enabled' % NAMESPACE, True)
api.portal.set_registry_record('%s.readNetwork' % NAMESPACE, True)
api.portal.set_registry_record('%s.rules' % NAMESPACE,
                             u'/++theme++travelkingstonjamaica.theme/rules.xml')



#csvimport = utils.ImportCSVContent(attractions, app)
#csvimport()

#site = app.unrestrictedTraverse("%s/attractions/tkj.import.csvcontent" % site_id)
#site.unrestrictedTraverse("attractions/tkj.import.csvcontent")

transaction.commit()
