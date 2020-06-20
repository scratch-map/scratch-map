class Countries:
    country_list = []

    def add_country(self, country_name):
        self.country_list.append(country_name)

    def remove_country(self, country_name):
        self.country_list.remove(country_name)
