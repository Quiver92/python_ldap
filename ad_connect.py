import ldap


connect = ldap.initialize('ldap://10.0.0.240')
connect.protocol_version = 3
connect.set_option(ldap.OPT_REFERRALS, 0)
connect.simple_bind_s('user@domain.local', 'pass')


result = connect.search_s('dc=domain,dc=local',
                          ldap.SCOPE_SUBTREE,
                          'userPrincipalName=user@domain.local',
                          ['memberOf'])
print(result)
