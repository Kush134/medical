from email import message
import websockets
import asyncio
import base64
import json
from config import auth_key
import pyaudio
import datetime


import streamlit as st 
 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
stop_seconds = 30
# starts recording
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	frames_per_buffer=FRAMES_PER_BUFFER
)
 
st.title('Transcribe patient information below.')

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
 
async def send_receive():

	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", auth_key),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		r = await asyncio.sleep(0.1)
		print("Receiving SessionBegins ...")

		session_begins = await _ws.recv()
		print(session_begins)
		print("Sending messages ...")


		async def send():
			while True:
				try:
					#time = datetime.datetime.now()
					data = stream.read(FRAMES_PER_BUFFER)
					data = base64.b64encode(data).decode("utf-8")
					json_data = json.dumps({"terminate_session": True})
					#print(time.time())
					print(session_begins)
					await _ws.send(json_data)

					#if time.time() - session_begins >= stop_seconds:
                    # send terminate message
						#terminate_message = json.dumps({"terminate_session": True})
						#await _ws.send(terminate_message)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e) 
					break
                    
				except Exception as e:
					print(e)
					break
				await asyncio.sleep(0.01)
			return True
	  

		async def receive():
			while True:
				try:
					result_str = await _ws.recv()
					data = json.loads(result_str)
					msg_type = data.get('message_type', 'no type')
					text = data.get('text', 'no text')
					print(text)
					if json.loads(result_str)['message_type'] == 'FinalTranscript':
						print(json.loads(result_str)['text'])
						st.markdown(json.loads(result_str)['text'])
					if msg_type == 'SessionTerminated':
						print('\nthanks for using AssemblyAI...\n')
						break
				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					#assert e.code == 4008
					break

				except Exception as e:
					print(e)
					#assert False, "Not a websocket 4008 error"
	  
		send_result, receive_result = await asyncio.gather(send(), receive())

asyncio.run(send_receive())


