def kanji(uchar):
    return True if u'\u4e00' <= uchar <= u'\u9fff' else False
def kata(uchar):
    return True if u'\u30a0' <= uchar <= u'\u30ff' else False
def hira(uchar):
    return True if u'\u3040' <= uchar <= u'\u309f' else False
before=open('处理前.txt','r',encoding='UTF-8')
after=open('处理后.txt','w',encoding='UTF-8')
trans=open('译文.txt','r',encoding='UTF-8')
after.truncate()
after.write('{{Photrans/button}}\n{{Lyrics\n|lb-color=\n|rb-color=\n|lb=text1=\n')
length=len(before.readlines())
before.seek(0)
num=1
for p in range(length):
    b=before.readline()
    if b=='\n':
        after.write('|rb-text'+str(num)+'=\n')
        t=trans.readline()
        while t!='\n':
            after.write(t)
            t=trans.readline()
        num+=1
        after.write('|lb-text'+str(num)+'=\n')
        continue
    a=''
    i=0
    while i < len(b):
        if kanji(b[i]):
            for j in range(i,len(b)):#要求汉字有注音
                if b[j]=='(':
                    if hira(b[j+1]):#只有平假名是可隐藏的Photrans
                        head='{{Photrans|'
                    else:           #其他都是ruby
                        head='{{ruby|'
                    break
            else:
                break
            a+=head
            while kanji(b[i]):#将汉字放入“写作”部分
                a+=b[i]
                i+=1
            i+=1
            a+='|'
            while b[i]!=')':#将振假名放入“读作”部分
                a+=b[i]
                i+=1
            i+=1
            a+='}}'
        elif b[i:i+7]=='{{ruby|':#ruby不作处理
            while 1:
                i+=1
                if b[i:i+2]=='}}':
                    break
        else:
            a+=b[i]
            i+=1
    after.write(a)
after.write('\n|rb-text'+str(num)+'=\n')
t=trans.read()
after.write(t)
after.write('\n}}')
before.close()
after.close()
