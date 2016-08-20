html_template = b"""
<!DOCTYPE html>
<html>
<title>Prashant Tiwari</title>
<body>
Work in progress.
<span id="cdSiteSeal1"><script type="text/javascript" src="//tracedseals.starfieldtech.com/siteseal/get?scriptId=cdSiteSeal1&amp;cdSealType=Seal1&amp;sealId=55e4ye7y7mb7334fdd8c49376b30e1eayhy7mb7355e4ye729c2d1bbfca23d3ba"></script></span>
</body>
</html>


"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [html_template]
