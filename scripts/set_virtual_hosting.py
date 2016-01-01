from os import getenv
import transaction
SITE = getenv("SITE_ID")
SITE_NAME = getenv("SITE_NAME")
HOST='%s.herokuapp.com' % SITENAME
print "-----> Plone site %s exists" % SITE
print "-----> Setting virtualhost settings"
app.virtual_hosting.set_map('%s/%s' % (HOST,SITE))
app.virtual_hosting.set_map(HOST + "/VirtualHostBase/https/%s/%s" % (HOST,SITE))
transaction.commit()
