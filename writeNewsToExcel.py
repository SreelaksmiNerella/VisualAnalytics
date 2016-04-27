path = "latestnews.csv"

import csv
def csv_writer(data, path):

    #Mode can be wb for writing and ab for appending
    
    #Here the first row which are the coloumn names should be added in the 
    #code initially and only once it has to be entered
    

    #For first row put in wb and other entries ab
    #This should run only once
    """with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow("Gname,Attack,Location".split(","))"""
    
    #For new rows only which will run in multiple loops:
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

import json
import requests
from aylienapiclient import textapi

c = textapi.Client("1cd2ba31", "1914eec2b403991cc5c761979ab92115")
#mycount = 1
related = ["Ananda Marga","Japanese Red Army","Maoists","Meitei extremists","Mizo National Front","Muslims","Naga People","Naxalites","Palestinians","People's Liberation Army","Akali Dal Party","All India Sikh Students Federation","Allahs Tigers","Anti Immigrant Activists","Anti Socials","Babbar Khalsa International","Bhinderanwale Tiger Force of Khalistan","Bodo Militants","Communist Party of India","Dishmish Regiment","Dissident","Extremists","Fedayeen Khalq","Gunmen","Gurkha National Liberation Front Insurgents","Iranians","Jammu and Kashmir Liberation Front","Jarnail Khalsa","Karamyit Singh","Kashmiri Militants","Khalistan Commando Force","Khalistan Liberation Force","Kisar Liberation Movement","Liberation Tigers of Tamil Eelam" ,"Maoist Communist Center","Muslim Militants","Muslim Separatists","National Socialist Council of Nagaland","Organization of Arab Fedayeen Cells","Peoples War Group","pro pakistani militants","Revolutionary Organization of Socialist Moslems","Saffron Tigers","Scooter Borne terrorists","Secessionists","Separatists","Sikh Extremists","Tamils","Terrorists","Tribal Separatists","Tripura National Volunteers","Tripura Nationalists","United Liberation Front of Assam","Achik National Volunteer Council","Adivasi National Liberation Army","Akhilesh Singh Gang","Al Nasirin","Al Arifeen","Al Badr","Al Fajr","Al Hamas Mujahideen","All India Anna Dravida Munetra Kazgan Party","All Kamatapur Liberation Force","All Tripura Tiger Force","Al Madina","Al Mansoorian","Al Nasireen Group","Al Shuda Brigade","Al Umar Mujahideen","Bandits","Bhumi Uchched Pratirodh Committee","Black Widows","Bodo Liberation Tigers","Bodo Peoples Front","Citizens Rights Protection Volunteers","Communist Party of India Maoist","Communist Party of India Marxist","Communist Party of India Marxist Leninist","Deccan Mujahideen","Dima Halao Daoga","Guerrillas","Harakat ul Mujahidin","Harkatul Jihad e Islami","Hizbul Mujahideen","Hmar Peoples Convention Democracy","Indian Mujahideen","Islamic Fateh","Islamic Front","Jaish e Mohammad","Jamiat ul Mujahedin","Jharkhand Liberation Tigers","Kamtapur Liberation Organization","Kanglei Yawol Kanna Lup","Kangleipak Communist Party","Karbi Longri National Liberation Front","Karbi Longri North Cachar Liberation Front","Karbi National Volunteers","Karbi Tribe","Kashmir Freedom Force","Kuki Liberation Army","Kuki National Army","Kuki National Front","Kuki Revolutionary Army","Lashkar e Jhangvi","Lashkar e Taiba","Mahaz e Inquilab","Militants","Miscreants","Muslim Rebels","Naga Peoples Council","National Democratic Front of Bodoland","National Liberation Front of Tripura National Peoples Party","Rashtriya Janata Dal","National Socialist Council of Nagaland Isak Muivah","National Socialist Council of Nagaland Khapla","Peoples Committee against Police Atrocities","Peoples Liberation Front of India","Peoples Revolutionary Party of Kangleipak","Peoples United Liberation Front","Porattom","Praveen Dalam","Ranbir Sena","Rashtriya Swayamsevak SanghRebels","Save Kashmir Movement","Students Islamic Movement of India","Tamil Nadu Liberation Army","Tehrik al Mojahedin","Tehrik e Galba Islam","Tritiya Prastuti Committee","United Bengali Liberation Front","United Democratic Terai Liberation Front","United Jihad Council","United Kuki Liberation Front India","United National Liberation Front ","United Peoples Democratic Solidarity ","Vishwa Hindu Parishad ","Achik National Cooperative Army","Achik National Liberation Army","Achik National Volunteer Council B" ,"A chik Songna An pachakgipa Kotok","A chik Tiger Force","Adivasi Cobra Militants of Assam","Adivasi Peoples Army" ,"Al Ummah","Bengali Sangram Mukti Bahini","Bru National Liberation Front","Coordination Committee","Dima Hasao National Army","Garo National Liberation Army","Hill Tiger Force","Hynniewtrep National Liberation Council","Islamic Movement of Kashmir","Jamaat E Islami" ,"Jammu  Kashmir Islamic Front","Jharkhand Bachao Aandolan","Jharkhand Janmukti Parishad","Jharkhand Prastuti Committee" ,"Karbi Peoples Liberation Tigers ","Khasi Students Union","Kuki National Liberation Front","Kuki Tribal Militants","Kuki tribesmen","Manipur Naga Peoples Army","Manipur Nationalist Revolutionary Party","Maoist Communist Party of Manipur","Muslim United Liberation Tigers of Assam","Naga National Council","National Liberation Council of Taniland","National Liberation Force of Bengalis","National Santhali Liberation Army","National Socialist Council of Nagaland Khole Kitovi","New Peoples Army","Pahadi Cheetah","Pattali Makkal Katchi","Peoples Revolutionary Party of Kangleipak Progressive","Rabha National Security Force","Shiv Sena","Telangana Separatists","Terai Janatantrik Party","Tribesmen","United A chik Liberation Army ","United Democratic Liberation Army","United Karbi Liberation Army","United Liberation Front of Barak Valley India","United Revolutionary Front","United Tribal Liberation Army" ,"Volunteers of Innocent People of Nagas ","Yimchunger Liberation Front ","Youths","Zeliangrong United Front","Zomi Revolutionary Arm"]

for phrase in related:
    #mycount = mycount-1

    #relatedPhrases.append(phrase['phrase'])

#for phrase in relatedPhrases:
    url="http://www.faroo.com/api?q="+phrase+"&start=1&length=10&l=en&src=news&f=json&key=L61Zj@aitGMws0IuAMFIyQ@nJ@A_"
    response = requests.get(url, verify=True)
    if response.status_code == 200:
        data1 = response.json()
        res = data1["results"]
        for nw in res:
            extract = c.Extract({"url": nw["url"], "best_image": True})
            entities = c.Entities({"text": extract})
            #for type, values in entities['entities'].items():
                #print (type,', '.join(values))
            summary = c.Summarize({'url': nw["url"], 'sentences_number': 5})
            articlesum = ''
            for sentence in summary['sentences']:
                articlesum+=sentence
                #print(articlesum)
            with open('newsDataGname.txt', 'w') as f:
                f.write(articlesum)

            data=[]
            search1 = ["ananda\smarga","japanese\sred\sarmy","maoists","meitei\sextremists","mizo\snational\sfront","muslims","naga\speople","naxalites","palestinians","people's\sliberation\sarmy","akali\saal\sparty","all\sindia\ssikh\sstudents\sfederation","allahs\stigers","anti\simmigrant\sactivists","anti\ssocials","babbar\skhalsa\sinternational","bhinderanwale\stiger\sforce\sof\skhalistan","bodo\smilitants","communist\sparty\sof\sindia","dishmish\sregiment","dissident","extremists","fedayeen\skhalq","gunmen","gurkha\snational\sliberation\sfront\s","insurgents","iranians","jammu\sand\skashmir\sliberation\sfront","jarnail\skhalsa","karamyit\ssingh","kashmiri\smilitants","khalistan\scommando\sforce","khalistan\sliberation\sforce","kisar\sliberation\smovement","liberation\stigers\sof\stamil\seelam","maoist\scommunist\scenter","muslim\smilitants","muslim\sseparatists","national\ssocialist\scouncil\sof\snagaland","organization\sof\sarab\sfedayeen\scells","peoples\swar\sgroup","pro\spakistani\smilitants","revolutionary\sorganization\sof\ssocialist\smoslems","saffron\stigers","scooter\sborne\sterrorists","secessionists","separatists","sikh\sextremists","tamils","terrorists","tribal\sseparatists","tripura\snational\svolunteers","tripura\snationalists","united\sliberation\sfront\sof\sassam","achik\snational\svolunteer\scouncil","adivasi\snational\sliberation\sarmy","akhilesh\ssingh\sgang","al\snasirin","al\sarifeen","al\sbadr","al\sfajr","al\shamas\smujahideen","all\sindia\sanna\sdravida\smunetra\skazgan\sparty","all\skamatapur\sliberation\sforce","all\stripura\stiger\sforce","al\smadina","al\smansoorian","al\snasireen\sgroup","al\sshuda\sbrigade","al\sumar\smujahideen","bandits","bhumi\suchched\spratirodh\scommittee","black\swidows","bodo\sliberation\stigers","bodo\speoples\sfront","citizens\srights\sprotection\svolunteers","communist\sparty\sof\sindia\smaoist","communist\sparty\sof\sindia\smarxist","communist\sparty\sof\sindia\smarxist\sleninist","deccan\smujahideen","dima\shalao\sdaoga","guerrillas","harakat\sul\smujahidin","harkatul\sjihad\se\sislami","hizbul\smujahideen","hmar\speoples\sconvention\sdemocracy","indian\smujahideen","islamic\sfateh","islamic\sfront","jaish\se\smohammad","jamiat\sul\smujahedin","jharkhand\sliberation\stigers","Hamtapur\sliberation\sorganization","kanglei\syawol\skanna\slup","kangleipak\scommunist\sparty","karbi\slongri\snational\sliberation\sfront","karbi\slongri\snorth\scachar\sliberation\sfront","karbi\snational\svolunteers","karbi\stribe","kashmir\sfreedom\sforce","kuki\sliberation\sarmy","kuki\snational\sarmy","kuki\snational\sfront","kuki\srevolutionary\sarmy","lashkar\se\sjhangvi","lashkar\se\staiba","mahaz\se\sinquilab","militants","miscreants","muslim\srebels","naga\speoples\scouncil","national\sdemocratic\sfront\sof\sbodoland","national\sliberation\sfront\sof\stripura\snational\speoples\sparty","rashtriya\sjanata\sdal","national\ssocialist\scouncil\sof\snagaland\sisak\smuivah","national\ssocialist\scouncil\sof\snagaland\skhapla","peoples\scommittee\sagainst\spolice\satrocities","peoples\sliberation\sfront\sof\sindia","peoples\srevolutionary\sparty\sof\skangleipak","peoples\sunited\sliberation\sfront","porattom","praveen\sdalam","ranbir\ssena","rashtriya\sswayamsevak\ssanghrebels","save\skashmir\smovement","students\sislamic\smovement\sof\sindia","tamil\snadu\sliberation\sarmy","tehrik\sal\smojahedin","tehrik\se\sgalba\sislam","tritiya\sprastuti\scommittee","united\sbengali\sliberation\sfront","united\sdemocratic\sterai\sliberation\sfront","united\sjihad\scouncil","united\skuki\sliberation\sfront\sindia","united\snational\sliberation\sfront\s","united\speoples\sdemocratic\ssolidarity\s","vishwa\shindu\sparishad\s","achik\snational\scooperative\sarmy","achik\snational\sliberation\sarmy","achik\snational\svolunteer\scouncil\sb","a\schik\ssongna\san\spachakgipa\skotok","a\schik\stiger\sforce","adivasi\scobra\smilitants\sof\sassam","adivasi\speoples\sarmy","al\summah","bengali\ssangram\smukti\sbahini","bru\snational\sliberation\sfront","coordination\scommittee","dima\shasao\snational\sarmy","garo\snational\sliberation\sarmy","hill\stiger\sforce","hynniewtrep\snational\sliberation\scouncil","islamic\smovement\sof\skashmir","jamaat\se\sislami","jammu\s\skashmir\sislamic\sfront","jharkhand\sbachao\saandolan","jharkhand\sjanmukti\sparishad","jharkhand\sprastuti\scommittee","karbi\speoples\sliberation\stigers\s","khasi\sstudents\sunion","kuki\snational\sliberation\sfront","kuki\stribal\smilitants","kuki\stribesmen","manipur\snaga\speoples\sarmy","manipur\snationalist\srevolutionary\sparty","maoist\scommunist\sparty\sof\smanipur","muslim\sunited\sliberation\stigers\sof\sassam","naga\snational\scouncil","national\sliberation\scouncil\sof\staniland","national\sliberation\sforce\sof\sbengalis","national\ssanthali\sliberation\sarmy","national\ssocialist\scouncil\sof\snagaland\skhole\skitovi","new\speoples\sarmy","pahadi\scheetah","pattali\smakkal\skatchi","peoples\srevolutionary\sparty\sof\skangleipak\sprogressive","rabha\snational\ssecurity\sforce","shiv\ssena","telangana\sseparatists","terai\sjanatantrik\sparty","tribesmen","united\sa\schik\sliberation\sarmy\s","united\sdemocratic\sliberation\sarmy","united\skarbi\sliberation\sarmy","united\sliberation\sfront\sof\sbarak\svalley\sindia","united\srevolutionary\sfront","united\stribal\sliberation\sarmy","volunteers\sof\sinnocent\speople\sof\snagas\s","yimchunger\sliberation\sfront\s","youths","zeliangrong\sunited\sfront","zomi\srevolutionary\sarm"]
            search2 = ["armed\sassault","assassination","bombing","infrastructure\sattack","hijacking","kidnapping","unarmed\sassault","barricade\sIncident"]
            search3 = ["Amrui","Dogri\sPora","Dhalbhumgarh","Dhekiajuli","Parsurampara","Kambiron","Bijapur\sdistrict","Pathgatha","Jeypore","Siju","Rongram","Chulabhat","Dharambandha","Duarmara","Mohunpur","Gajol","Gadtoli","Tinsukia","Kirwala","Dhurli","Gandiwani","Imphal","Bastar\sdistrict","Chintagufa","Shikaripara","Rongara","Khantlang","Rajgarh","Gelmol","Guwahati","Sukma\sdistrict","Bishenpur\sdistrict","Naid\sKhai","Nowpora","Chatra","Rai","Langol\sGames","Arnia","Maharabi\slamkhai","Lakhimpur","Bordumsa","Senapati\sdistrict","Poonch\sdistrict","Srinagar","Thoubal\sdistrict","Moirang","Shopian","Dantewada\sdistrict","Bollonggre\sApal","Rajouri\sdistrict","Shopian\sdistrict","New\sDelhi","Bhagalpur\sdistrict","Labdanguri","Parganas\sdistrict","Pahoo","East\sGaro\sHills\sdistrict","Roro","Rongrakgre","Tral","Mohara","Nakkapalli","Dambuk\sAga","Gaya\sdistrict","Roorkee","Diphu","Chargi","Gangalur","Phaikon","Gulmarg","Rajdhanwar","Unknown","Anantnag","Sopore","Siliguri\sdistrict","Sarkeguda","Lohardaga\sdistrict","Pirtand","Latehar\sdistrict","Lilong","Amrapara","Bomia","Moreh","Bongaigaon\sdistrict","Suangphuh","Hiangtam","Patgaon","Gossaigaon","Sonarpur","Ishuapur","Bongaigaon","Mukkali","Chandra\sNagar","Vellamunda","Phulbari","Sonitpur\sdistrict","Pakhiriguri","Shantipur\sUltapani","Lambari","Mariani","Itkhori","Bijni","Bengaluru","Tamenglong","Pega","Umrangso","Satyanarayanapuram","Chandel\sdistrict"]
            count1 = dict.fromkeys(search1, 0)

            import re

            with open('newsDataGname.txt', 'r') as searchfile:
                for line in searchfile:
                    for word1 in search1:
                        if re.search( word1, line, re.M|re.I):
                            count1[word1] += 1

            count2 = dict.fromkeys(search2, 0)
            with open('newsDataGname.txt', 'r') as searchfile:
                for line in searchfile:
                    for word2 in search2:
                        if re.search( word2, line, re.M|re.I):
                            count2[word2] += 1

            count3 = dict.fromkeys(search3, 0)
            with open('newsDataGname.txt', 'r') as searchfile:
                for line in searchfile:
                    for word3 in search3:
                        if re.search( word3, line, re.M|re.I):
                            count3[word3] += 1

            flag=0
            flag1=0

            for key1,val1 in count1.items():
                if(val1>0):
                    s=""
                    s=s+key1
                    for key2,val2 in count2.items():
                        if(val2>0):
                            s=s+","+key2
                            flag=1
                            for key3,val3 in count3.items():
                                if(val3>0):
                                    flag1=1
                                    s=s+","+key3
                                    data.append(s.split(","))
                                s=key1+","+key2
                            if(flag1==0):
                                s+=",Unknown"
                                data.append(s.split(","))
                            s=key1
                    if(flag==0):
                        for key3,val3 in count3.items():
                            if(val3>0):
                                s=s+",Unknown,"+key3
                                data.append(s.split(","))
                                s=key1
            print(data)
            csv_writer(data, path)


exit()