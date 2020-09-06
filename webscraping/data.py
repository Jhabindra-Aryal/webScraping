from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://covid19.mohp.gov.np/")
r.html.render()