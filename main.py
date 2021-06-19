# Example of receiving an Android Share of .mp4 file or plain text.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.label import Label
from android import api_version
from android.permissions import request_permissions,Permission,check_permission
from sharercv import ShareRcv
from storage import PrivateStorage
from os.path import exists
from os import remove


class ShareReceiveExample(App):

    def build(self):
        self.label = Label(text='Share some text or video with me')
        self.video = VideoPlayer()
        self.now_playing = None
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.video)
        box.add_widget(self.label)
        if api_version < 29 and not\
           check_permission(Permission.READ_EXTERNAL_STORAGE):
            request_permissions([Permission.READ_EXTERNAL_STORAGE],
                                self.new_listener)
        else:
            self.new_listener(None,None)
        return box

    def new_listener(self,permissions,grants):
        self.share_listener = ShareRcv(text_callback=self.new_text,
                                       video_callback=self.new_video)
        
    def new_text(self, text, MIMEtype):
        self.label.text  = text

    def new_video(self, source, MIMEtype):
        self.video.state  = 'stop'
        self.video.source = source
        self.video.state  = 'play'
        
        if self.now_playing and\
           PrivateStorage().getCacheDir() in self.now_playing and\
           exists(self.now_playing):
            remove(self.now_playing)
        self.now_playing = source
    
    def on_pause(self):
        self.resume_state = self.video.state
        if self.video.state  == 'play':
            self.video.state  = 'pause'
        return True

    def on_resume(self):
        if self.resume_state == 'play':
            self.video.state = 'play'

ShareReceiveExample().run()


