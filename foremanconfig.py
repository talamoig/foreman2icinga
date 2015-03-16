# URL of your foreman server
baseurl="https://foreman-server"

# auth is the base64-encoded version of the string username:password
# you can generate it from command-line with
# echo 'username:password' | base64

auth="c2Rmc2RmOjM0NTNsNGtmbXNkCg"

# The host inclusion/exclusion works like this:
# if the host matches ANY of the hostinclude regular expression is included
# only if is not included in ANY of the hostexclude expression
#
# in a host name matches any of these regular-expression is excluded
hostexclude=['host-to-exclude','exlude-this.*']

#
hostinclude=['.*']
