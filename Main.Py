import webbrowser as web

url = "https://www.picknpull.com/check-inventory/vehicle-search?make=90&model=1244&distance=25&zip=94707&year="
chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

web.register("Chrome",None, web.BackgroundBrowser(chromePath))
web.get("Chrome").open_new_tab(url)