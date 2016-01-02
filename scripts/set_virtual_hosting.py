from os import getenv
import transaction
SITE = getenv("SITE_ID")
SITE_NAME = getenv("SITE_NAME")
HOST='%s.herokuapp.com' % SITE_NAME
print "-----> Plone site %s exists" % SITE
print "-----> Setting virtualhost settings"
vhosts = ['%s/%s' % (HOST,SITE), HOST + "/VirtualHostBase/https/%s/%s" % (HOST,SITE)]
rules = "\n".join(vhosts)
app.virtual_hosting.set_map(rules)
transaction.commit()
