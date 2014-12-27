# Simple, minimal Python wrapper around Internet Archive's Wayback Machine APIs:
#
# http://archive.org/help/wayback_api.php
#
# Check if user-specified URL was archived in Internet Archive's Wayback Machine.
# CLI tool returns comma-delimited output with info on availability in Wayback
# Archived URL (if available) is given for most recent snapshot only!
#
# Author: Johan van der Knijff
#

import sys
import urllib2
import json

def checkURL(url):

    # API url (see: http://archive.org/help/wayback_api.php)
    urlAPI="http://archive.org/wayback/available?url="

    # URL we want to search for
    urlSearch = url

    req = urllib2.Request(urlAPI + urlSearch)
    response = urllib2.urlopen(req)
    the_page = response.read()

    # Decode json object
    data = json.loads(the_page)
    snapshots = data['archived_snapshots']
    if len(snapshots) == 0:
        # No snapshots available, so not available in Wayback
        available = False
        urlWayback = ""
        status = ""
        timestamp = ""

    else:
        # Snapshot(s) available
        # For now API only returns 1 snaphot, which is the most recent one.
        # May change in future API versions.
        closest = snapshots['closest']
        available = closest['available']
        urlWayback = closest['url']
        status = closest['status']
        timestamp = closest['timestamp']
    
    return(available, urlWayback, status, timestamp)

def main():
    
    if len(sys.argv) == 1:
        sys.stderr.write("USAGE: iawayback.py <url> \n")
        sys.exit()

    url = sys.argv[1]

    available, urlWayback, status, timestamp = checkURL(url)
    stringOut = url + "," + str(available) + "," + urlWayback + "," + status + "," + timestamp
    sys.stdout.write(stringOut + "\n")

main()

