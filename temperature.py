import requests
from selectorlib import Extractor
class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    """

    # Headers may be needed in order to scrape data from a webpage
    h = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'
    # initialize a temperature object

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    #     Add the country and city to build the url
    def build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    # Scrape the value and return a temperature
    def scrape(self):
        url = self.build_url()
        r = requests.get(url, headers=self.h)
        content = r.text
        extractor = Extractor.from_yaml_file("temperature.yaml")
        raw_result = extractor.extract(content)
        return raw_result

    #     Return the temperature as a float with extra spaces removed
    def get(self):
        raw_result = self.scrape()
        result = float(raw_result["temp"].replace('°F', "").strip())
        return result


if __name__ == "__main__":
    sacramento_temp = Temperature(country='USA', city="Sacramento")
    sac_result = sacramento_temp.get()
    print(sac_result)












