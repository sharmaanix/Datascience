from sklearn import  tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
#[height,weight,shoe size]
 

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
	 [166,65,40],[190,90,47],[175,64,39],[175,64,39],[177,70,40],
	 [159,55,37],[171,75,42],[181,85,43]]

y=['male','female','female','female','male','male','male',
	'male','female','male','female','male']

prediction=[]

#decision tree classifier
clf = tree.DecisionTreeClassifier()
clf=clf.fit(X,y)

prediction1 = clf.predict([[190,70,43]])
prediction.append(str(prediction1))

print("the Decision Tree classifier prediction:"+str(prediction1))

# Random forest classifier

clf1=RandomForestClassifier()
clf1=clf1.fit(X,y)
prediction2=clf1.predict([[190,70,43]])
prediction.append(str(prediction2))
print("Random Forest  classifier prediction:"+str(prediction2))


# AdaBoostClassifier
clf2=AdaBoostClassifier()
clf2=clf2.fit(X,y)
prediction3=clf2.predict([[190,70,43]])
prediction.append(str(prediction3))
print('AdaBoostClassifier prediction:'+str(prediction3))


# using Gaussian Naive Bayes

gnb = GaussianNB()
prediction4=gnb.fit(X,y).predict([[190,70,43]])
prediction.append(str(prediction4))
print('Using Gaussian Naive Bayes, prediction:'+str(prediction4))


# using Support Vector Machine
clf4=svm.SVC()
clf4=clf4.fit(X,y)
prediction5=clf4.predict([[190,70,43]])
prediction.append(str(prediction5))
print('Using Support Vector Machine,prediction'+str(prediction5))



print(prediction)

count_m=0
count_f=0

for i in prediction:
	if i=="['male']":
		count_m+=1
	else:
		count_f+=1

print(count_m)
print(count_f)

if count_m>count_f:
	print('The correction prediction would be male')

else:
	print('The correction prediction would be female')	







		

