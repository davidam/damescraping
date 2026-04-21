#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damescraping; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from unittest import TestCase
import newspaper
import nltk
from newspaper import Article

class TestNewspaper(TestCase):
    def test_minimal(self):
        url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
        article = Article(url)
        article.download()
        html_txt = article.html
        html_txt = html_txt.casefold()
        self.assertTrue("doctype html" in html_txt)

        
    # def test_categories(self):
    #     cnn_paper = newspaper.build('http://cnn.com')
    #     categories = []
    #     for category in cnn_paper.category_urls():
    #         categories.append(category)
    #     self.assertTrue(len(categories) > 1)
    #     print("------------------------------------")
    #     print(categories)

    # def test_article(self):
    #     url = "https://timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms"
    #     article = Article(url)
    #     article.download()
    #     article.parse()
    #     nltk.download('punkt_tab')
    #     article.nlp()
    #     self.assertTrue('indian' in article.keywords)
