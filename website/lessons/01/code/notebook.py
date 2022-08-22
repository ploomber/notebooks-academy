# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Exploring music data
#
# ## Data loading
#
# - [Data source](http://millionsongdataset.com/lastfm/)
# - Data is a zipped file with JSON files

# %%
import zipfile
import json
from urllib import request
from pathlib import Path
from glob import iglob

import pandas as pd
import seaborn as sns

# %%
home = Path('~/noteboooks-academy/data').expanduser()
home.mkdir(exist_ok=True, parents=True)

name = "lastfm_test"
url = f"http://millionsongdataset.com/sites/default/files/lastfm/{name}.zip"
path_to_zip = Path(home, f"{name}.zip")
path_to_dir = Path(home, name)

if not path_to_zip.exists():
    print(f'downloading: {path_to_zip}')
    request.urlretrieve(url, filename=path_to_zip)

if not path_to_dir.exists():
    print(f'unzipping: {path_to_zip}')
    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(path=home)

# %% [markdown]
# ## Parsing JSONs into a data frame
#
# - We parse the JSON files and convert to a data frame
# - 104k records

# %%
# reading all the JSON files will take a ~2 minutes
# you can set this value to a number to only load a few files
n = None

files_all = iglob(f"{name}/**/*.json", recursive=True)

if n is not None:
    files = [next(files_all) for _ in range(n)]
else:
    files = files_all

raw = [json.loads(Path(path).read_text()) for path in files]

# %%
df = pd.DataFrame.from_records(raw)

# %%
df.head()

# %%
df.shape

# %% [markdown]
# ## Artists
#
# - The `artist` column has no null values
# - There are 7.4k unique values

# %%
df.artist.isna().sum().mean()

# %%
df.artist.nunique()

# %%
artists = df.groupby('artist').size().sort_values(ascending=False).head(10)

# %%
sns.barplot(x=artists, y=artists.index, orient="h")

# %% [markdown]
# ## Tags
#
# - `tags` contain classifiers for each song
# - It's a list of (key, value) tuples. Example: (rock, 100)
# - The median is a single tag
# - There is an outlier with 100 tags

# %%
df.tags.sample(n=10)


# %%
def tags_len(tags):
    return len(tags)         

df['tags_len'] = df.tags.apply(tags_len)

# %% [markdown]
# There's a long tail of tags:

# %%
df['tags_len'].describe()

# %%
sns.displot(df['tags_len'])


# %%
def parse_tags(tags):
    if not tags:
        return {}
    
    # we'll only process the first three     
    to_process = tags[:3]
    
    # convert: [[key0, value0], [key1, value1], ...]
    # into: [key0, key1, ...], [value0, value1, ...], 
    keys, values = zip(*to_process[:3])
    
    # convert to: column_name: key
    keys_mapping = {f'tag_{i}': k for i, k in enumerate(keys)}
    # convert to: column_name: value
    values_mapping = {f'value_{i}': k for i, k in enumerate(values)}
    
    return {**keys_mapping, **values_mapping}


# %%
df_tags = pd.DataFrame.from_records(df.tags.apply(parse_tags))
df_tags.head()

# %%
df_tagged = df.join(df_tags)

# %% [markdown]
# ## Tracks tagged as "rock"
#
# - 2.5k tracks tagged as rock
# - Bryan Adams overly represented with 100 songs
# - Followed by Toto, with 33

# %%
rock = df_tagged[df_tagged["tag_0"] == "rock"]
rock.head()

# %%
rock.shape

# %%
artists_rock = rock.groupby('artist').size().sort_values(ascending=False).head(10)
artists_rock.head()

# %%
sns.barplot(x=artists_rock, y=artists_rock.index, orient="h")
