def create_youtube_video(title,description):
	youtube_video = {"Title": title,"description": description, "likes": 0, "dislikes": 0,"comments": {"username": " "}}
	return youtube_video

def likes(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1
	return youtube_video 

def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1
	return youtube_video

def add_comment(youtube_video,username1,commen_text):
	youtube_video[comments[username]]==commen_text
	return youtube_video

mahmoud = create_youtube_video("firstvideo","ilikeyoutube")

for i in range(495):
	 likes(mahmoud)


print(mahmoud)