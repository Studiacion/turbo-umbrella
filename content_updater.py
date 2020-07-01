import sqlite3
conn = sqlite3.connect('dev.db')

c = conn.cursor()

f = open("video_ID.txt", "r")
video_ID_MX = f.readline()
video_ID_US = f.readline()
video_ID_BR = f.readline()
video_ID_CL = f.readline()

f.close()

c.execute("UPDATE pages_richtextpage SET content = '<h2 style=\"text-align: center;\">Mexico</h2>\n<p style=\"text-align: center;\"><iframe allowfullscreen=\"allowfullscreen\" height=\"315\" src=\"https://www.youtube.com/embed/{}\" width=\"560\"></iframe></p>\n<h2 style=\"text-align: center;\">United States</h2>\n<p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>\n<h2 style=\"text-align: center;\">Brazil</h2>\n<p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>\n<h2 style=\"text-align: center;\">Chile</h2>\n<p><iframe width=\"560\" height=\"315\" style=\"display: block; margin-left: auto; margin-right: auto;\" allowfullscreen=\"allowfullscreen\" src=\"https://www.youtube.com/embed/{}\"></iframe></p>' WHERE page_ptr_id = '3'".format(video_ID_MX, video_ID_US, video_ID_BR, video_ID_CL))

conn.commit()

conn.close()


'''
line = file1.readline() 


<h2 style="text-align: center;">Mexico</h2>
<p style="text-align: center;"><iframe width="560" height="315" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/ui_9qAoosls"></iframe></p>
<p style="text-align: center;"></p>
<h2 style="text-align: center;">United States</h2>
<p><iframe width="560" height="315" style="display: block; margin-left: auto; margin-right: auto;" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/q1p5t_GJHCY"></iframe></p>
'''

'''

# link 1
<p><iframe allowfullscreen="allowfullscreen" height="315" src="https://www.youtube.com/embed/VMyjxx3y27Y" width="560"></iframe></p>

# link 2
<p><iframe allowfullscreen="allowfullscreen" height="315" src="https://www.youtube.com/embed/BfBT1D04SoE" width="560"></iframe></p>
'''
