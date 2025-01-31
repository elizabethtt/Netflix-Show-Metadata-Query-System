import doctest

#done

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


def helper_month_as_int(month:str) -> int:
    """ This is a helper function I wrote to make my code for next function more
    compact.
    """
    if month == 'Jan':
        return 1
    elif month == 'Feb':
        return 2
    elif month == 'Mar':
        return 3
    elif month == 'Apr':
        return 4
    elif month == 'May':
        return 5
    elif month == 'Jun':
        return 6
    elif month == 'Jul':
        return 7
    elif month == 'Aug':
        return 8
    elif month == 'Sep':
        return 9 
    elif month == 'Oct':
        return 10
    elif month == 'Nov':
        return 11
    elif month == 'Dec':
        return 12
    

def helper_create_date(date: str) -> Date:
    """ Takes a string representing a valid date and returns a date tuple 
    (as shown in the first type alias). The string passed to the function is 
    guaranteed to be in the 'day-month-year' format. 
    
    >>> helper_create_date('10-Jan-18')
    (2018, 1, 10)
    
    >>> helper_create_date('22-Feb-00')
    (2000, 2, 22)
    
    >>> helper_create_date('31-Dec-01')
    (2001, 12, 31)
    
    >>> helper_create_date('01-Mar-22')
    (2022, 3, 1)
    """
    day,month,year = date.split('-')
    return (int(year) + 2000, helper_month_as_int(month), int(day))


def read_file(filename: str) -> (dict[str, Date], dict[str, list[str]],dict[str, list[str]], dict[str, str]): # type: ignore
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    file_handle = open(filename, 'r', encoding="utf8")
    file_handle.readline()
    data = file_handle.readlines()
    file_handle.close()
    
    date_added = {}
    unique_actor_names = {}
    unique_show_ids = {}
    show_title = {}
    
    for line in data:
        split_line = line.split(',')
        ID = split_line[0]
        Date = helper_create_date(split_line[6])
        date_added[ID] = Date
        
        actors = split_line[4]
        if actors != '':
            actors_list = actors.split(':')
            unique_actors = list(dict.fromkeys(actors_list))
            unique_actor_names[ID] = unique_actors
            
        categories = split_line[10]
        if categories != '':
            categories_list = categories.split(':')
            for category in categories_list:
                unique_show_ids.setdefault(category, []).append(ID)
        
        title = split_line[2]
        show_title[ID] = title
        
    return tuple((date_added, unique_actor_names, unique_show_ids, show_title))
    
    

def helper_check_date(show_ids: list[str], date_added: dict[str, Date],
                      date: Date) -> list[str]:
    """ This function returns a new list of show ids that were added to Netflix before
    the given date and exist in the show_ids
    """
    result = []
    
    for ID in show_ids:
        #we know that id exists in the date_added dictionary because the show_ids 
        #list was created from the categories dictionary
        date_added_for_id = date_added.get(ID)
        if date_added_for_id < date:
            result.append(ID)
    return result


def helper_check_actors(show_ids: list[str], unique_actor_names: dict[str, list[str]],
                        actors: list[str]) -> list[str]:
    """ This function returns a new list of show ids that have at least one in 
    common with the actors list. If no actors are specified in the actors list, 
    all show_ids will be returned
    """
    result = []
    
    if len(actors) == 0:
        return show_ids
    
    for ID in show_ids:
        actors_list = unique_actor_names.get(ID)
        
        if actors_list != None:     
            actors_in_common = set(actors_list).intersection(actors)
            
            if len(actors_in_common) > 0:
                result.append(ID)
    return result            


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
      If no actors are specified (empty list), all actors in library are valid;
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE 
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]
    """
    # TODO: complete this function according to the documentation
    date_added, unique_actor_names, unique_show_ids, show_title = read_file(filename)
    
    potential_ids = unique_show_ids.get(category)
    
    if potential_ids == None:
        return []
    
    potential_ids = helper_check_date(potential_ids, date_added, date)
    final_ids = helper_check_actors(potential_ids, unique_actor_names, actors)
    result = []
    
    for ID in final_ids:
        title = show_title.get(ID)
        result.append(tuple((title, ID)))
    result.sort()
    return result