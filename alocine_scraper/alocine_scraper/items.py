# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FilmItem(scrapy.Item):
    # Définition des champs pour l'élément AlloCiné
    title = scrapy.Field()
    original_title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    description = scrapy.Field()
    actors = scrapy.Field()
    director = scrapy.Field()