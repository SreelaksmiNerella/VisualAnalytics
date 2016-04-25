import json
import requests
from aylienapiclient import textapi
c = textapi.Client("2362d480", "27606230dda39598ad692c0e8809285e")

related = ["Ananda Marga","Japanese Red Army","Maoists","Meitei extremists","Mizo National Front","Muslims","Naga People","Naxalites","Palestinians","People's Liberation Army","Akali Dal Party","All India Sikh Students Federation","Allahs Tigers","Anti Immigrant Activists","Anti Socials","Babbar Khalsa International","Bhinderanwale Tiger Force of Khalistan","Bodo Militants","Communist Party of India","Dishmish Regiment","Dissident","Extremists","Fedayeen Khalq","Gunmen","Gurkha National Liberation Front Insurgents","Iranians","Jammu and Kashmir Liberation Front","Jarnail Khalsa","Karamyit Singh","Kashmiri Militants","Khalistan Commando Force","Khalistan Liberation Force","Kisar Liberation Movement","Liberation Tigers of Tamil Eelam" ,"Maoist Communist Center","Muslim Militants","Muslim Separatists","National Socialist Council of Nagaland","Organization of Arab Fedayeen Cells","Peoples War Group","pro pakistani militants","Revolutionary Organization of Socialist Moslems","Saffron Tigers","Scooter Borne terrorists","Secessionists","Separatists","Sikh Extremists","Tamils","Terrorists","Tribal Separatists","Tripura National Volunteers","Tripura Nationalists","United Liberation Front of Assam","Achik National Volunteer Council","Adivasi National Liberation Army","Akhilesh Singh Gang","Al Nasirin","Al Arifeen","Al Badr","Al Fajr","Al Hamas Mujahideen","All India Anna Dravida Munetra Kazgan Party","All Kamatapur Liberation Force","All Tripura Tiger Force","Al Madina","Al Mansoorian","Al Nasireen Group","Al Shuda Brigade","Al Umar Mujahideen","Bandits","Bhumi Uchched Pratirodh Committee","Black Widows","Bodo Liberation Tigers","Bodo Peoples Front","Citizens Rights Protection Volunteers","Communist Party of India Maoist","Communist Party of India Marxist","Communist Party of India Marxist Leninist","Deccan Mujahideen","Dima Halao Daoga","Guerrillas","Harakat ul Mujahidin","Harkatul Jihad e Islami","Hizbul Mujahideen","Hmar Peoples Convention Democracy","Indian Mujahideen","Islamic Fateh","Islamic Front","Jaish e Mohammad","Jamiat ul Mujahedin","Jharkhand Liberation Tigers","Kamtapur Liberation Organization","Kanglei Yawol Kanna Lup","Kangleipak Communist Party","Karbi Longri National Liberation Front","Karbi Longri North Cachar Liberation Front","Karbi National Volunteers","Karbi Tribe","Kashmir Freedom Force","Kuki Liberation Army","Kuki National Army","Kuki National Front","Kuki Revolutionary Army","Lashkar e Jhangvi","Lashkar e Taiba","Mahaz e Inquilab","Militants","Miscreants","Muslim Rebels","Naga Peoples Council","National Democratic Front of Bodoland","National Liberation Front of Tripura National Peoples Party","Rashtriya Janata Dal","National Socialist Council of Nagaland Isak Muivah","National Socialist Council of Nagaland Khapla","Peoples Committee against Police Atrocities","Peoples Liberation Front of India","Peoples Revolutionary Party of Kangleipak","Peoples United Liberation Front","Porattom","Praveen Dalam","Ranbir Sena","Rashtriya Swayamsevak SanghRebels","Save Kashmir Movement","Students Islamic Movement of India","Tamil Nadu Liberation Army","Tehrik al Mojahedin","Tehrik e Galba Islam","Tritiya Prastuti Committee","United Bengali Liberation Front","United Democratic Terai Liberation Front","United Jihad Council","United Kuki Liberation Front India","United National Liberation Front ","United Peoples Democratic Solidarity ","Vishwa Hindu Parishad ","Achik National Cooperative Army","Achik National Liberation Army","Achik National Volunteer Council B" ,"A chik Songna An pachakgipa Kotok","A chik Tiger Force","Adivasi Cobra Militants of Assam","Adivasi Peoples Army" ,"Al Ummah","Bengali Sangram Mukti Bahini","Bru National Liberation Front","Coordination Committee","Dima Hasao National Army","Garo National Liberation Army","Hill Tiger Force","Hynniewtrep National Liberation Council","Islamic Movement of Kashmir","Jamaat E Islami" ,"Jammu  Kashmir Islamic Front","Jharkhand Bachao Aandolan","Jharkhand Janmukti Parishad","Jharkhand Prastuti Committee" ,"Karbi Peoples Liberation Tigers ","Khasi Students Union","Kuki National Liberation Front","Kuki Tribal Militants","Kuki tribesmen","Manipur Naga Peoples Army","Manipur Nationalist Revolutionary Party","Maoist Communist Party of Manipur","Muslim United Liberation Tigers of Assam","Naga National Council","National Liberation Council of Taniland","National Liberation Force of Bengalis","National Santhali Liberation Army","National Socialist Council of Nagaland Khole Kitovi","New Peoples Army","Pahadi Cheetah","Pattali Makkal Katchi","Peoples Revolutionary Party of Kangleipak Progressive","Rabha National Security Force","Shiv Sena","Telangana Separatists","Terai Janatantrik Party","Tribesmen","United A chik Liberation Army ","United Democratic Liberation Army","United Karbi Liberation Army","United Liberation Front of Barak Valley India","United Revolutionary Front","United Tribal Liberation Army" ,"Volunteers of Innocent People of Nagas ","Yimchunger Liberation Front ","Youths","Zeliangrong United Front","Zomi Revolutionary Arm"]
relatedPhrases = []
for phrase in related:
	#relatedPhrases.append(phrase['phrase'])

#for phrase in relatedPhrases:
	url="http://www.faroo.com/api?q="+phrase+"&start=1&length=10&l=en&src=news&f=json&key=L61Zj@aitGMws0IuAMFIyQ@nJ@A_"
	response = requests.get(url, verify=True)
	if response.status_code == 200:
		data = response.json()
		res = data["results"]
		for nw in res:
			"""extract = c.Extract({"url": nw["url"], "best_image": True})
			entities = c.Entities({"text": extract})
			for type, values in entities['entities'].items():
 				print (type,', '.join(values))"""
			summary = c.Summarize({'url': nw["url"], 'sentences_number': 5})
			articlesum = ''
			for sentence in summary['sentences']:
				articlesum+=sentence
			with open('newsDataGname.txt', 'a') as f:
				f.write(articlesum)
			"""entities = c.Entities({"text": articlesum})
			for type, values in entities['entities'].items():
 				print (type,', '.join(values))
			print("---------------------------------------------------------------------------------------------")
	
	print("---------------------------------------------------------------------------------------------")"""
	
