import datetime
from billy.utils.fulltext import pdfdata_to_text, text_after_line_numbers
from .bills import ARBillScraper
from .legislators import ARLegislatorScraper
from .committees import ARCommitteeScraper
from .events import AREventScraper

metadata = dict(
    name='Arkansas',
    abbreviation='ar',
    legislature_name='Arkansas General Assembly',
    legislature_url='http://www.arkleg.state.ar.us/',
    capitol_timezone='America/Chicago',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms=[
        {'name': '2011-2012',
         'start_year': 2011,
         'end_year': 2012,
         'sessions': ['2011', '2012F']},
        {'name': '2013-2014',
         'start_year': 2013,
         'end_year': 2014,
         'sessions': ['2013', '2013S1', '2014', '2014F', '2014S2']}
        ],
    session_details={
        '2011': {'start_date': datetime.date(2011, 1, 10),
                 'end_date': datetime.date(2011, 4, 27),
                 'display_name': '2011 Regular Session',
                 '_scraped_name': 'Regular Session, 2011',
                 'type': 'primary',
                 'slug': '2011R',
                },
        '2012F': {'start_date': datetime.date(2012, 2, 13),
                 'display_name': '2012 Fiscal Session',
                 '_scraped_name': 'Fiscal Session 2012',
                 'type': 'special',
                 'slug': '2012F',
                },
        '2013': {'start_date': datetime.date(2013, 1, 14),
                 'display_name': '2013 Regular Session',
                 '_scraped_name': 'Regular Session, 2013',
                 'type': 'primary',
                 'slug': '2013R',
                },
        '2013S1': {'start_date': datetime.date(2013, 10, 18),
                 'display_name': '2013 First Extraordinary Session',
                 '_scraped_name': 'First Extraordinary Session, 2013',
                 'type': 'special',
                 'slug': '2013S1',
                },
        '2014': {'start_date': datetime.date(2014, 2, 10),
                 'display_name': '2014 Regular Session',
                 '_scraped_name': 'Regular Session, 2014',
                 'type': 'primary',
                 'slug': '2014R',
                },
        '2014F': {'start_date': datetime.date(2014, 2, 10),
                 'display_name': '2014 Fiscal Session',
                 '_scraped_name': 'Fiscal Session, 2014',
                 'type': 'special',
                 'slug': '2014F',
                },
        '2014S2': {'start_date': datetime.date(2014, 7, 2),
                 'display_name': '2014 Second Extraordinary Session',
                 '_scraped_name': 'Second Extraordinary Session, 2014',
                 'type': 'special',
                 'slug': '2014S2',
                }
        },
    feature_flags=['influenceexplorer'],
    _ignored_scraped_sessions=['Regular Session, 2009',
                               'Fiscal Session, 2010',
                               'Regular Session, 2007',
                               'First Extraordinary Session, 2008',
                               'Regular Session, 2005',
                               'First Extraordinary Session, 2006 ',
                               'Regular Session, 2003 ',
                               'First Extraordinary Session, 2003',
                               'Second Extraordinary Session, 2003',
                               'Regular Session, 2001 ',
                               'First Extraordinary Session, 2002',
                               'Regular Session, 1999',
                               'First Extraordinary Session, 2000',
                               'Second Extraordinary Session, 2000',
                               'Regular Session, 1997 ',
                               'Regular Session, 1995 ',
                               'First Extraordinary Session, 1995 ',
                               'Regular Session, 1993 ',
                               'First Extraordinary Session, 1993 ',
                               'Second Extraordinary Session, 1993',
                               'Regular Session, 1991',
                               'First Extraordinary Session, 1991 ',
                               'Second Extraordinary Session, 1991 ',
                               'Regular Session, 1989',
                               'First Extraordinary Session, 1989',
                               'Second Extraordinary Session, 1989',
                               'Third Extraordinary Session, 1989 ',
                               'Regular Session, 1987 ',
                               'First Extraordinary Session, 1987',
                               'Second Extraordinary Session, 1987',
                               'Third Extraordinary Session, 1987',
                               'Fourth Extraordinary Session, 1987']
    )

def session_list():
    from billy.scrape.utils import url_xpath
    links = url_xpath(
        'http://www.arkleg.state.ar.us/assembly/2013/2013R/Pages/Previous%20Legislatures.aspx',
        '//a')
    sessions = [a.text_content() for a in links if 'Session' in a.attrib.get('title', '')]
    return sessions


def extract_text(doc, data):
    return text_after_line_numbers(pdfdata_to_text(data))
