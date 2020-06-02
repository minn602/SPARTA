from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##
#매트리스의 평점 가져오기
movie = db.movies.find_one({'title':'매트릭스'})
print(movie['star'])
#매트릭스 평점과 같은 평점의 영화 제목들
same_star = list(db.movies.find({'star':'9.39'}))
for star in same_star:
    print(star['title'])
#2번문제 제목들의 평점을 0으로 만들기
db.movies.update_many({'star':'9.39'},{'$set':{'star':0}})
#평점 9.38보다 높은 영화들의 갯수 뽑기 for문 없이
counts = db.movies.find({'star':{'$gt':'9.38'}}).count()
print(counts)