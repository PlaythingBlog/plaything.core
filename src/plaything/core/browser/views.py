# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView

import datetime

class PostsList(BrowserView):
    """ A list of posts that we call bob
    """
    
    def posts(self):
        # eyes @@
        results = []
        portal_catalog = api.portal.get_tool('portal_catalog')
        # brains @@
        brains = portal_catalog(
            portal_type=[
                'Event','News Item','Link','Image','File'
                ],
                review_state='published',
                sort_on='effective',
                sort_order='descending',
                )
        return [
                  {"id":brain.id,
                    "type":brain.portal_type,
                    "title":brain.Title,
                    "description":brain.Description,
                    } 
                          for brain in brains
                  
                  ]
        
    def __call__(self):
        """ we will return the posts here """
        return self.posts()
        
        
class frontpageView(BrowserView):
    """The view of the conference frontpage
    """

    def posts(self):
        """Get the posts"""
        results = []
        catalog = api.portal.get_tool('portal_catalog')
        today = datetime.date.today()
        brains = catalog(
            portal_type=['Event','News Item','Link','Image','File'],
            review_state='published',
            sort_on='effective',
            sort_order='descending',
        )
        return brains