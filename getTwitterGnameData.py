from aylienapiclient import textapi
c = textapi.Client("331741bd", "b5b0b3079d2220b1dfd3eeed32f8adab")

related = ["Ananda Marga","Japanese Red Army","Maoists","Meitei extremists","Mizo National Front","Muslims","Naga People","Naxalites","Palestinians","People's Liberation Army","Akali Dal Party","All India Sikh Students Federation","Allahs Tigers","Anti Immigrant Activists","Anti Socials","Babbar Khalsa International","Bhinderanwale Tiger Force of Khalistan","Bodo Militants","Communist Party of India","Dishmish Regiment","Dissident","Extremists","Fedayeen Khalq","Gunmen","Gurkha National Liberation Front Insurgents","Iranians","Jammu and Kashmir Liberation Front","Jarnail Khalsa","Karamyit Singh","Kashmiri Militants","Khalistan Commando Force","Khalistan Liberation Force","Kisar Liberation Movement","Liberation Tigers of Tamil Eelam" ,"Maoist Communist Center","Muslim Militants","Muslim Separatists","National Socialist Council of Nagaland","Organization of Arab Fedayeen Cells","Peoples War Group","pro pakistani militants","Revolutionary Organization of Socialist Moslems","Saffron Tigers","Scooter Borne terrorists","Secessionists","Separatists","Sikh Extremists","Tamils","Terrorists","Tribal Separatists","Tripura National Volunteers","Tripura Nationalists","United Liberation Front of Assam","Achik National Volunteer Council","Adivasi National Liberation Army","Akhilesh Singh Gang","Al Nasirin","Al Arifeen","Al Badr","Al Fajr","Al Hamas Mujahideen","All India Anna Dravida Munetra Kazgan Party","All Kamatapur Liberation Force","All Tripura Tiger Force","Al Madina","Al Mansoorian","Al Nasireen Group","Al Shuda Brigade","Al Umar Mujahideen","Bandits","Bhumi Uchched Pratirodh Committee","Black Widows","Bodo Liberation Tigers","Bodo Peoples Front","Citizens Rights Protection Volunteers","Communist Party of India Maoist","Communist Party of India Marxist","Communist Party of India Marxist Leninist","Deccan Mujahideen","Dima Halao Daoga","Guerrillas","Harakat ul Mujahidin","Harkatul Jihad e Islami","Hizbul Mujahideen","Hmar Peoples Convention Democracy","Indian Mujahideen","Islamic Fateh","Islamic Front","Jaish e Mohammad","Jamiat ul Mujahedin","Jharkhand Liberation Tigers","Kamtapur Liberation Organization","Kanglei Yawol Kanna Lup","Kangleipak Communist Party","Karbi Longri National Liberation Front","Karbi Longri North Cachar Liberation Front","Karbi National Volunteers","Karbi Tribe","Kashmir Freedom Force","Kuki Liberation Army","Kuki National Army","Kuki National Front","Kuki Revolutionary Army","Lashkar e Jhangvi","Lashkar e Taiba","Mahaz e Inquilab","Militants","Miscreants","Muslim Rebels","Naga Peoples Council","National Democratic Front of Bodoland","National Liberation Front of Tripura National Peoples Party","Rashtriya Janata Dal","National Socialist Council of Nagaland Isak Muivah","National Socialist Council of Nagaland Khapla","Peoples Committee against Police Atrocities","Peoples Liberation Front of India","Peoples Revolutionary Party of Kangleipak","Peoples United Liberation Front","Porattom","Praveen Dalam","Ranbir Sena","Rashtriya Swayamsevak SanghRebels","Save Kashmir Movement","Students Islamic Movement of India","Tamil Nadu Liberation Army","Tehrik al Mojahedin","Tehrik e Galba Islam","Tritiya Prastuti Committee","United Bengali Liberation Front","United Democratic Terai Liberation Front","United Jihad Council","United Kuki Liberation Front India","United National Liberation Front ","United Peoples Democratic Solidarity ","Vishwa Hindu Parishad ","Achik National Cooperative Army","Achik National Liberation Army","Achik National Volunteer Council B" ,"A chik Songna An pachakgipa Kotok","A chik Tiger Force","Adivasi Cobra Militants of Assam","Adivasi Peoples Army" ,"Al Ummah","Bengali Sangram Mukti Bahini","Bru National Liberation Front","Coordination Committee","Dima Hasao National Army","Garo National Liberation Army","Hill Tiger Force","Hynniewtrep National Liberation Council","Islamic Movement of Kashmir","Jamaat E Islami" ,"Jammu  Kashmir Islamic Front","Jharkhand Bachao Aandolan","Jharkhand Janmukti Parishad","Jharkhand Prastuti Committee" ,"Karbi Peoples Liberation Tigers ","Khasi Students Union","Kuki National Liberation Front","Kuki Tribal Militants","Kuki tribesmen","Manipur Naga Peoples Army","Manipur Nationalist Revolutionary Party","Maoist Communist Party of Manipur","Muslim United Liberation Tigers of Assam","Naga National Council","National Liberation Council of Taniland","National Liberation Force of Bengalis","National Santhali Liberation Army","National Socialist Council of Nagaland Khole Kitovi","New Peoples Army","Pahadi Cheetah","Pattali Makkal Katchi","Peoples Revolutionary Party of Kangleipak Progressive","Rabha National Security Force","Shiv Sena","Telangana Separatists","Terai Janatantrik Party","Tribesmen","United A chik Liberation Army ","United Democratic Liberation Army","United Karbi Liberation Army","United Liberation Front of Barak Valley India","United Revolutionary Front","United Tribal Liberation Army" ,"Volunteers of Innocent People of Nagas ","Yimchunger Liberation Front ","Youths","Zeliangrong United Front","Zomi Revolutionary Arm"]
"""relatedPhrases = []
for phrase in related['related']:
	relatedPhrases.append(phrase['phrase'])
#print(relatedPhrases)"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = '1frw6GnZHIzkrAz6Nk8jRo2Y1'
consumer_secret = '9pkhy6Ow0m22xRMUjIjJYfd0lt4insoQTue6x3NWLqjn4rDm4B'
access_token = '4780814894-0AX6wOOG7C8FGM7FGA70tQ49rMYve73cTWUuNDc'
access_secret = 'ERUUrdWj90uOkaHgs0nsFDua5LKypfeh447YsB5cUYWOC'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweetDataGname.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=related,async=True,languages=["en"])