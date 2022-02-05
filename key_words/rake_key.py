# -*- coding: utf8 -*-
import pymorphy2
from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, Doc, NewsNERTagger, MorphVocab

from rake_nltk import Rake
from rutermextract import TermExtractor

morph = pymorphy2.MorphAnalyzer()

morph_vocab = MorphVocab()
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
ner_tagger = NewsNERTagger(emb)

my_stopwords = open('key_words/stops.txt', 'r', encoding='utf-8')
my_stopwords = my_stopwords.readlines()

for ind, val in enumerate(my_stopwords):
    my_stopwords[ind] = val.rstrip('\n').strip()

marks = "'?_–=-!()[]{};?@#$%:'\"\,./^&;*_«»~`‹…›—·"


class Hashtags:

    @staticmethod
    def rake_key_words(self):
        r = Rake(min_length=1, max_length=3, include_repeated_phrases=False, punctuations=set(marks),
                 stopwords=set(my_stopwords))
        r.extract_keywords_from_text(self)
        key_phrases_ranked = r.get_ranked_phrases()[:7]
        return key_phrases_ranked

    @staticmethod
    def terms_extractor(self):
        terms = []
        term_extractor = TermExtractor()
        term_extractor_self = term_extractor(self)
        for term in term_extractor_self:
            terms.append(term.normalized)
        return terms[:12]

    @staticmethod
    def names_extraction(self):
        names = []
        doc = Doc(self)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.tag_ner(ner_tagger)
        for span in doc.spans:
            span.normalize(morph_vocab)
            names.append(span.normal)
        return names

    def all_compile(self, message):
        key_phrases_ranked = self.rake_key_words(message)
        names = self.names_extraction(message)
        terms = self.terms_extractor(message)

        all_phrases = terms + names + key_phrases_ranked

        for words in all_phrases.copy():
            for word in words.split():
                p = morph.normal_forms(word)[0]
                if p in (my_stopwords) and (words in all_phrases):
                    all_phrases.remove(words)

        for index, phrase in enumerate(all_phrases):
            all_phrases[index] = '#' + phrase.translate({ord(i): None for i in marks}).strip().replace("  ",
                                                                                                       "_").replace(" ",
                                                                                                                    "_")
        all_phrases = set(all_phrases)
        return str(all_phrases)[1:-1].replace("'", "")
