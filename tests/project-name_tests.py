from nose.tools import *
from writer.readability import Ranalyzer
from writer.readability import UnknownWordError

def test_nsyl():
    r = Ranalyzer("The quick brown fox jumps over the lazy dog.")
    assert_equal(r._nsyl("syllable")[0], 3)
    assert_raises(UnknownWordError, r._nsyl, "monosyllabic")

def test_nsyl_best_guess():
     r = Ranalyzer("The quick brown fox jumps over the lazy dog.")
     assert_equal(r._nsyl_best_guess("monosyllabic"), 5)
     
def test_total_syllables():
    r = Ranalyzer("The quick brown fox jumps over the lazy dog.")
    assert_equal(r._total_syllables(), 11)

def test_total_sentences():
    r = Ranalyzer("The fox was a bit of a dick. The dog ate his mother. Whose mother, he asked? Why, mother Jones of course!")
    assert_equal(r._total_sentences(), 4)

def test_total_words():
    f = open('tests/sample.txt', 'r')
    r = Ranalyzer(f.read())
    f.close()
    assert_equal(r._total_words(), 161)

def test_total_complex_words():
    r = Ranalyzer("The gentleman will not be allergic to my medicine.")
    assert_equal(r._total_complex_words(), 3)

def test_word():
    r = Ranalyzer("The gentleman will not be allergic to my medicine.")
    assert_equal(r._nsyl("medicine")[0], 3)
     
def test_reading_ease():
    f = open('tests/sample.txt', 'r')
    r = Ranalyzer(f.read())
    f.close()
    assert_equal(r.reading_ease(), 63)
     
def test_grade_level():
    f = open('tests/sample.txt', 'r')
    r = Ranalyzer(f.read())
    f.close()
    assert_equal(r.grade_level(), 7)

def test_gunning_fog():
    f = open('tests/sample.txt', 'r')
    r = Ranalyzer(f.read())
    f.close()
    assert_equal(r.gunning_fog(), 9.57)
    
@classmethod
def setup_class(klass):
    """This method is run once for each class before any tests are run"""

@classmethod
def teardown_class(klass):
    """This method is run once for each class _after_ all tests are run"""

def setUp(self):
    """This method is run once before _each_ test method is executed"""

def teardown(self):
    """This method is run once after _each_ test method is executed"""