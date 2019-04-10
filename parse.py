import csv
import pickle

def parse_lyrics_file(filename):
	with open('lyrics.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		songs_set1=set()
		lyrics_dict={}
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				song=" ".join((word.lower() for word in row[1].split("-")))
				song=song.lower()
				artist=" ".join((word.lower() for word in row[3].split("-")))
				artist=artist.lower()
				songs_set1.add(artist+song)
				lyrics_dict[artist+song]=[row[5]]
				line_count += 1
		print(len(songs_set1))
		return songs_set1,lyrics_dict

def parse_sent_file(filename):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		songs_set2=set()
		sent_dict={}
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				art=row[1].lower().strip()
				song=row[2].lower().strip()
				songs_set2.add(art+song)
				sent_dict[art+song]=[song,art,row[3]]
				line_count += 1
		print("Lines ",line_count)
		return songs_set2,sent_dict

def matchDatasets():
	songs_set1,lyrics_dict=parse_lyrics_file("lyrics.csv")
	# songs_set2,bin_sent_dict=parse_sent_file("songs_sent_bin.csv")
	songs_set2,quad_sent_dict=parse_sent_file("songs_sent_quad.csv")
	# print(len(bin_sent_dict),len(quad_sent_dict))

	count=0
	i1=0
	found_set=set()
	first=False
	for s2 in songs_set2:
		print("Song No.",i1)
		first=True
		# for s1 in songs_set1:
		if(first and s2 in songs_set1):
			first=False
			found_set.add(s2)
			print("Found",count)
			count+=1
		i1+=1

	# print(len(found_set),found_set)
	print(len(found_set))
	dbfile = open('found_set_quad.pkl', 'wb') 
	pickle.dump(found_set, dbfile)                      
	dbfile.close()


def get_final_dataset():
	_,lyrics_dict=parse_lyrics_file("lyrics.csv")
	# _,bin_sent_dict=parse_sent_file("songs_sent_bin.csv")
	_,quad_sent_dict=parse_sent_file("songs_sent_quad.csv")
	pick_off=open("found_set_quad.pkl","rb")
	found_set=pickle.load(pick_off)
	print("Number of matches",len(found_set))
	fin_data=[]
	for s in found_set:
		song=quad_sent_dict[s][0]
		art=quad_sent_dict[s][1]
		# bin_sent=bin_sent_dict[s][2]
		quad_sent=quad_sent_dict[s][2]
		lyr=lyrics_dict[s]
		fin_data.append([song,art,lyr,quad_sent])

	dbfile = open('fin_data_quad.pkl','wb')
	pickle.dump(found_set, dbfile)                      
	dbfile.close()
	print(len(fin_data))
	# print(fin_data[0:10])
	# print(fin_data[])

# get_final_dataset()
# matchDatasets()


