#!/usr/bin/env python3
# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: <John-L-Jones-IV>
# Collaborators: <iamwhil>
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from tkinter import * # mtTkinter is depreciated? 
from datetime import datetime
from datetime import timedelta
import pytz

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate = pubdate.replace(tzinfo=pytz.timezone('GMT'))
#            pubdate = pubdate.astimezone(pytz.timezone('EST'))
#            pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

#======================
# PHRASE TRIGGERS
#======================

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    def get_phrase(self):
        return self.phrase
    def is_phrase_in(self,text):
        """
        Return True if self.phrase is in text, ignoring capitalization, punctuation and repeated spaces
        """
        # remove punctuation
        text_copy = text.lower()
        for c in string.punctuation:
            text_copy = text_copy.replace(c,' ')

        # serperate into lists of words removing spaces
        text_words = text_copy.split()
        phrase_words = self.get_phrase().split()

        # find suspect phrases in text
        suspects = []
        for i in range(len(text_words)):
            if text_words[i] == phrase_words[0]:
                suspects.append( text_words[i:i+len(phrase_words)] )

        # examine suspects
        for suspect in suspects:
            if suspect == phrase_words:
                return True

        return False

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

#======================
# TIME TRIGGERS
#======================

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self,time):
    #   Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
    #   Convert time from string to a datetime before saving it as an attribute.
        dt = datetime.strptime(time,'%d %b %Y %H:%M:%S')
        self.time = dt.replace(tzinfo=pytz.timezone('EST'))
    def get_time(self):
        return self.time

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        trigger_time = self.get_time()
        if pubdate.tzname() is None:
            pubdate = pubdate.replace(tzinfo=None)
            trigger_time = trigger_time.replace(tzinfo=None)

        return pubdate <= trigger_time

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        trigger_time = self.get_time()
        if pubdate.tzname() is None:
            pubdate = pubdate.replace(tzinfo=None)
            trigger_time = self.get_time().replace(tzinfo=None)

        return pubdate >= trigger_time

#======================
# COMPOSITE TRIGGERS
#======================

# Problem 7
class NotTrigger(Trigger):
    def __init__(self,T):
        # T - Trigger
        self.T = T
    def get_T(self):
        return self.T
    def evaluate(self,x):
        # x - NewsStory
        return not self.get_T().evaluate(x)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self,T1,T2):
        self.T1 = T1
        self.T2 = T2
    def get_T1(self):
        return self.T1
    def get_T2(self):
        return self.T2
    def evaluate(self,x):
        # x - NewsStory
        return self.get_T1().evaluate(x) and self.get_T2().evaluate(x)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self,T1,T2):
        self.T1 = T1
        self.T2 = T2
    def get_T1(self):
        return self.T1
    def get_T2(self):
        return self.T2
    def evaluate(self,x):
        # x - NewsStory
        return self.get_T1().evaluate(x) or self.get_T2().evaluate(x)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    stories_out = []
    for t in triggerlist:
        for s in stories:
            if t.evaluate(s):
                stories_out.append(s)

    return stories_out

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # My code ...
    d_trigs = {}
    l_trigs = []
    for line in lines:
        l = line.split(',')
        if l[1] == 'TITLE' and d_trigs.get(l[0]) is None:
            d_trigs[l[0]] = TitleTrigger(l[2])
        elif l[1] == 'DESCRIPTION' and d_trigs.get(l[0]) is None:
            d_trigs[l[0]] = DescriptionTrigger(l[2])
        elif l[1] == 'BEFORE' and d_trigs.get(l[0]) is None:
            d_trigs[l[0]] = BeforeTrigger(l[2]) 
        elif l[1] == 'AFTER' and d_trigs.get(l[0]) is None:
            d_trigs[l[0]] = AfterTrigger(l[2]) 
        elif l[1] == 'NOT' and d_trigs.get(l[0]) is None and isinstance(d_trigs.get(l[2]), Trigger):
            d_trigs[l[0]] = NotTrigger(d_trigs.pop(l[2]))
        elif l[1] == 'AND' and d_trigs.get(l[0]) is None and isinstance( d_trigs.get(l[2]), Trigger) and isinstance(d_trigs.get(l[3]),Trigger):
            d_trigs[l[0]] = AndTrigger(d_trigs.pop(l[2]), d_trigs.pop(l[3]))
        elif l[1] == 'OR' and d_trigs.get(l[0]) is None and isinstance(d_trigs.get(l[2]), Trigger) and isinstance(d_trigs.get(l[3]),Trigger):
            d_trigs[l[0]] = OrTrigger(d_trigs.pop(l[2]), d_trigs.pop(l[3]))
        elif l[0] == 'ADD':
            for t in l[1:]:
                l_trigs.append(d_trigs.get(t))
        else:
            print('Line was not processed:', line)

    return l_trigs

SLEEPTIME = 120 #seconds -- how often we poll
def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #        t1 = TitleTrigger("election")
        #        t2 = DescriptionTrigger("Trump")
        #        t3 = DescriptionTrigger("Clinton")
        #        t4 = AndTrigger(t2, t3)
        #        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .")
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)
            print(triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
