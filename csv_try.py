import csv
def csv_writer(data, path):

    #Mode can be wb for writing and ab for appending
    
    #Here the first row which are the coloumn names should be added in the 
    #code initially and only once it has to be entered
    

    #For first row put in wb and other entries ab
    #This should run only once
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow("iyear,imonth,idate,city,gname,attack_type".split(","))
    
    #For new rows only which will run in multiple loops:
    with open(path, "ab") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


#Call it from the method you want,here I just tried from main as I didn't
#have other methods



if __name__ == "__main__":
    data=[]
    s="2014,10,10,mumbai,Let,bombing"
    s2="2014,10,10,mumbai,Let,bombing"
    path = "output.csv"
    data.append(s.split(","))
    data.append(s2.split(","))
    print(data)
    csv_writer(data, path)

#Here every article ka summary is in a seperate file...don't do that correlation ka logic here
#I meant not multiple summaries in one file as date,city and other details will vary
#Lets keep those two logics seperate
#2 seperate csvs



#Create a global list
#1...Create a string and add year,date,month or as whole one day from entities,add a comma,then add city from entities,add comma,add gname,add comma
#2...If it is gnames duplicate the whole string n times and only change the gname part 
#3...Before the next article is read add the string/strings to the list

#I dunno if we have to handle the case of multiple dates and multiple cities
#If so we will have many loops
#Let's try that later..as of now this is enough I think



#Append every single entry to string and put those strings to a list and then 
#this code will loop throught the lists to write to csv


#Every time append to the string with  comma as the delimiter
#Every time within the loop while appending the string add split(",")