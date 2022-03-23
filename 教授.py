for p in range(2):                                  #p:王教授是苏州人
    for q in range(2):                              #q:王教授是上海人
        for r in range(2):                          #r:王教授是杭州人
         #以下三行表示p,q,r不可能同时为真的情况
         if (p == 1 and q == 1): continue
         if (p == 1 and r == 1): continue
         if (q == 1 and r == 1): continue
         
         Jia = (not p) and q                        #甲的判断
         Yi = p and (not q)                         #乙的判断
         Bing = (not q) and (not r)                 #丙的判断
       
         B1 = (not p) and q                         #甲的判断全对
         B2 = ((not p) and (not q))or (p and q)     #甲的判断一半对
         B3 = p and (not q)                         #甲的判断全错
         
         C1 = p and (not q)                         #乙的判断全对
         C2 = (p and q) or ((not p) and (not q))    #乙的判断一半对
         C3 = (not p) and q                         #乙的判断全错
         
         D1 = (not q) and (not r)                   #丙的判断全对
         D2 = ((not q) and r) or (q and(not r))     #丙的判断一半对
         D3 = q and r                               #丙的判断全错

         #题设条件
         E = (B1 and C2 and D3) \
           or(B1 and C3 and D2) \
           or(B2 and C1 and D3) \
           or(B2 and C3 and D1) \
           or(B3 and C1 and D2) \
           or(B3 and C2 and D1)

         #符合王教授所的E值
         if E==1 :
           print(" E=%d,Jia=%d,Yi=%d,Bing=%d"%(E,Jia,Yi,Bing))
