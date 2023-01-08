def kanji(uchar):
    return True if u'\u4e00' <= uchar <= u'\u9fff' else False
def kata(uchar):
    return True if u'\u30a0' <= uchar <= u'\u30ff' else False
original=open('原文.txt','r',encoding='UTF-8')
before=open('处理前.txt','r',encoding='UTF-8')
after=open('处理后.txt','w', encoding='UTF-8')
after.truncate()
length=len(original.readlines())
original.seek(0)
for p in range(length):
    o=original.readline()
    b=before.readline()
    i=0
    while i<len(b):#删除片假名后的振假名
        j=0
        if kata(b[i]):
            while i+j<len(b) and kata(b[i]) :
                if b[i]=='ー' and not kata(b[i-1]):
                    i+=1
                    break
                i+=1
                j+=1
        else:
            i+=1
        b=b[:i]+b[i+j::]
        
    a=''
    oi=0
    bi=0
    while bi < len(b):
        if kanji(b[bi]):
            a+='{{Photrans|'
            while kanji(b[bi]):#将汉字放入“写作”部分
                a+=b[bi]
                oi+=1
                bi+=1
            a+='|'
            bj=0
            while bi+bj<len(b) and not kanji(b[bi+bj]):#找到b的结尾或下一处假名
                bj+=1
            oj=0
            while oi+oj<len(o) and not kanji(o[oi+oj]):#找到o的结尾或下一处假名
                oj+=1
            a+=b[bi:bi+bj-oj]+'}}'#将振假名放入“读作”部分
            b=b[:bi]+b[bi+bj-oj::]#删除b中的振假名
        elif b[bi:bi+7]=='{{ruby|':#ruby不作处理
            while 1:
                bi+=1
                if b[bi:bi+2]=='}}':
                    break
            while 1:
                a+=o[oi]
                oi+=1
                if o[oi:oi+2]=='}}':
                    break
        else:
            a+=b[bi]
            oi+=1
            bi+=1
    after.write(a)
original.close()
before.close()
after.close()
