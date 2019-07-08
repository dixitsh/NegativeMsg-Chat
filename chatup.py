from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
from new import myinput_network
# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):

  print( 'recived my event: ' + str( json ) )
  mesg=json['message']
  result,x=myinput_network(mesg)
  result=[r*100 for r in result]
  if result[0]>30 or result[1]>30 or result[2]>30 or result[3]>30 or result[4]>30 or result[5]>30:
  	json['message'] = "Warning: Vulgar Message Detected"
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )