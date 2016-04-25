import csv
def csv_writer(data, path):

    #Mode can be wb for writing and ab for appending
    
    #Here the first row which are the coloumn names should be added in the 
    #code initially and only once it has to be entered
    

    #For first row put in wb and other entries ab
    #This should run only once
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow("Gname,Count".split(","))
    
    #For new rows only which will run in multiple loops:
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
data = [['maoists', '2'], ['naxalites', '1'], ['maoists', '1'], ['extremists', '1'], ['terrorists', '1'], ['bandits', '1'], ['gunmen', '1'], ['muslims', '1'], ['insurgents', '1'], ['muslim\\srebels', '1'], ['national\\ssocialist\\scouncil\\sof\\snagaland', '1'], ['terrorists', '1'], ['secessionists', '1'], ['terrorists', '1'], ['al\\sfajr', '1'], ['hizbul\\smujahideen', '1'], ['militants', '1'], ['muslims', '1'], ['indian\\smujahideen', '1']]
[['maoists', '2'], ['naxalites', '1'], ['maoists', '1'], ['extremists', '1'], ['terrorists', '1'], ['bandits', '1'], ['gunmen', '1'], ['muslims', '1'], ['insurgents', '1'], ['muslim\\srebels', '1'], ['national\\ssocialist\\scouncil\\sof\\snagaland', '1'], ['terrorists', '1'], ['secessionists', '1'], ['terrorists', '1'], ['al\\sfajr', '1'], ['hizbul\\smujahideen', '1'], ['militants', '1'], ['muslims', '1'], ['indian\\smujahideen', '1'], ['terrorists', '2']]
[['maoists', '2'], ['naxalites', '1'], ['maoists', '1'], ['extremists', '1'], ['terrorists', '1'], ['bandits', '1'], ['gunmen', '1'], ['muslims', '1'], ['insurgents', '1'], ['muslim\\srebels', '1'], ['national\\ssocialist\\scouncil\\sof\\snagaland', '1'], ['terrorists', '1'], ['secessionists', '1'], ['terrorists', '1'], ['al\\sfajr', '1'], ['hizbul\\smujahideen', '1'], ['militants', '1'], ['muslims', '1'], ['indian\\smujahideen', '1'], ['terrorists', '2'], ['militants', '1']]

csv_writer(data, "newsData.csv")