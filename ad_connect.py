import ldap


connect = ldap.initialize('ldap://10.0.0.240')
connect.protocol_version = 3
connect.set_option(ldap.OPT_REFERRALS, 0)
connect.simple_bind_s('w.lytovka@koksztys.local', 'Tazafe54')


result = connect.search_s('dc=koksztys,dc=local',
                          ldap.SCOPE_SUBTREE,
                          'userPrincipalName=w.lytovka@koksztys.local',
                          ['memberOf'])
print(result)
