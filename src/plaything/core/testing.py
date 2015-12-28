# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plaything.core


class PlaythingCoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plaything.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plaything.core:default')


PLAYTHING_CORE_FIXTURE = PlaythingCoreLayer()


PLAYTHING_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLAYTHING_CORE_FIXTURE,),
    name='PlaythingCoreLayer:IntegrationTesting'
)


PLAYTHING_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLAYTHING_CORE_FIXTURE,),
    name='PlaythingCoreLayer:FunctionalTesting'
)


PLAYTHING_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLAYTHING_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlaythingCoreLayer:AcceptanceTesting'
)
