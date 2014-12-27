# iawayback

## About
Iawayback is a simple, minimal Python wrapper around Internet Archive's Wayback Machine APIs, which are described here:

<http://archive.org/help/wayback_api.php>

For now the functionality is limited to a check if a user-specified URL is available in Internet Archive's Wayback Machine. The CLI tool returns comma-delimited output with info on the availability of a URL in Wayback. the following items are returned (if available):

* The source URL (as specified by the user).
* A True/ False flag that indicates whether the URL is available in Wayback.
* The URL of the *most recent* snapshot in Wayback.
* The status of the snapshot (what does this mean, exactly?)
* Snapshot timestamp

## Command line use

### Usage

    usage: iawayback.py <url>

### Positional arguments

`url` : input url

## Example 1

    iawayback.py www.projectmoonbase.com

Which gives the following output:

    www.projectmoonbase.com,True,http://web.archive.org/web/20141116085509/http://www.projectmoonbase.com/,200,20141116085509

## Example 2

    iawayback.py http://www.bitsgalore.org/2014/11/13/Demise-Of-Dutch-Blogosphere/

This results in:

    http://www.bitsgalore.org/2014/11/13/Demise-Of-Dutch-Blogosphere/,False,,,

In the second example, the page was not found in Wayback, so the last 3 output items are empty.

## Warning

This code has had *very* limited testing, and doesn't have any error trapping whatsoever. I mainly wrote this to get more familiar with the Internet Archive's Wayback API. Use at your own risk!
 
