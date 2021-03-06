# Receive a Share from another app

*Receive a file or text shared by another app.*

### **Depreciated, use [share_receive_example](https://github.com/Android-for-Python/share_receive_example).**

Example of receiving an Android share of a .mp4 file or of plain text. This app on its own does nothing. If another app shares text it displays it, and if another app shares a .mp4 it plays it. You can use the Share example to do this.

Be aware, this app copies the .mp4, 500MB has only a small latency but file management becomes important.

The principles here apply to any file type, but [intent_filter.xml](https://github.com/Android-for-Python/Share-Receive-Example/blob/main/intent_filter.xml) and [sharercv.py](https://github.com/Android-for-Python/Share-Receive-Example/blob/main/sharercv.py) must be customized according to the file types handled by your app.

The buildozer options are documented in [BUILDOZER_README.txt](https://github.com/Android-for-Python/Share-Receive-Example/blob/main/BUILDOZER_README.txt)

