import sqlite3
conn = sqlite3.connect('dev.db')

c = conn.cursor()

f = open("video_ID.txt", "r")
video_ID = f.read()
f.close()

c.execute("UPDATE pages_richtextpage SET content = '<p><iframe allowfullscreen=\"allowfullscreen\" height=\"315\" src=\"https://www.youtube.com/embed/{}\" width=\"560\"></iframe></p>' WHERE page_ptr_id = '3'".format(video_ID))

conn.commit()

conn.close()

'''

# link 1
<p><iframe allowfullscreen="allowfullscreen" height="315" src="https://www.youtube.com/embed/VMyjxx3y27Y" width="560"></iframe></p>

# link 2
<p><iframe allowfullscreen="allowfullscreen" height="315" src="https://www.youtube.com/embed/BfBT1D04SoE" width="560"></iframe></p>
'''
