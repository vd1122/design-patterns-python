#!/usr/bin/env python

"""
Behavioural Pattern --> Mediator Pattern

This pattern de-couples components by making them communicate indirectly, through a special mediator object.
"""

class NewsStudio:

    def broadcast(self, reporter, news):
        print(news)


class Reporter(object):

    def __init__(self, name):
        self.name = name
        self.news_studio = NewsStudio()

    def report_news(self, news):
        self.news_studio.broadcast(self, news)

    def __str__(self):
        return self.name


reporter1 = Reporter('John')
reporter2 = Reporter('Jane')

reporter1.report_news(f"This is {reporter1} reporting from London.")
reporter2.report_news(f"This is {reporter1} reporting from New York.")
