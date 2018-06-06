"""
Holds chapter name and current chapter, will get stored in an array later on
a data file.
"""
class manga():

    def __init__(self, m_name, current_chapter, website='', finished=''):
        self.name = m_name
        self.chapter = current_chapter
        self.website = website
        self.finished = finished

    def __str__(self):
        return("Manga name: {0} | Current Chapter: {1} | Site: {2} | Finished?: {3}".format(self.name, self.chapter, self.website, self.finished))

