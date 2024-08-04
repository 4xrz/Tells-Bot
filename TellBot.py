import requests,os
import uuid
import json,random
import cloudscraper
from tellon import Info_Account
from time import sleep
from kvsqlite.sync import Client
from telebot import *

mi =types.InlineKeyboardMarkup(row_width=3)
bannn = types.InlineKeyboardButton(text='حظر شخص ❌ ',callback_data='ban')
unban = types.InlineKeyboardButton(text='الغاء حظر شخص ✔️',callback_data='unban')
ahs = types.InlineKeyboardButton(text='الاحصائيات ',callback_data='ah')
addm= types.InlineKeyboardButton(text='اضافة نقاط',callback_data='am')
mi.add(bannn,unban)

mi.add(ahs)
mi.add(addm)

mb = types.InlineKeyboardMarkup(row_width=2)

back = types.InlineKeyboardButton(text='رجوع',callback_data='back')

ban = Client('ban.hex')
info = Client('info.hex')
idd=  Client('id.hex')
ow = 7345974968

bot = TeleBot('7232694227:AAH36uF1fc0TtGgSO5T4-DfNNTA7i9Gn9yU')

#def comp():
#	bot.send_message(message.chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')



				




@bot.message_handler(commands=['start'])
def start(m):
	id = m.from_user.id
	am = types.InlineKeyboardMarkup(row_width=2)
	dc = info.get(f"score_{id}")
	co = f'نقاطك : {dc} ،'
	coins = types.InlineKeyboardButton(text=co,
	callback_data='we')
	Arrod = types.InlineKeyboardButton('العروض',callback_data='arod')
	am.add(coins)
	am.add(Arrod)
	#am.add(coins)
	user = m.from_user.username
	fi = m.from_user.first_name
	id = m.from_user.id
	bai = f'ban_{id}'
	iban = ban.exists(bai)
	hg =f'id_{id}'
	sc = info.get(f'score_{id}')
	
	#print(m)
	#print(iban)
	if m.from_user.id == ow and info.exists(f'ow_{ow}')==False:
		bot.reply_to(m,'مرحباً عزيزي المالك 🤭💋،\n اليك قائمة الاوامر الخاصة بك و وياها بوسة على الخد 🫦،',reply_markup=mi)
		info.set(f'ow_{ow}',ow)
		bot.send_message(ow,'احلى مالك 💋 ،')
	if m.from_user.id == info.get(f'ow_{ow}') and info.exists(f'ow_{ow}')== True:
		bot.reply_to(m,'مرحباً عزيزي المالك 🤭💋،\n اليك قائمة الاوامر الخاصة بك و وياها بوسة على الخد 🫦،',reply_markup=mi)
	if iban==True:
		bot.reply_to(m,'ابنلخره انت محظور شني ماعندك كرامة؟')
	if iban== False and info.exists(hg) ==False:
		dj = {'الاسم : ':str(fi),'الايدي : ':str(id),'المعرف : ':'@'+str(user)}
		info.set(f'id_{id}',dj)
		idd.set(f'id_{id}',id)
		info.set(f'score_{id}',50)
		ng = info.get('num')
		info.set('num',ng+1)
		bot.send_message(m.chat.id,f'اهلاً و سهلاً عزيزي في بوت رشق تيلات تيلينيوم .',reply_markup=am)
		hhh = f'''
		تم دخول عضو جديد الى البوت 🥳 ،
		
		الاسم : {fi} ،
		اليوزر : @{user} ،
		الايدي : {id} ،
		'''
		bot.send_message(ow,
		hhh)
	if iban== False and info.exists(hg) ==True:
		bot.send_message(m.chat.id,'اهلاً و سهلاً عزيزي في بوت رشق تيلات تيلينيوم .',reply_markup=am)
	if info.get('num')==None:
		info.set('num',0)
	

@bot.callback_query_handler(func=lambda call : True)
def oa(c):
		gn = info.get('num')
		
		data = c.data
		if data =='ban':
			#bot.send_message(ow,'ارسل ايديه ليتم حظره ،')
			m = c.message.text
			iu = c.message.from_user.id
			jj = bot.send_message(ow,'ارسل ايديه ليتم حظره ،')
			bot.register_next_step_handler(jj,baan)
		if data=='unban':
			jjj = bot.send_message(c.message.chat.id,'ارسل ايديه ليتم الغاء حظره ،')
			bot.register_next_step_handler(jjj,unbaan)
		
		if data =='ah':
			print(info.get('num'))
			bot.send_message(ow,f'الاحصائيات : \n‹عدد مستخدمين البوت : {gn} ، ')
			
		if data =='am':
			zaam = bot.send_message(c.message.chat.id,'ارسل ايديه ليتم اضافة نقاط لحسابه ،')
			bot.register_next_step_handler(zaam,zam)
		if data =='arod':
			bot.delete_message(c.message.chat.id , c.message.message_id)
			
			tels = types.InlineKeyboardMarkup(row_width=2)
			ft = types.InlineKeyboardButton(text='5 Tells',callback_data='5')
			tt = types.InlineKeyboardButton(text='10 Tells',callback_data='10')
			twt = types.InlineKeyboardButton(text='20 Tells',callback_data='20')
			fwt = types.InlineKeyboardButton(text='40 Tells',callback_data='40')
			tels.add(ft)
			tels.add(tt)
			tels.add(twt)
			tels.add(fwt)
			bot.send_message(c.message.chat.id,
			text='اهلاً عزيزي في قائمة العروض'
			,reply_markup=tels)
		if data =='5':
			bot.delete_message(c.message.chat.id , c.message.message_id)
			se5 = bot.send_message(c.message.chat.id,'ارسل اليوزر ليتم الرشق :) ')
			bot.register_next_step_handler(se5,s5)
		if data =='10':
			bot.delete_message(c.message.chat.id , c.message.message_id)
			se10 = bot.send_message(c.message.chat.id,'ارسل اليوزر ليتم الرشق :) ')
			bot.register_next_step_handler(se10,s10)
		if data =='20':
			bot.delete_message(c.message.chat.id , c.message.message_id)
			se20 = bot.send_message(c.message.chat.id,'ارسل اليوزر ليتم الرشق :) ')
			bot.register_next_step_handler(se20,s20)
		if data=='40':
			bot.delete_message(c.message.chat.id , c.message.message_id)
			se40 = bot.send_message(c.message.chat.id,'ارسل اليوزر ليتم الرشق :) ')
			bot.register_next_step_handler(se40,s40)
@bot.message_handler(func=lambda m : True)
def comp():
	bot.send_message(chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')	
	
@bot.message_handler(func=lambda m : True)
def zam(message):
	m = message.text
	te = m.split()[0]
	z = m.split()[1]
	print(z);print(te)
	info.set(f'score_{te}',info.get(f"score_{te}")+int(z))
	gm = info.get(f"score_{te}")
	bot.reply_to(message,text=f'تم بنجاح اضافة {z} الى حساب رقم {te} ✓ ، اصبح مجموع نقاطه : {gm} ،')
@bot.message_handler(func=lambda m : True)
def s10(m):
	id = m.from_user.id
	whisper = cloudscraper.create_scraper(
	browser={ 'browser': 'chrome', 'platform': 'windows', 'desktop': True})
	user = m.text#input('enter tellon user to get id : ')
	urlg = f"https://api.tellonym.me/profiles/name/{user}"
	paramsg = {
  'previousRouteName': "ScreenFeed",
  'isClickedInSearch': "false",
  'sourceElement': "SearchHistorySuggestion",
  'adExpId': "8",
  'limit': "16"}
	headersg = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'content-type': "application/json;charset=utf-8",
#  'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q",
  'Cookie': "__cf_bm=4ZTWGo8by3rMLNV4tlah9EAbC50pR.ahV0MIDLryoZ0-1722596501-1.0.1.1-8yXiUGSgM9Muj9FvVhmbXMYNoKb1ox2WMGrdvaFzVUgDFRGUMRaT4ZN804Tuh1Txia5T3CXHbjq3DYSx.6HAWg"}


	
#	d = Info_Account(user)
	responseg = whisper.get(urlg, params=paramsg, headers=headersg)
	
	d = responseg.json()['id']
	if d:
		bot.send_message(m.chat.id,text='تم العثور على الحساب ، \nانتظر دقيقة ليتم اكمال طلبك بنجاح ؛-؛ ')
		dc = info.get(f"score_{id}")
		jk = dc - 5
		info.set(f'score_{id}',jk)
		info.set(f'talb-5{id}',0)
		
		for i in range(20):
			msg = random.randint(0,1000)
			gt=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			url = "https://api.tellonym.me/tells/create"
			payload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			headers = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gt}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
  
			mssg = random.randint(0,1000)
			gtg=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			urrl = "https://api.tellonym.me/tells/create"
			payyload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			heeaders = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gtg}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
			response = whisper.post(url,data=payload,headers=headers)
			reesponse = whisper.post(urrl, data=payyload, headers=heeaders)
			if reesponse.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-5{id}',info.get(f'talb-5{id}')+1)
			if response.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-5{id}',info.get(f'talb-5{id}')+1)
				if info.get(f'talb-5{id}') ==10:
					
					bot.delete_message(m.chat.id , m.message_id)
					s0 = info.set(f'talb-5{id}',0)
					dn = bot.send_message(m.chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')
					bot.register_next_step_handler(dn,comp)
					#comp()
					#bot.register_next_step_handler(s0,comp)
					
				#resend(user)
			else:
				
				print('Error')

	else:
				bot.delete_message(message.chat.id , message.message_id)
				bot.send_message(m.chat.id,'عزيزي ارسل اليوزر الصحيح ، اليوزر خاطئ ،')


@bot.message_handler(func=lambda m : True)
def s10(m):
	id = m.from_user.id
	whisper = cloudscraper.create_scraper(
	browser={ 'browser': 'chrome', 'platform': 'windows', 'desktop': True})
	user = m.text#input('enter tellon user to get id : ')
	urlg = f"https://api.tellonym.me/profiles/name/{user}"
	paramsg = {
  'previousRouteName': "ScreenFeed",
  'isClickedInSearch': "false",
  'sourceElement': "SearchHistorySuggestion",
  'adExpId': "8",
  'limit': "16"}
	headersg = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'content-type': "application/json;charset=utf-8",
#  'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q",
  'Cookie': "__cf_bm=4ZTWGo8by3rMLNV4tlah9EAbC50pR.ahV0MIDLryoZ0-1722596501-1.0.1.1-8yXiUGSgM9Muj9FvVhmbXMYNoKb1ox2WMGrdvaFzVUgDFRGUMRaT4ZN804Tuh1Txia5T3CXHbjq3DYSx.6HAWg"}


	
#	d = Info_Account(user)
	responseg = whisper.get(urlg, params=paramsg, headers=headersg)
	
	d = responseg.json()['id']
	if d:
		bot.send_message(m.chat.id,text='تم العثور على الحساب ، \nانتظر دقيقة ليتم اكمال طلبك بنجاح ؛-؛ ')
		dc = info.get(f"score_{id}")
		jk = dc - 10
		info.set(f'score_{id}',jk)
		info.set(f'talb-10{id}',0)
		
		for i in range(20):
			msg = random.randint(0,1000)
			gt=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			url = "https://api.tellonym.me/tells/create"
			payload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			headers = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gt}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
  
			mssg = random.randint(0,1000)
			gtg=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			urrl = "https://api.tellonym.me/tells/create"
			payyload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			heeaders = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gtg}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
			response = whisper.post(url,data=payload,headers=headers)
			reesponse = whisper.post(urrl, data=payyload, headers=heeaders)
			if reesponse.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-10{id}',info.get(f'talb-10{id}')+1)
			if response.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-10{id}',info.get(f'talb-10{id}')+1)
				if info.get(f'talb-10{id}') ==10:
					
					bot.delete_message(m.chat.id , m.message_id)
					s0 = info.set(f'talb-10{id}',0)
					dn = bot.send_message(m.chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')
					bot.register_next_step_handler(dn,comp)
					#comp()
					#bot.register_next_step_handler(s0,comp)
					
				#resend(user)
			else:
				
				print('Error')

	else:
				bot.delete_message(message.chat.id , message.message_id)
				bot.send_message(m.chat.id,'عزيزي ارسل اليوزر الصحيح ، اليوزر خاطئ ،')

@bot.message_handler(func=lambda m : True)
def s20(m):
	id = m.from_user.id
	whisper = cloudscraper.create_scraper(
	browser={ 'browser': 'chrome', 'platform': 'windows', 'desktop': True})
	user = m.text#input('enter tellon user to get id : ')
	urlg = f"https://api.tellonym.me/profiles/name/{user}"
	paramsg = {
  'previousRouteName': "ScreenFeed",
  'isClickedInSearch': "false",
  'sourceElement': "SearchHistorySuggestion",
  'adExpId': "8",
  'limit': "16"}
	headersg = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'content-type': "application/json;charset=utf-8",
#  'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q",
  'Cookie': "__cf_bm=4ZTWGo8by3rMLNV4tlah9EAbC50pR.ahV0MIDLryoZ0-1722596501-1.0.1.1-8yXiUGSgM9Muj9FvVhmbXMYNoKb1ox2WMGrdvaFzVUgDFRGUMRaT4ZN804Tuh1Txia5T3CXHbjq3DYSx.6HAWg"}


	
#	d = Info_Account(user)
	responseg = whisper.get(urlg, params=paramsg, headers=headersg)
	
	d = responseg.json()['id']
	if d:
		bot.send_message(m.chat.id,text='تم العثور على الحساب ، \nانتظر دقيقة ليتم اكمال طلبك بنجاح ؛-؛ ')
		dc = info.get(f"score_{id}")
		jk = dc - 20
		info.set(f'score_{id}',jk)
		info.set(f'talb-20{id}',0)
		
		for i in range(45):
			msg = random.randint(0,1000)
			gt=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			url = "https://api.tellonym.me/tells/create"
			payload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			headers = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gt}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
  
			mssg = random.randint(0,1000)
			gtg=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			urrl = "https://api.tellonym.me/tells/create"
			payyload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			heeaders = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gtg}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
			response = whisper.post(url,data=payload,headers=headers)
			reesponse = whisper.post(urrl, data=payyload, headers=heeaders)
			if reesponse.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-20{id}',info.get(f'talb-20{id}')+1)
			if response.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-20{id}',info.get(f'talb-20{id}')+1)
				if info.get(f'talb-20{id}') ==20:
					
					bot.delete_message(m.chat.id , m.message_id)
					s0 = info.set(f'talb-20{id}',0)
					dn = bot.send_message(m.chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')
					bot.register_next_step_handler(dn,comp)
					#comp()
					#bot.register_next_step_handler(s0,comp)
					
				#resend(user)
			else:
				
				print('Error')

	else:
				bot.delete_message(message.chat.id , message.message_id)
				bot.send_message(m.chat.id,'عزيزي ارسل اليوزر الصحيح ، اليوزر خاطئ ،')

@bot.message_handler(func=lambda m : True)
def s40(m):
	id = m.from_user.id
	whisper = cloudscraper.create_scraper(
	browser={ 'browser': 'chrome', 'platform': 'windows', 'desktop': True})
	user = m.text#input('enter tellon user to get id : ')
	urlg = f"https://api.tellonym.me/profiles/name/{user}"
	paramsg = {
  'previousRouteName': "ScreenFeed",
  'isClickedInSearch': "false",
  'sourceElement': "SearchHistorySuggestion",
  'adExpId': "8",
  'limit': "16"}
	headersg = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'content-type': "application/json;charset=utf-8",
#  'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q",
  'Cookie': "__cf_bm=4ZTWGo8by3rMLNV4tlah9EAbC50pR.ahV0MIDLryoZ0-1722596501-1.0.1.1-8yXiUGSgM9Muj9FvVhmbXMYNoKb1ox2WMGrdvaFzVUgDFRGUMRaT4ZN804Tuh1Txia5T3CXHbjq3DYSx.6HAWg"}


	
#	d = Info_Account(user)
	responseg = whisper.get(urlg, params=paramsg, headers=headersg)
	
	d = responseg.json()['id']
	if d:
		bot.send_message(m.chat.id,text='تم العثور على الحساب ، \nانتظر دقيقة ليتم اكمال طلبك بنجاح ؛-؛ ')
		dc = info.get(f"score_{id}")
		jk = dc - 40
		info.set(f'score_{id}',jk)
		info.set(f'talb-40{id}',0)
		
		for i in range(55):
			msg = random.randint(0,1000)
			gt=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			url = "https://api.tellonym.me/tells/create"
			payload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			headers = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gt}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
  
			mssg = random.randint(0,1000)
			gtg=random.choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAyNzA0LCJpYXQiOjE3MjI0NjYzNjZ9.d0DXPJm3UBHjDVbsvN8wC2wPlAmQkhV7g19JazPcC7Q',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTgzNTAxLCJpYXQiOjE3MjI2NzcwOTh9.HLbWV7kDWirds4MdZptXykWL3dumWx0_GGrlPQFty80',
			  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA2NTAzODE2LCJpYXQiOjE3MjI2ODM5Njh9.D0tzTf1cng4EjrIzlkyNl8ZbR2DzCDpvBikD4xWx78s'])
			sleep(2)
			#gt = c.get('token')
			urrl = "https://api.tellonym.me/tells/create"
			payyload = json.dumps({
  "senderStatus": 0,
  "previousRouteName": "ScreenProfile",
  "contentType": "CUSTOM",
  "tell": msg,
  "userId":d,
  "limit": 16})

			heeaders = {
  'User-Agent': "okhttp/4.9.2",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'tellonym-client': "android:3.111.1:1979304:12:k65v1_64_bsp",
  'authorization': f"Bearer {gtg}",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "__cf_bm=U_2.kuqq7OSXRg8nRfa8bp0Zrceb.6N5_uPgYvhmfwc-1722421071-1.0.1.1-6oT_hVILNh0QXYjuQ0TMOHwV0tg4GNXNY45CODiA5z2PpgS.iXziplvOXDrdLoao3AmDNMlU8VcI6KPfFPaRvw"}
			response = whisper.post(url,data=payload,headers=headers)
			reesponse = whisper.post(urrl, data=payyload, headers=heeaders)
			if reesponse.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-40{id}',info.get(f'talb-40{id}')+1)
			if response.status_code==200:
				print('\nSend Done ✓ ')
				info.set(f'talb-40{id}',info.get(f'talb-40{id}')+1)
				if info.get(f'talb-40{id}') ==40:
					
					bot.delete_message(m.chat.id , m.message_id)
					s0 = info.set(f'talb-40{id}',0)
					dn = bot.send_message(m.chat.id,'عزيزي تم اكتمال طلبك بنجاح ✓ ')
					bot.register_next_step_handler(dn,comp)
					#comp()
					#bot.register_next_step_handler(s0,comp)
					
				#resend(user)
			else:
				
				print('Error')

	else:
				bot.delete_message(message.chat.id , message.message_id)
				bot.send_message(m.chat.id,'عزيزي ارسل اليوزر الصحيح ، اليوزر خاطئ ،')



@bot.message_handler(func=lambda m : True)
def comp():
	dmj = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'
	bot.send_message(ow,f'عزيزي تم اكتمال طلب {dmj} بنجاح ✓ ')	


bot.infinity_polling()