import dataclasses
from pathlib import Path
from typing import Optional

import scrapy


@dataclasses.dataclass(frozen=True)
class Vacancy:
    url: str
    title: str
    location: str
    description: str
    salary_min: Optional[str] = None
    salary_max: Optional[str] = None


class VacancySpider(scrapy.Spider):
    name = "vacancy"

    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response):
        cards = response.css("h2 a")
        for card in cards:
            job_link = card.attrib["href"]
            yield response.follow(job_link, callback=self.parse_vacancy)

    def parse_vacancy(self, response):
        url = response.url
        title = response.css("h1::text").get()
        location = extract_location(response)
        description = response.css("#job-description").xpath("normalize-space()").get()
        salary = extract_salary(response)

        vacancy_data = {
            "url": url,
            "title": title,
            "location": location,
            "salary_min": salary["min"],
            "salary_max": salary["max"],
            "description": description,
        }

        print(vacancy_data)


def extract_location(response):
    for par in response.css("p"):
        try:
            if par.css("span").attrib["title"] == "Адреса роботи":
                location = par.xpath("normalize-space()").get().split(".")[0]
                return location
        except:
            pass
    return None


def extract_salary(response):
    salary = {"min": None, "max": None}
    for par in response.css("p"):
        try:
            if par.css("span").attrib["title"] == "Зарплата":
                salary_info = par.xpath("normalize-space()").get().split(".")[0]
                salary_value = (
                    salary_info.split("грн")[0].replace("\u202f", "_").split("\u2009")
                )
                salary["min"] = f"{int(salary_value[0])} грн"
                salary["max"] = f"{int(salary_value[2])} грн"

        except:
            pass
    if salary["max"] is None and salary["min"]:
        salary["max"] = salary["min"]
    return salary
