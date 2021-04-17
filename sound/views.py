from rest_framework.serializers import ModelSerializer
from sound.models import Song,Podcast,Audiobook
from sound.serializers import SongSerializer,PodcastSerializer,AudiobookSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
class ListSoundAPIView(ListAPIView):    
    def get_queryset(self):
        model = self.kwargs.get('slug')
        if "song" == model:
            return Song.objects.all()
        elif "podcast" == model:
            return Podcast.objects.all()
        elif "audiobook"== model:
            return Audiobook.objects.all()
        else:
            pass           

    def get_serializer_class(self):
        model = self.kwargs.get('slug')
        model=model.lower()
        if("song" ==  model):
            return SongSerializer
        elif("podcast" == model):
            return PodcastSerializer
        elif("audiobook" == model):
            return AudiobookSerializer
        else:
            pass
               
class CreateSoundAPIView(CreateAPIView):

    def get_queryset(self):
        model = self.kwargs.get('slug')
        model=model.lower()
        if "song" == model:
            return Song.objects.all()
        elif "podcast"== model:
            return Podcast.objects.all()
        elif "audiobook" == model:
            return Audiobook.objects.all()
        else:
            pass    

    def get_serializer_class(self):
        model = self.kwargs.get('slug')
        model=model.lower()
        if("song" == model):
            return SongSerializer
        elif("podcast" == model):
            return PodcastSerializer
        elif("audiobook" == model):
            return AudiobookSerializer
        else:
            pass
from rest_framework import permissions
class DeleteSoundAPIView(RetrieveDestroyAPIView):
    def get_queryset(self):
        model = self.kwargs.get('slug')
        model =model.lower()
        if "song" == model:
            return Song.objects
            return Podcast.objects.all()
        elif "audiobook"  == model:
            return Audiobook.objects.all()
        else:
            pass           

    def get_serializer_class(self):
        model = self.kwargs.get('slug')
        model=model.lower()
        #model = self.request.path[1:]
        if "song"  == model:
            return SongSerializer
        elif "podcast"  == model:
            return PodcastSerializer
        elif "audiobook" == model:
            return AudiobookSerializer
        else:
            pass


class UpdateSoundAPIView(RetrieveUpdateAPIView):
    def get_queryset(self):
        model = self.kwargs.get('slug')
        if "song"  == model:
            return Song.objects.all()
        elif "podcast"  == model:
            return Podcast.objects.all()
        elif "audiobook"  == model:
            return Audiobook.objects.all()
        else:
            pass           

    def get_serializer_class(self):
        model = self.kwargs.get('slug')
        model=model.lower()
        if"song"  == model:
            return SongSerializer
        elif"podcast"  == model:
            return PodcastSerializer
        elif("audiobook"  == model):
            return AudiobookSerializer
        else:
            pass