##Fonctionne
# from itemadapter import ItemAdapter
# from sqlalchemy.orm import sessionmaker
# from .models import Film, engine
# import re

# class AlocineScraperPipeline:
#     def process_item(self, item, spider):
#         item = self.clean_duration(item)
#         item = self.clean_actors(item)
#         item = self.clean_description(item)
#         item = self.clean_director(item)
#         item = self.clean_genre(item)
#         item = self.clean_original_title(item)
#         item = self.clean_score(item)
#         item = self.clean_title(item)
#         item = self.clean_year(item)
#         return item

#     def clean_duration(self, item):
#         adapter = ItemAdapter(item)
#         duration = adapter.get('duration')
#         if duration:
#             duration_text = ' '.join(duration).strip().replace('\n', '').replace(' ,', '').replace('  ', ' ')
#             hours_match = re.search(r'(\d+)\s*h', duration_text)
#             minutes_match = re.search(r'(\d+)\s*min', duration_text)

#             hours = int(hours_match.group(1)) if hours_match else 0
#             minutes = int(minutes_match.group(1)) if minutes_match else 0

#             total_minutes = hours * 60 + minutes
#             adapter['duration'] = total_minutes
#         return item

#     def clean_actors(self, item):
#         adapter = ItemAdapter(item)
#         actors = adapter.get('actors')
#         if actors:
#             actors_cleaned = ', '.join([actor.strip() for actor in actors])
#             adapter['actors'] = actors_cleaned
#         return item

#     def clean_description(self, item):
#         adapter = ItemAdapter(item)
#         description = adapter.get('description')
#         if description:
#             description_cleaned = description.strip().replace('\n', ' ')
#             adapter['description'] = description_cleaned
#         return item

#     def clean_director(self, item):
#         adapter = ItemAdapter(item)
#         director = adapter.get('director')
#         if director:
#             director_cleaned = ', '.join([dir.strip() for dir in director])
#             adapter['director'] = director_cleaned
#         return item

#     def clean_genre(self, item):
#         adapter = ItemAdapter(item)
#         genre = adapter.get('genre')
#         if genre:
#             genre_cleaned = ', '.join([g.strip() for g in genre if g.strip() != '|'])
#             adapter['genre'] = genre_cleaned
#         return item

#     def clean_original_title(self, item):
#         adapter = ItemAdapter(item)
#         original_title = adapter.get('original_title')
#         if original_title:
#             original_title_cleaned = original_title.strip().replace('\n', ' ')
#             adapter['original_title'] = original_title_cleaned
#         return item

#     def clean_score(self, item):
#         adapter = ItemAdapter(item)
#         score = adapter.get('score')
#         if score:
#             score_cleaned = score.strip().replace('\n', ' ')
#             adapter['score'] = score_cleaned
#         return item

#     def clean_title(self, item):
#         adapter = ItemAdapter(item)
#         title = adapter.get('title')
#         if title:
#             title_cleaned = title.strip().replace('\n', ' ')
#             adapter['title'] = title_cleaned
#         return item

#     def clean_year(self, item):
#         adapter = ItemAdapter(item)
#         year = adapter.get('year')
#         if year:
#             year_cleaned = year.strip().replace('\n', ' ')
#             adapter['year'] = year_cleaned
#         return item

# class PostgresPipeline:
#     def __init__(self):
#         self.Session = sessionmaker(bind=engine)

#     def open_spider(self, spider):
#         self.session = self.Session()

#     def close_spider(self, spider):
#         self.session.close()

#     def process_item(self, item, spider):
#         film = Film(
#             title=item['title'],
#             original_title=item['original_title'],
#             score=item['score'],
#             genre=item['genre'],
#             year=item['year'],
#             duration=item['duration'],
#             description=item['description'],
#             actors=item['actors'],
#             director=item['director']
#         )

#         self.session.add(film)
#         self.session.commit()
        
#         return item
##fin
####################################################################
####################################################################
###FONCTIONNE DBEAVER###############################################

# import psycopg2
# from alocine_scraper.utils import connect_to_postgres, close_connection
# from itemadapter import ItemAdapter
# import re
# class PostgresPipeline:
#     def open_spider(self, spider):
#         self.conn = connect_to_postgres()
#         self.cursor = self.conn.cursor()

#     def close_spider(self, spider):
#         close_connection(self.conn)

#     def process_item(self, item, spider):
#         try:
#             insert_query = """
#             INSERT INTO films (title, original_title, score, genre, year, duration, description, actors, director)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             film_data = (
#                 item['title'], item['original_title'], item['score'], item['genre'],
#                 item['year'], item['duration'], item['description'], item['actors'], item['director']
#             )
#             print(f"Inserting item: {film_data}")
#             self.cursor.execute(insert_query, film_data)
#             self.conn.commit()
#         except psycopg2.Error as e:
#             spider.logger.error(f"Erreur lors de l'insertion dans PostgreSQL: {e}")
#         return item

# class AlocineScraperPipeline:
#     def process_item(self, item, spider):
#         item = self.clean_duration(item)
#         item = self.clean_actors(item)
#         item = self.clean_description(item)
#         item = self.clean_director(item)
#         item = self.clean_genre(item)
#         item = self.clean_original_title(item)
#         item = self.clean_score(item)
#         item = self.clean_title(item)
#         item = self.clean_year(item)
#         return item

#     def clean_duration(self, item):
#         adapter = ItemAdapter(item)
#         duration = adapter.get('duration')
#         if duration:
#             duration_text = ' '.join(duration).strip().replace('\n', '').replace(' ,', '').replace('  ', ' ')
#             hours_match = re.search(r'(\d+)\s*h', duration_text)
#             minutes_match = re.search(r'(\d+)\s*min', duration_text)

#             hours = int(hours_match.group(1)) if hours_match else 0
#             minutes = int(minutes_match.group(1)) if minutes_match else 0

#             total_minutes = hours * 60 + minutes
#             adapter['duration'] = total_minutes
#         return item

#     def clean_actors(self, item):
#         adapter = ItemAdapter(item)
#         actors = adapter.get('actors')
#         if actors:
#             actors_cleaned = ', '.join([actor.strip() for actor in actors])
#             adapter['actors'] = actors_cleaned
#         return item

#     def clean_description(self, item):
#         adapter = ItemAdapter(item)
#         description = adapter.get('description')
#         if description:
#             description_cleaned = description.strip().replace('\n', ' ')
#             adapter['description'] = description_cleaned
#         return item

#     def clean_director(self, item):
#         adapter = ItemAdapter(item)
#         director = adapter.get('director')
#         if director:
#             director_cleaned = ', '.join([dir.strip() for dir in director])
#             adapter['director'] = director_cleaned
#         return item

#     def clean_genre(self, item):
#         adapter = ItemAdapter(item)
#         genre = adapter.get('genre')
#         if genre:
#             genre_cleaned = ', '.join([g.strip() for g in genre if g.strip() != '|'])
#             adapter['genre'] = genre_cleaned
#         return item

#     def clean_original_title(self, item):
#         adapter = ItemAdapter(item)
#         original_title = adapter.get('original_title')
#         if original_title:
#             original_title_cleaned = original_title.strip().replace('\n', ' ')
#             adapter['original_title'] = original_title_cleaned
#         return item

#     def clean_score(self, item):
#         adapter = ItemAdapter(item)
#         score = adapter.get('score')
#         if score:
#             score_cleaned = score.strip().replace('\n', ' ')
#             adapter['score'] = score_cleaned
#         return item

#     def clean_title(self, item):
#         adapter = ItemAdapter(item)
#         title = adapter.get('title')
#         if title:
#             title_cleaned = title.strip().replace('\n', ' ')
#             adapter['title'] = title_cleaned
#         return item

#     def clean_year(self, item):
#         adapter = ItemAdapter(item)
#         year = adapter.get('year')
#         if year:
#             year_cleaned = year.strip().replace('\n', ' ')
#             adapter['year'] = year_cleaned
#         return item
#####FIN DBEAVER##################################################
    ###############################################################
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from .models import Film, Actor, Director, engine
import re

class AlocineScraperPipeline:
    def process_item(self, item, spider):
        item = self.clean_duration(item)
        item = self.clean_actors(item)
        item = self.clean_description(item)
        item = self.clean_director(item)
        item = self.clean_genre(item)
        item = self.clean_original_title(item)
        item = self.clean_score(item)
        item = self.clean_title(item)
        item = self.clean_year(item)
        return item

    def clean_duration(self, item):
        adapter = ItemAdapter(item)
        duration = adapter.get('duration')
        if duration:
            duration_text = ' '.join(duration).strip().replace('\n', '').replace(' ,', '').replace('  ', ' ')
            hours_match = re.search(r'(\d+)\s*h', duration_text)
            minutes_match = re.search(r'(\d+)\s*min', duration_text)

            hours = int(hours_match.group(1)) if hours_match else 0
            minutes = int(minutes_match.group(1)) if minutes_match else 0

            total_minutes = hours * 60 + minutes
            adapter['duration'] = total_minutes
        return item

    def clean_actors(self, item):
        adapter = ItemAdapter(item)
        actors = adapter.get('actors')
        if actors:
            actors_cleaned = ', '.join([actor.strip() for actor in actors])
            adapter['actors'] = actors_cleaned
        return item

    def clean_description(self, item):
        adapter = ItemAdapter(item)
        description = adapter.get('description')
        if description:
            description_cleaned = description.strip().replace('\n', ' ')
            adapter['description'] = description_cleaned
        return item

    def clean_director(self, item):
        adapter = ItemAdapter(item)
        director = adapter.get('director')
        if director:
            director_cleaned = ', '.join([dir.strip() for dir in director])
            adapter['director'] = director_cleaned
        return item

    def clean_genre(self, item):
        adapter = ItemAdapter(item)
        genre = adapter.get('genre')
        if genre:
            genre_cleaned = ', '.join([g.strip() for g in genre if g.strip() != '|'])
            adapter['genre'] = genre_cleaned
        return item

    def clean_original_title(self, item):
        adapter = ItemAdapter(item)
        original_title = adapter.get('original_title')
        if original_title:
            original_title_cleaned = original_title.strip().replace('\n', ' ')
            adapter['original_title'] = original_title_cleaned
        return item

    def clean_score(self, item):
        adapter = ItemAdapter(item)
        score = adapter.get('score')
        if score:
            score_cleaned = score.strip().replace('\n', ' ')
            adapter['score'] = score_cleaned
        return item

    def clean_title(self, item):
        adapter = ItemAdapter(item)
        title = adapter.get('title')
        if title:
            title_cleaned = title.strip().replace('\n', ' ')
            adapter['title'] = title_cleaned
        return item

    def clean_year(self, item):
        adapter = ItemAdapter(item)
        year = adapter.get('year')
        if year:
            year_cleaned = year.strip().replace('\n', ' ')
            adapter['year'] = year_cleaned
        return item
class PostgresPipeline:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        self.session = self.Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        try:
            film = Film(
                title=item['title'],
                original_title=item['original_title'],
                score=item['score'],
                genre=item['genre'],
                year=item['year'],
                duration=item['duration'],
                description=item['description'],
            )
            self.session.add(film)
            self.session.commit()

            for actor_name in item['actors'].split(', '):
                actor = self.session.query(Actor).filter_by(name=actor_name).first()
                if not actor:
                    actor = Actor(name=actor_name)
                    self.session.add(actor)
                film.actors.append(actor)

            for director_name in item['director'].split(', '):
                director = self.session.query(Director).filter_by(name=director_name).first()
                if not director:
                    director = Director(name=director_name)
                    self.session.add(director)
                film.directors.append(director)

            self.session.commit()
        except Exception as e:
            spider.logger.error(f"Erreur lors de l'insertion dans PostgreSQL: {e}")
            self.session.rollback()
        return item
