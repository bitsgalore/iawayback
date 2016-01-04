#!/usr/bin/env python
"""Simple, minimal Python wrapper around Internet Archive's
Wayback Machine APIs:

    http://archive.org/help/wayback_api.php

Check if user-specified URL was archived in Internet Archive's
Wayback Machine. CLI tool returns comma-delimited output with info on
availability in Wayback Archived URL (if available) is given for most
recent snapshot only!

Usage: ia wayback [--help] <url>

Options:
  -h, --help                Show this help message and exit.
"""
import sys
import urllib2
import json

from docopt import docopt


__title__ = 'ia_plugin'
__version__ = '0.0.1'
__url__ = 'https://github.com/jjjake/iawayback'
__author__ = 'Johan van der Knijff'
__all__ = ['ia_wayback']


def checkURL(url):

    # API url (see: http://archive.org/help/wayback_api.php)
    urlAPI="https://archive.org/wayback/available?url="

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

def main(argv=None, session=None):
    # Support for calling script directly, rather than through 'ia'.
    if argv is None:
        argv = ['wayback'] + sys.argv[1:]

    # Parse args.
    args = docopt(__doc__, argv=argv)

    available, urlWayback, status, timestamp = checkURL(args['<url>'])
    print(','.join([args['<url>'], str(available), urlWayback, status, timestamp]))

if __name__ == '__main__':
    main()
