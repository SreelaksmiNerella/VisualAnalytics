
search = ["ananda\smarga","japanese\sred\sarmy","maoists","meitei\sextremists","mizo\snational\sfront","muslims","naga people","naxalites","palestinians","people's liberation army","akali aal party","all india sikh students federation","allahs tigers","anti immigrant activists","anti socials","babbar khalsa international","bhinderanwale tiger force of khalistan","bodo militants","communist\arty of india","dishmish regiment","dissident","extremists","fedayeen khalq","gunmen","gurkha national liberation front ","insurgents","iranians","jammu and kashmir liberation front","jarnail khalsa","karamyit singh","kashmiri militants","khalistan commando force","khalistan liberation force","kisar liberation movement","liberation tigers of tamil eelam" ,"maoist communist center","muslim militants","muslim separatists","national socialist council of nagaland","organization of arab fedayeen cells","peoples war group","pro pakistani militants","revolutionary organization of socialist moslems","saffron tigers","scooter borne terrorists","secessionists","separatists","sikh extremists","tamils","terrorists","tribal separatists","tripura national volunteers","tripura nationalists","united liberation front of assam","achik national volunteer council","adivasi national liberation army","akhilesh singh gang","al nasirin","al arifeen","al badr","al fajr","al hamas mujahideen","all india anna dravida munetra kazgan party","all kamatapur liberation force","all tripura tiger force","al madina","al mansoorian","al nasireen group","al shuda brigade","al umar mujahideen","bandits","bhumi uchched pratirodh committee","black widows","bodo liberation tigers","bodo peoples front","citizens rights protection volunteers","communist party of india maoist","communist party of india marxist","communist party of india marxist leninist","deccan mujahideen","dima halao daoga","guerrillas","harakat ul mujahidin","harkatul jihad e islami","hizbul mujahideen","hmar peoples convention democracy","indian mujahideen","islamic fateh","islamic front","jaish e mohammad","jamiat ul mujahedin","jharkhand liberation tigers","Hamtapur liberation organization","kanglei yawol kanna lup","kangleipak communist party","karbi longri national liberation front","karbi longri north cachar liberation front","karbi national volunteers","karbi tribe","kashmir freedom force","kuki liberation army","kuki national army","kuki national front","kuki revolutionary army","lashkar e jhangvi","lashkar e taiba","mahaz e inquilab","militants","miscreants","muslim rebels","naga peoples council","national democratic front of bodoland","national liberation front of tripura national peoples party","rashtriya janata dal","national socialist council of nagaland isak muivah","national socialist council of nagaland khapla","peoples committee against police atrocities","peoples liberation front of india","peoples revolutionary party of kangleipak","peoples united liberation front","porattom","praveen dalam","ranbir sena","rashtriya swayamsevak sanghrebels","save kashmir movement","students islamic movement of india","tamil nadu liberation army","tehrik al mojahedin","tehrik e galba islam","tritiya prastuti committee","united bengali liberation front","united democratic terai liberation front","united jihad council","united kuki liberation front india","united national liberation front ","united peoples democratic solidarity ","vishwa hindu parishad ","achik national cooperative army","achik national liberation army","achik national volunteer council b" ,"a chik songna an pachakgipa kotok","a chik tiger force","adivasi cobra militants of assam","adivasi peoples army" ,"al ummah","bengali sangram mukti bahini","bru national liberation front","coordination committee","dima hasao national army","garo national liberation army","hill tiger force","hynniewtrep national liberation council","islamic movement of kashmir","jamaat e islami" ,"jammu  kashmir islamic front","jharkhand bachao aandolan","jharkhand janmukti parishad","jharkhand prastuti committee" ,"karbi peoples liberation tigers ","khasi students union","kuki national liberation front","kuki tribal militants","kuki tribesmen","manipur naga peoples army","manipur nationalist revolutionary party","maoist communist party of manipur","muslim united liberation tigers of assam","naga national council","national liberation council of taniland","national liberation force of bengalis","national santhali liberation army","national socialist council of nagaland khole kitovi","new peoples army","pahadi cheetah","pattali makkal katchi","peoples revolutionary party of kangleipak progressive","rabha national security force","shiv sena","telangana separatists","terai janatantrik party","tribesmen","united a chik liberation army ","united democratic liberation army","united karbi liberation army","united liberation front of barak valley india","united revolutionary front","united tribal liberation army" ,"volunteers of innocent people of nagas ","yimchunger liberation front ","youths","zeliangrong united front","zomi revolutionary arm"]
"""
count = dict.fromkeys(search, 0)

with open("newsDataGname.txt", 'r') as f:
    for line in f:
        for word in line.lower().split():
            if word in count:
                count[word] += 1
"""
#print(count)
#search = ["ananda\smarga","japanese\sred\sarmy","maoists","meitei\sextremists","mizo\snational\sfront","muslims","naga\speople","naxalites","palestinians","people's\sliberation\sarmy","akali\saal\sparty","all\sindia\ssikh\sstudents\sfederation","allahs\stigers","anti\simmigrant\sactivists","anti\ssocials","babbar\skhalsa\sinternational","bhinderanwale\stiger\sforce\sof\skhalistan","bodo\smilitants","communist\sparty\sof\sindia","dishmish\sregiment","dissident","extremists","fedayeen\skhalq","gunmen","gurkha\snational\sliberation\sfront ","insurgents","iranians","jammu\sand\skashmir\sliberation\sfront","jarnail\skhalsa","karamyit\ssingh","kashmiri\smilitants","khalistan\scommando\sforce","khalistan\sliberation\sforce","kisar\sliberation\smovement","liberation\stigers\sof\stamil\seelam" ,"maoist\scommunist\scenter","muslim\smilitants","muslim\sseparatists","national\ssocialist\scouncil\sof\snagaland","organization\sof\sarab\sfedayeen\scells","peoples\swar\sgroup","pro\spakistani\smilitants","revolutionary\sorganization\sof\ssocialist\smoslems","saffron\stigers","scooter\sborne\sterrorists","secessionists","separatists","sikh\sextremists","tamils","terrorists","tribal\sseparatists","tripura\snational\svolunteers","tripura\snationalists","united\sliberation\sfront\sof\sassam","achik\snational\svolunteer\scouncil","adivasi\snational liberation army","akhilesh singh gang","al nasirin","al arifeen","al badr","al fajr","al hamas mujahideen","all india anna dravida munetra kazgan party","all kamatapur liberation force","all tripura tiger force","al madina","al mansoorian","al nasireen group","al shuda brigade","al umar mujahideen","bandits","bhumi uchched pratirodh committee","black widows","bodo liberation tigers","bodo peoples front","citizens rights protection volunteers","communist party of india maoist","communist party of india marxist","communist party of india marxist leninist","deccan mujahideen","dima halao daoga","guerrillas","harakat ul mujahidin","harkatul jihad e islami","hizbul mujahideen","hmar peoples convention democracy","indian mujahideen","islamic fateh","islamic front","jaish e mohammad","jamiat ul mujahedin","jharkhand liberation tigers","Hamtapur liberation organization","kanglei yawol kanna lup","kangleipak communist party","karbi longri national liberation front","karbi longri north cachar liberation front","karbi national volunteers","karbi tribe","kashmir freedom force","kuki liberation army","kuki national army","kuki national front","kuki revolutionary army","lashkar e jhangvi","lashkar e taiba","mahaz e inquilab","militants","miscreants","muslim rebels","naga peoples council","national democratic front of bodoland","national liberation front of tripura national peoples party","rashtriya janata dal","national socialist council of nagaland isak muivah","national socialist council of nagaland khapla","peoples committee against police atrocities","peoples liberation front of india","peoples revolutionary party of kangleipak","peoples united liberation front","porattom","praveen dalam","ranbir sena","rashtriya swayamsevak sanghrebels","save kashmir movement","students islamic movement of india","tamil nadu liberation army","tehrik al mojahedin","tehrik e galba islam","tritiya prastuti committee","united bengali liberation front","united democratic terai liberation front","united jihad council","united kuki liberation front india","united national liberation front ","united peoples democratic solidarity ","vishwa hindu parishad ","achik national cooperative army","achik national liberation army","achik national volunteer council b" ,"a chik songna an pachakgipa kotok","a chik tiger force","adivasi cobra militants of assam","adivasi peoples army" ,"al ummah","bengali sangram mukti bahini","bru national liberation front","coordination committee","dima hasao national army","garo national liberation army","hill tiger force","hynniewtrep national liberation council","islamic movement of kashmir","jamaat e islami" ,"jammu  kashmir islamic front","jharkhand bachao aandolan","jharkhand janmukti parishad","jharkhand prastuti committee" ,"karbi peoples liberation tigers ","khasi students union","kuki national liberation front","kuki tribal militants","kuki tribesmen","manipur naga peoples army","manipur nationalist revolutionary party","maoist communist party of manipur","muslim united liberation tigers of assam","naga national council","national liberation council of taniland","national liberation force of bengalis","national santhali liberation army","national socialist council of nagaland khole kitovi","new peoples army","pahadi cheetah","pattali makkal katchi","peoples revolutionary party of kangleipak progressive","rabha national security force","shiv sena","telangana separatists","terai janatantrik party","tribesmen","united a chik liberation army ","united democratic liberation army","united karbi liberation army","united liberation front of barak valley india","united revolutionary front","united tribal liberation army" ,"volunteers of innocent people of nagas ","yimchunger liberation front ","youths","zeliangrong united front","zomi revolutionary arm"]
path = "todaysdata.csv"
data=[]
import csv
def csv_writer(data, path):

    #Mode can be wb for writing and ab for appending
    
    #Here the first row which are the coloumn names should be added in the 
    #code initially and only once it has to be entered
    

    #For first row put in wb and other entries ab
    #This should run only once
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow("Gname,Attack,Location".split(","))
    
    #For new rows only which will run in multiple loops:
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)




search1 = ["ananda\smarga","japanese\sred\sarmy","maoists","meitei\sextremists","mizo\snational\sfront","muslims","naga\speople","naxalites","palestinians","people's\sliberation\sarmy","akali\saal\sparty","all\sindia\ssikh\sstudents\sfederation","allahs\stigers","anti\simmigrant\sactivists","anti\ssocials","babbar\skhalsa\sinternational","bhinderanwale\stiger\sforce\sof\skhalistan","bodo\smilitants","communist\sparty\sof\sindia","dishmish\sregiment","dissident","extremists","fedayeen\skhalq","gunmen","gurkha\snational\sliberation\sfront\s","insurgents","iranians","jammu\sand\skashmir\sliberation\sfront","jarnail\skhalsa","karamyit\ssingh","kashmiri\smilitants","khalistan\scommando\sforce","khalistan\sliberation\sforce","kisar\sliberation\smovement","liberation\stigers\sof\stamil\seelam","maoist\scommunist\scenter","muslim\smilitants","muslim\sseparatists","national\ssocialist\scouncil\sof\snagaland","organization\sof\sarab\sfedayeen\scells","peoples\swar\sgroup","pro\spakistani\smilitants","revolutionary\sorganization\sof\ssocialist\smoslems","saffron\stigers","scooter\sborne\sterrorists","secessionists","separatists","sikh\sextremists","tamils","terrorists","tribal\sseparatists","tripura\snational\svolunteers","tripura\snationalists","united\sliberation\sfront\sof\sassam","achik\snational\svolunteer\scouncil","adivasi\snational\sliberation\sarmy","akhilesh\ssingh\sgang","al\snasirin","al\sarifeen","al\sbadr","al\sfajr","al\shamas\smujahideen","all\sindia\sanna\sdravida\smunetra\skazgan\sparty","all\skamatapur\sliberation\sforce","all\stripura\stiger\sforce","al\smadina","al\smansoorian","al\snasireen\sgroup","al\sshuda\sbrigade","al\sumar\smujahideen","bandits","bhumi\suchched\spratirodh\scommittee","black\swidows","bodo\sliberation\stigers","bodo\speoples\sfront","citizens\srights\sprotection\svolunteers","communist\sparty\sof\sindia\smaoist","communist\sparty\sof\sindia\smarxist","communist\sparty\sof\sindia\smarxist\sleninist","deccan\smujahideen","dima\shalao\sdaoga","guerrillas","harakat\sul\smujahidin","harkatul\sjihad\se\sislami","hizbul\smujahideen","hmar\speoples\sconvention\sdemocracy","indian\smujahideen","islamic\sfateh","islamic\sfront","jaish\se\smohammad","jamiat\sul\smujahedin","jharkhand\sliberation\stigers","Hamtapur\sliberation\sorganization","kanglei\syawol\skanna\slup","kangleipak\scommunist\sparty","karbi\slongri\snational\sliberation\sfront","karbi\slongri\snorth\scachar\sliberation\sfront","karbi\snational\svolunteers","karbi\stribe","kashmir\sfreedom\sforce","kuki\sliberation\sarmy","kuki\snational\sarmy","kuki\snational\sfront","kuki\srevolutionary\sarmy","lashkar\se\sjhangvi","lashkar\se\staiba","mahaz\se\sinquilab","militants","miscreants","muslim\srebels","naga\speoples\scouncil","national\sdemocratic\sfront\sof\sbodoland","national\sliberation\sfront\sof\stripura\snational\speoples\sparty","rashtriya\sjanata\sdal","national\ssocialist\scouncil\sof\snagaland\sisak\smuivah","national\ssocialist\scouncil\sof\snagaland\skhapla","peoples\scommittee\sagainst\spolice\satrocities","peoples\sliberation\sfront\sof\sindia","peoples\srevolutionary\sparty\sof\skangleipak","peoples\sunited\sliberation\sfront","porattom","praveen\sdalam","ranbir\ssena","rashtriya\sswayamsevak\ssanghrebels","save\skashmir\smovement","students\sislamic\smovement\sof\sindia","tamil\snadu\sliberation\sarmy","tehrik\sal\smojahedin","tehrik\se\sgalba\sislam","tritiya\sprastuti\scommittee","united\sbengali\sliberation\sfront","united\sdemocratic\sterai\sliberation\sfront","united\sjihad\scouncil","united\skuki\sliberation\sfront\sindia","united\snational\sliberation\sfront\s","united\speoples\sdemocratic\ssolidarity\s","vishwa\shindu\sparishad\s","achik\snational\scooperative\sarmy","achik\snational\sliberation\sarmy","achik\snational\svolunteer\scouncil\sb","a\schik\ssongna\san\spachakgipa\skotok","a\schik\stiger\sforce","adivasi\scobra\smilitants\sof\sassam","adivasi\speoples\sarmy","al\summah","bengali\ssangram\smukti\sbahini","bru\snational\sliberation\sfront","coordination\scommittee","dima\shasao\snational\sarmy","garo\snational\sliberation\sarmy","hill\stiger\sforce","hynniewtrep\snational\sliberation\scouncil","islamic\smovement\sof\skashmir","jamaat\se\sislami","jammu\s\skashmir\sislamic\sfront","jharkhand\sbachao\saandolan","jharkhand\sjanmukti\sparishad","jharkhand\sprastuti\scommittee","karbi\speoples\sliberation\stigers\s","khasi\sstudents\sunion","kuki\snational\sliberation\sfront","kuki\stribal\smilitants","kuki\stribesmen","manipur\snaga\speoples\sarmy","manipur\snationalist\srevolutionary\sparty","maoist\scommunist\sparty\sof\smanipur","muslim\sunited\sliberation\stigers\sof\sassam","naga\snational\scouncil","national\sliberation\scouncil\sof\staniland","national\sliberation\sforce\sof\sbengalis","national\ssanthali\sliberation\sarmy","national\ssocialist\scouncil\sof\snagaland\skhole\skitovi","new\speoples\sarmy","pahadi\scheetah","pattali\smakkal\skatchi","peoples\srevolutionary\sparty\sof\skangleipak\sprogressive","rabha\snational\ssecurity\sforce","shiv\ssena","telangana\sseparatists","terai\sjanatantrik\sparty","tribesmen","united\sa\schik\sliberation\sarmy\s","united\sdemocratic\sliberation\sarmy","united\skarbi\sliberation\sarmy","united\sliberation\sfront\sof\sbarak\svalley\sindia","united\srevolutionary\sfront","united\stribal\sliberation\sarmy","volunteers\sof\sinnocent\speople\sof\snagas\s","yimchunger\sliberation\sfront\s","youths","zeliangrong\sunited\sfront","zomi\srevolutionary\sarm"]
search2 = ["armed\sassault","assassination","bombing","infrastructure\sattack","hijacking","kidnapping","unarmed\sassault","barricade\sIncident"]
search3 = ["mumbai","bangalore","kashmir","bihar","assam"]
count1 = dict.fromkeys(search1, 0)

import re

with open('newsDataGname.txt', 'r') as searchfile:
    for line in searchfile:
        for word1 in search1:
            if re.search( word1, line, re.M|re.I):
                count1[word1] += 1
for key,val in count1.items():
    if val>0:
        print(key +"->"+str(val)+",")
#print(count1)
#print("--------------------------------------------------------------------------------------") 
#print(count)   
count2 = dict.fromkeys(search2, 0)
with open('newsDataGname.txt', 'r') as searchfile:
    for line in searchfile:
        for word2 in search2:
            if re.search( word2, line, re.M|re.I):
                count2[word2] += 1
for key,val in count2.items():
    if val>0:
        print(key+"->"+str(val)+",")
count3 = dict.fromkeys(search3, 0)
with open('newsDataGname.txt', 'r') as searchfile:
    for line in searchfile:
        for word3 in search3:
            if re.search( word3, line, re.M|re.I):
                count3[word3] += 1
for key,val in count3.items():
    if val>0:
        print(key+"->"+str(val)+",") 
flag = 0

for key,val in count1.items():
    s = ''
    if val>0:
        s = key
        flag=0
        for key1,val1 in count2.items():
            if val1>0:
                s = s+","+key1
                for key2,val2 in count3.items():
                    if val2>0:
                        flag = 1
                        s = s+","+key2
                        print(s)
                        data.append(s.split(","))
                        s = key+","+key1
                if(flag==0):
                    data.append(s.split(","))
                       
        s= key


print(data)
csv_writer(data, path)

exit()

"""           for key,val in count1.items():
        if(isinstance(val,int)):
            mystr =key+","+str(val)
            data.append(mystr.split(","))
        else:
            for key1,val1 in val.items():
                mystr =key+","+str(val)+","+str(val1)
                data.append(mystr.split(","))
            #print(data)
    if(mycount==0):
        #csv_writer(data, path)
        print(data)
                exit()"""
    #print(mystr)
#print(data)


#add the count number of entries to csv with the attack type being the key
#in the dictinary with the city name(if multiple cities then again 
#multiple entries-ex:2 cities and 2 attack type:we will have 4 entries)
#Similarily dates as well:all these got from the named entity rec
#Append all to single list and if there is no entry put unknown for gname
#and blanks for other entries so that the structure matches with GTD.
#Each entry is a list which is entered to csv

#add csv code with a dummy list...make changes to the dummy list to get
#actual contents

#csv file structure

#date/year/month/date city/provstate gname attack_type """