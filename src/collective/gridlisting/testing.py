# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.gridlisting


class CollectiveFolderlistingLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.gridlisting)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.gridlisting:default")


COLLECTIVE_FOLDERLISTING_FIXTURE = CollectiveFolderlistingLayer()


COLLECTIVE_FOLDERLISTING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FOLDERLISTING_FIXTURE,),
    name="CollectiveFolderlistingLayer:IntegrationTesting",
)


COLLECTIVE_FOLDERLISTING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FOLDERLISTING_FIXTURE,),
    name="CollectiveFolderlistingLayer:FunctionalTesting",
)


COLLECTIVE_FOLDERLISTING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_FOLDERLISTING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveFolderlistingLayer:AcceptanceTesting",
)
