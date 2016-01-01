from os import getenv
import transaction
SITE = getenv("SITE_ID")
HOST='*.herokuapp.com'
print "-----> Plone site %s exists" % SITE
print "-----> Setting virtualhost settings"
app.virtual_hosting.set_map('%s/%s' % (HOST,SITE))
transaction.commit()
