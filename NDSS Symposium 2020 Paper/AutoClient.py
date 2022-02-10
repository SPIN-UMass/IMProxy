#!/usr/bin/env python3

from telethon import TelegramClient
from telethon.tl.functions import updates
from telethon.tl import types
import datetime
import time
import os
import random
import sys
from dateutil import tz
import asyncio
import socks


host = '127.0.0.1'
port = 9011
username = '1234'
password = '1234'
proxy = (socks.SOCKS5, host, port, True, username, password)

channel_id1 = sys.argv[1]
channel_id2 = sys.argv[2]
# channel_id3 = sys.argv[3]

COVERT_RATE = 10

directory1 = 'channels-'+str(COVERT_RATE)+'/channel-'+str(COVERT_RATE)+'-'+channel_id1+'.txt' 
directory2 = 'channels-'+str(COVERT_RATE)+'/channel-'+str(COVERT_RATE)+'-'+channel_id2+'.txt'
# directory3 = 'channels/channel-'+channel_id3+'.txt'

update_count1 = 0
update_count2 = 0
update_count3 = 0
TestChannelID1 = 1141095048
TestChannelID2 = 1347586411
TestChannelID3 = 1367067490
counter = 0

now = datetime.datetime.now()

f= open(directory1, 'w')
f.write(str(now) + "\n")
f.close()

f= open(directory2, 'w')
f.write(str(now) + "\n")
f.close()

# f= open(directory3, 'w')
# f.write(str(now) + "\n")
# f.close()


def to_est(time):
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('US/Eastern')
	utc = time.replace(tzinfo = from_zone)
	est = utc.astimezone(to_zone)
	return est

def update_handler(update):
	# print ("OK")
	# print (update)
	global directory
	global TestChannelID1
	global TestChannelID2
	global TestChannelID3
	global update_count1
	global update_count2
	global update_count3
	# print (type(event.is_channel))
	# if event.is_channel == True:
	# 	update = event.original_update
	if isinstance(update, types.UpdateNewChannelMessage):
		# print ("new channel message")
		# print (update)
		update_type = None
		size = None
		if update.message.to_id.channel_id==TestChannelID1:
			update_count1 = update_count1 + 1
			print ("First Channel "+str(update_count1))
			channel_id = update.message.to_id.channel_id
			update_time = update.message.date
			# update_time_est = to_est(update_time)
			# print (update_time_est)
			if update.message.media == None:
				update_type = 'text'
				size = len(update.message.message)
			elif update.message.media != None:
				if isinstance(update.message.media, types.MessageMediaDocument):
					size = update.message.media.document.size
					doc_type = update.message.media.document.mime_type
					if 'image' in doc_type:
						update_type = 'image'
					elif 'video' in doc_type:
						update_type = 'video'
					elif 'audio' in doc_type:
						update_type = 'audio'
				elif isinstance(update.message.media, types.MessageMediaPhoto):
					print ("Photo Message")
					sizes = update.message.media.photo.sizes
					update_type = 'photo'
					for i in range(len(sizes)):
						if sizes[i].type == 'x':
							size = sizes[i].size
			print (size)			
			f = open(directory1, 'a')
			f.write(str(channel_id)+' '+str(update_time)+' '+update_type+' '+str(size)+"\n")
			f.close()

		if update.message.to_id.channel_id==TestChannelID2:
			update_count2 = update_count2 + 1
			print ("Second Channel "+str(update_count2))
			channel_id = update.message.to_id.channel_id
			update_time = update.message.date
			# update_time_est = to_est(update_time)
			if update.message.media == None:
				update_type = 'text'
				size = len(update.message.message)
			elif update.message.media != None:
				if isinstance(update.message.media, types.MessageMediaDocument):
					size = update.message.media.document.size
					doc_type = update.message.media.document.mime_type
					if 'image' in doc_type:
						update_type = 'image'
					elif 'video' in doc_type:
						update_type = 'video'
					elif 'audio' in doc_type:
						update_type = 'audio'
				elif isinstance(update.message.media, types.MessageMediaPhoto):
					print ("Photo Message")
					sizes = update.message.media.photo.sizes
					update_type = 'photo'
					for i in range(len(sizes)):
						if sizes[i].type == 'x':
							size = sizes[i].size

			print (size)			
			f = open(directory2, 'a')
			f.write(str(channel_id)+' '+str(update_time)+' '+update_type+' '+str(size)+"\n")
			f.close()

		# if update.message.to_id.channel_id==TestChannelID3:
		# 	update_count3 = update_count3 + 1
		# 	print ("Third Channel "+str(update_count3))
		# 	channel_id = update.message.to_id.channel_id
		# 	update_time = update.message.date
		# 	# update_time_est = to_est(update_time)
		# 	if update.message.media == None:
		# 		update_type = 'text'
		# 		size = len(update.message.message)
		# 	elif update.message.media != None:
		# 		if isinstance(update.message.media, types.MessageMediaDocument):
		# 			size = update.message.media.document.size
		# 			doc_type = update.message.media.document.mime_type
		# 			if 'image' in doc_type:
		# 				update_type = 'image'
		# 			elif 'video' in doc_type:
		# 				update_type = 'video'
		# 			elif 'audio' in doc_type:
		# 				update_type = 'audio'
		# 		elif isinstance(update.message.media, types.MessageMediaPhoto):
		# 			print ("Photo Message")
		# 			sizes = update.message.media.photo.sizes
		# 			update_type = 'photo'
		# 			for i in range(len(sizes)):
		# 				if sizes[i].type == 'x':
		# 					size = sizes[i].size

			# print (size)			
			# f = open(directory3, 'a')
			# f.write(str(channel_id)+' '+str(update_time)+' '+update_type+' '+str(size)+"\n")
			# f.close()


api_id = 424693
api_hash = 'dee82f0e2c13bfd0c5180a86bae1372c'
phone = '+6584266155'

# client = TelegramClient('TestClient', api_id, api_hash, update_workers = 1)
# client = TelegramClient('TestClient', api_id, api_hash)
# client.connect()

# if not client.is_user_authorized():
# 	client.send_code_request(phone)
# 	client.sign_in(phone, input('Enter the code: '))


# print (messages)

# client.send_message('bahraam72', 'OK')
# @client.on(events.NewMessage)
# async def my_event_handler(event):


client = TelegramClient('TestClient', api_id, api_hash, update_workers = 1)
# client = TelegramClient('TestClient', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code: '))

client.add_update_handler(update_handler)
input('Press Enter to stop this!\n')
# async def main():
# 	await client.start()
# 	await client.run_until_disconnected()

# if __name__ == '__main__':
# 	loop = asyncio.get_event_loop()
# 	loop.run_until_complete(main())
client.disconnect()