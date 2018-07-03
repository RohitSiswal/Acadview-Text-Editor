#1.Extract id,domain name n suffix
import re
email1 = "zuck26@facebook.com"
email2 = "page33@google.com"
email3 = "jeff42@amazon.com"
matchObj = re.match(r'(......)*@(........)*.(...)',email1)
print(matchObj.groups())
matchObj = re.match(r'(......)*@(......)*.(...)',email2)
print(matchObj.groups())
matchObj = re.match(r'(......)*@(......)*.(...)',email3)
print(matchObj.groups())

#2.Retrieve words starting from b or B
import re
text = "Betty bought a bit of butter,But the butter was so bitter,So she bought some better butter,To make the bitter butter better."
matches = re.findall(r'[bB]+\w+',text)
for i in matches:
    print('Match:%s'%(i))

#3.spliting the sentence
sen1 = "A,very very"
sen2 = ";irregular"
sen3 = "_sentence"
new1 = re.sub(r',',' ',sen1)
new2 = re.sub(r';',' ',sen2)
new3 = re.sub(r'_',' ',sen3)
print(new1,new2,new3)