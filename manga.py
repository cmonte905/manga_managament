"""
Holds chapter name and current chapter, will get stored in an array later on
a data file.
"""
class manga():

    def __init__(self, m_name, current_chapter, website=''):
        self.name = m_name
        self.chapter = current_chapter
        self.website = website

    def __str__(self):
        return("Manga name: {0}; Current Chapter: {1}".format(self.name, self.chapter))

    def get_site(self):
        return self.website

    def update_chapter(self, new_chapter):
        """
        Updates the new chapter from a manga object
        """
        self.chapter = new_chapter

    def update_site(self, new_site):
        self.website = new_site
