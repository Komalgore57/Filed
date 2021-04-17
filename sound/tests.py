from django.test import TestCase
from ..models import Song,Podcast,Audiobook


class AuiobookTest(TestCase):
    def setUp(self):
        Audiobook.objects.create(Title = "Rich Dad Poor Dad" ,Author="Robert Kiyosaki", Narrator =  "Mr. Ali",    Duration=10,)
    def test_song(self):
        Data = Audiobook.objects.get(Name='Be Mine')
        self.assertEqual(Data, "Be Mine")
         
class SongTest(TestCase):
    def setUp(self):
        Song.objects.create(ID=1,Name="Be Mine",Duration="10")
    def test_song(self):
        Data = Song.objects.get(Name='Be Mine')
        self.assertEqual(Data, "Be Mine")
class PodcastTest(TestCase):
    def setUp(self):
        Podcast.objects.create(ID=1,Name="Be Mine",Duration="10")
    def test_song(self):
        Data = Podcast.objects.get(Name='Be Mine')
        self.assertEqual(Data, "Be Mine")