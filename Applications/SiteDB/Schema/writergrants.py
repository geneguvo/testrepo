user = "cms_sitedb_writer"
print user

import cx_Oracle
cx_Oracle.threaded=True
con = cx_Oracle.connect("cms_sitedb/drill0rd34th@cms_sitedb")
cur = con.cursor()
cur.execute("select table_name from user_tables")
tables = cur.fetchall()
print tables
cur.execute("select sequence_name from user_sequences")
sequences = cur.fetchall()
print sequences

for t in tables:
  cur.execute("Grant select,update,insert,delete on %s to %s" % (t[0], user))

for s in sequences:
  cur.execute("Grant alter, select on %s to %s" % (s[0], user))

con.commit()
con.close()

con = cx_Oracle.connect("cms_sitedb_writer/l0rd0nlykn0w5@cms_sitedb")
cur = con.cursor()

for t in tables:
  cur.execute("Create synonym %s for CMS_SITEDB.%s" % (t[0], t[0]))

for s in sequences:
  cur.execute("Create synonym %s for CMS_SITEDB.%s" % (s[0], s[0]))

con.commit()
con.close()