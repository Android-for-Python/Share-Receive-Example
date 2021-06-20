from android import mActivity,autoclass,activity
from threading import Thread
from storage import SharedStorage

Intent = autoclass('android.content.Intent')

# Source https://github.com/Android-for-Python/Share-Receive-Example

'''
   NOTE: intent_filter.xml and intent_handler() must be customized 
         according to the file types handled by the app.
         The intent_filter tells Android what data types this app can handle
         The intent_handler passes the shared data to the app.

   READ:
   https://developer.android.com/training/sharing/receive#handling-content

./intent_filter.xml

    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="video/mp4" />
    </intent-filter>
'''


class ShareRcv():
    # Must be instantiated in App.build() 

    def __init__(self,text_callback=None,video_callback=None):              
        self.text_callback=text_callback
        self.video_callback=video_callback
        self.intent = mActivity.getIntent()
        self.intent_handler(self.intent)
        activity.bind(on_new_intent=self.intent_handler)

    def to_file(self,uri,MIME_type):
        try:
            file_path = SharedStorage().retrieveUri(uri)
            self.video_callback(file_path,MIME_type)
        except Exception as e:
            print('ShareRcv.to_file() ' + str(e))

    def intent_handler(self,intent):
        if Intent.ACTION_SEND == intent.getAction():
            MIME_type = intent.getType()
            if MIME_type == "text/plain":
                text = intent.getStringExtra(Intent.EXTRA_TEXT)
                if text and self.text_callback:
                    self.text_callback(text,MIME_type)
            elif MIME_type == "video/mp4":
                uri = intent.getParcelableExtra(Intent.EXTRA_STREAM)
                if uri and self.video_callback:
                    Thread(target=self.to_file, args=[uri,MIME_type],
                           daemon=True).start()
