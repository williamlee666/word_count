#from django.http import HttpResponse
from django.shortcuts import render
import jieba


def home(request):
	return render(request,'home.html')


def count(request):
	txt=request.GET['text']
	dic={}
	text = jieba.lcut(txt)
	for word in text:
		dic[word]=dic.get(word,0)+1
	sortedDic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
	length=len(text)
	return render(request,'count.html',{'lenText':length,'T':text,
		'D':dic,'S':sortedDic}
		)