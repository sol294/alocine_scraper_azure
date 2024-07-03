import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from alocine_scraper.items import FilmItem
from alocine_scraper.utils import connect_to_postgres, close_connection
import psycopg2

class AllocineSpiderSpider(CrawlSpider):
    name = "allocine_spider"
    allowed_domains = ["allocine.fr"]
    start_urls = [f"https://www.allocine.fr/film/meilleurs/?page={n}" for n in range(1, 10)]

    rules = [
        Rule(LinkExtractor(restrict_xpaths="//h2/a"), callback='parse_item', follow=False),
    ]

    def parse_item(self, response):
        item = FilmItem()

        item['title'] = response.xpath('//div[@class="titlebar-title titlebar-title-xl"]/text()').get()
        item['original_title'] = response.xpath('//div[@class="meta-body-item"]/span[@class="dark-grey"]/text()').get()
        item['score'] = response.xpath('//span[@class="stareval-note"]/text()').get()
        item['genre'] = response.xpath('//span[@class="spacer"][2]/following-sibling::*/text()').getall()
        item['year'] = response.xpath('//span[contains(text(),"Année de production")]/following-sibling::span/text()').get()
        item['duration'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/text()').getall()
        item['description'] = response.xpath('//p[@class="bo-p"]/text()').get()
        item['actors'] = response.xpath('//span[contains(text(),"Avec")]/following-sibling::span/text()').getall()
        item['director'] = response.xpath('//span[contains(text(),"Par")]/following-sibling::span/text()').getall()

        # Nettoyer les champs dans le spider
        item = self.clean_item(item)

    ###Fonctionne
    #     # Connexion à PostgreSQL et insertion des données
    #     conn = connect_to_postgres()
    #     if conn:
    #         try:
    #             cursor = conn.cursor()

    #             # Exemple d'insertion dans une table films
    #             insert_query = "INSERT INTO films (title, original_title, score, genre, year, duration, description, actors, director) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #             film_data = (
    #                 item['title'], item['original_title'], item['score'], item['genre'],
    #                 item['year'], item['duration'], item['description'], item['actors'], item['director']
    #             )
    #             cursor.execute(insert_query, film_data)
    #             conn.commit()

    #         except psycopg2.Error as e:
    #             print("Erreur lors de l'insertion dans PostgreSQL:", e)

    #         finally:
    #             close_connection(conn)

    #     yield item

    # def clean_item(self, item):
    #     item['genre'] = ', '.join([g.strip() for g in item['genre'] if g.strip() != '|'])

    #     item['duration'] = ' '.join([d.strip() for d in item['duration']]).replace('\n', '').replace('\r', '').strip()
        
    #     item['description'] = item['description'].strip().replace('\n', ' ')

    #     item['actors'] = ', '.join([actor.strip() for actor in item['actors']])
    #     item['director'] = ', '.join([director.strip() for director in item['director']])
        
    #     return item
    ##fin
        print(f"Scraped item: {item}") 
        yield item

    def clean_item(self, item):
        item['genre'] = ', '.join([g.strip() for g in item['genre'] if g.strip() != '|'])
        item['duration'] = ' '.join([d.strip() for d in item['duration']]).replace('\n', '').replace('\r', '').strip()
        item['description'] = item['description'].strip().replace('\n', ' ')
        item['actors'] = ', '.join([actor.strip() for actor in item['actors']])
        item['director'] = ', '.join([director.strip() for director in item['director']])
        return item