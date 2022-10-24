import os
import keep_alive
import scratchattach as scratch3
from random_word  import RandomWords 
from scratchattach import Encoding

keep_alive.keep_alive()

s = RandomWords()
word = Encoding.encode(s.get_random_word())
#generates random word and encodes it in a variable

sessionID = os.environ["sessionID"]
#my password

session = scratch3.Session(sessionID, username="LoIdesMio")
conn = session.connect_cloud("749213684")
client = scratch3.CloudRequests(conn)

@client.request
def want_word():
  s = RandomWords()
  word = s.get_random_word()
  #generates random word and encodes it in a variable
  print("Ping request received")
  return word
client.run()