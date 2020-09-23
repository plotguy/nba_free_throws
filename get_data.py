import random
import time

from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

for year in range (1980, 2021):
    client.players_season_totals(season_end_year=year, output_type=OutputType.JSON, output_file_path=f'./raw_data/{year}_player_season_totals.json')