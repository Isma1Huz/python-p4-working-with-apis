import requests
import json

class GetPrograms:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

if __name__ == "__main__":
    # Specify the URL for the NYC Open Data API
    nyc_api_url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    # Create an instance of GetPrograms with the API URL
    programs = GetPrograms(nyc_api_url)

    # Get and print the list of program schools
    programs_schools = programs.program_school()
    for school in set(programs_schools):
        print(school)
