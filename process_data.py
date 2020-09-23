# goals: we'd like to generate a few charts
# ideally, we can generate the 'position -> free throw percentage distribution' as one chart
# secondly, we'd want individual data of year: [{player name, free throw percentage, total free throws taken}]
# thirdly, we'd like 'total free throws per year'

import json
import math
#for year in range(1980, 2021):


yearly_pdl = {}
yearly_player = {}
yearly_total = []

for year in range(1980, 2021):
    position_data = {}
    player_data = []
    year_total = {'year': year, 'fta': 0, 'ftm': 0}
    with open(f'./raw_data/{year}_player_season_totals.json') as json_file:
        data = json.load(json_file)


        for player in data:
            position = player['positions'][0]
            fta = player['attempted_free_throws']
            ftm = player['made_free_throws']
            if fta > 20:
                year_total['fta'] += fta
                year_total['ftm'] += ftm
                pct_bucket = math.floor(((1.0 * ftm) / fta) * 100)
                if pct_bucket not in position_data:
                    position_data[pct_bucket] = {}
                
                if position not in position_data[pct_bucket]:
                    position_data[pct_bucket][position] = 0
                
                position_data[pct_bucket][position] += fta

                player_data.append({'name': player['name'], 'ft_percent': pct_bucket, 'fta': fta, 'ftm': ftm, 'position':position})
        
    pdl = []
    for key, val in position_data.items():
        val['PCT'] = key
        pdl.append(val)
    yearly_pdl[year] = pdl
    yearly_player[year] = player_data
    yearly_total.append(year_total)

#print(yearly_pdl)

with open('./data/yearly_pdl.json', 'w') as outfile:
    json.dump(yearly_pdl, outfile)
with open('./data/yearly_player.json', 'w') as outfile:
    json.dump(yearly_player, outfile)
with open('./data/yearly_total.json', 'w') as outfile:
    json.dump(yearly_total, outfile)


# json.dump(yearly_pdl, 'yearly_pdl.json')
# json.dump(yearly_player, 'yearly_player.json')
# json.dump(yearly_total, 'yearly_total.json')
# print(yearly_total)
