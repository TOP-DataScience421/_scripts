from pandas import read_csv

from pathlib import Path
from sys import path


movies_raw = read_csv(Path(path[0]) / 'movies.csv')
ratings_raw = read_csv(Path(path[0]) / 'ratings.csv')


ratings_mean = ratings_raw.groupby('movie_id')['rating'].mean()
ratings_mean.sort_values(ascending=False, inplace=True)

mask = movies_raw['movie_id'].isin(ratings_mean.index[:10])
print(movies_raw[mask])

#       movie_id                                              title                        genres
# 1647      2196                                   Knock Off (1998)                        Action
# 5287      8738  Woman Is a Woman, A (femme est une femme, Une)...  Comedy|Drama|Musical|Romance
# 5308      8804     Story of Women (Affaire de femmes, Une) (1988)                         Drama
# 6499     53355                     Sun Alley (Sonnenallee) (1999)                Comedy|Romance
# 7581     86237                                 Connections (1978)                   Documentary
# 8873    134004                                What Love Is (2007)                Comedy|Romance
# 8877    134095                                     My Love (2006)               Animation|Drama
# 8878    134109                                   Radio Day (2008)                        Comedy
# 9180    149350                              Lumberjack Man (2015)                 Comedy|Horror
# 9185    149508                                  Spellbound (2011)                Comedy|Romance


