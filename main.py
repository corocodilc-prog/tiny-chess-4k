import json as J,os
from urllib.request import Request,urlopen
V=(0,100,320,335,500,950,0)
T="KKKKKKKKKKKPKPPZKPU_PPUdUU_iKKKK##--#7KK-KUZ-PZ_-KZ_-PUZ#7KP##--7AAAAKKKAKPUAPPUAKUUAUUUAPKK7AAAKKKKPUUUFKKKFKKKFKKKFKKKFKKKKKKP7AAFAKKKAKPPFKPPFKPPAPPPAKKK7AAF-###-###-###-###7--#A777__KK_iUK"
MT=10**5
NC=125000
N=0
TT={}
KN=(-33,-31,-18,-14,14,18,31,33)
RD=(-16,-1,1,16)
BD=(-17,-15,15,17)
KG=RD+BD
AB=Exception
def A(b,s,y):
 for D,a in(((-15*y,-17*y),1),(KN,2),(KG,6)):
  for d in D:
   t=s+d
   if not t&136 and b[t]==a*y:return 1
 for D,P in((RD,(4,5)),(BD,(3,5))):
  for d in D:
   t=s+d
   while not t&136 and not b[t]:t+=d
   if not t&136 and b[t]*y in P:return 1
 return 0
def G(b,w,e):
 m=[]
 for f,p in enumerate(b):
  if not p or p*w<0:continue
  a=abs(p)
  if a==1:
   d=16*w;Q=5<<14 if f>>4==6-5*(w<0)else 0
   for o in(d,d-1,d+1):
    t=f+o
    if t&136:continue
    v=(b[t] and b[t]*w<0)or t==e
    if b[t] if o==d else not v:continue
    m.append(f|t<<7|Q)
   if f>>4==1+5*(w<0) and not b[f+d] and not b[f+2*d]:m.append(f|(f+2*d)<<7)
  elif a in(2,6):
   for d in(KN,KG)[a==6]:
    t=f+d
    if not t&136 and(not b[t] or b[t]*w<0):m.append(f|t<<7)
   if a==6 and f==4+112*(w<0) and not A(b,f,-w):
    for o in(2,-2):
     if b[f+3 if o>0 else f-4]==4*w and not b[f+o//2] and not b[f+o] and not A(b,f+o//2,-w) and not A(b,f+o,-w) and(o>0 or not b[f+o-1]):m.append(f|(f+o)<<7)
  else:
   for d in(BD,RD,RD+BD)[a-3]:
    t=f+d
    while not t&136 and not b[t]:m.append(f|t<<7);t+=d
    if not t&136 and b[t]*w<0:m.append(f|t<<7)
 return m
def M(b,m,w,e,k):
 f=m&127;t=m>>7&127;q=m>>14&7;p=b[f];v=b[t]
 n=p==w and t==e and not v
 b[t]=q*w if q else p;b[f]=0
 if abs(p)==6:
  k[w<0]=t
  if abs(t-f)==2:
   s=f+3 if t>f else f-4
   b[f+1 if t>f else f-1]=b[s];b[s]=0
 elif n:b[t-16*w]=0
 e=f+16*w if p==w and t-f==32*w else -1
 return e
def F(b,w):
 s=0
 for i,p in enumerate(b):
  if p:
   a=abs(p);r=i>>4;f=min(i&7,7-(i&7))
   v=V[a]+ord(T[(a-1)*32+(r if p>0 else 7-r)*4+f])-75
   s+=v if p>0 else -v
 return s*w+12
def O(m,b,t):return MT if m==t else 10000+abs(v) if(v:=b[m>>7&127])else 0
def S(b,w,d,a,z,p,e,k):
 global N
 N+=1
 if N>NC:raise AB
 h=A(b,k[w<0],-w)
 if d<=0:
  s=F(b,w);a=max(a,s)
  if a>=z:return z
 ms=G(b,w,e)
 if d<=0:ms=[m for m in ms if h or b[u:=m>>7&127] or m>>14 or u==e]
 t=0
 if d>0:
  y=(tuple(b),w,e);n=TT.get(y)
  if n and n[0]>=d:
   if n[1]==0 or n[1]==1 and n[2]>=z or n[1]==2 and n[2]<=a:return n[2]
   t=n[3]
 ms.sort(key=lambda m:-O(m,b,t))
 bs=-MT;bm=0;f=2;lg=0
 for m in ms:
  b2=b[:];k2=k[:]
  e2=M(b2,m,w,e,k2)
  if A(b2,k2[w<0],-w):continue
  lg+=1
  v=-S(b2,-w,d-1,-z,-a,p+1,e2,k2)
  if v>bs:bs=v;bm=m
  if v>a:a=v;f=0
  if a>=z:f=1;break
 if not lg:return -MT+p if h else a if d<=0 else 0
 if d<=0:return a
 TT[y]=(d,f,bs,bm)
 return bs
def Y(f):
 b=[0]*128;k=[0,0];q=f.split();i=112
 for s in q[0]:
  if s=="/":i-=24
  elif s.isdigit():i+=int(s)
  else:
   x="PNBRQK".index(s.upper())+1;b[i]=x if s<'a' else -x
   if x==6:k[s>='a']=i
   i+=1
 w=1-(q[1]=="b")*2
 e=ord(q[3][0])-97+int(q[3][1])*16-16 if q[3]!="-" else -1
 return b,w,e,k
def Z(m):
 f=m&127;t=m>>7&127
 s="".join(chr(97+x%8)+str(x//16+1) for x in(f,t))
 return s+"q" if m>>14 else s
def R(b,w,e,k,ls):
 global N
 L=[m for m in G(b,w,e) if Z(m) in ls]
 if not L:return None,-MT
 L.sort(key=lambda m:-O(m,b,0))
 bm=L[0];bv=-MT;N=0;TT.clear()
 for d in range(10):
  try:
   a=-MT;z=MT;cb=bm
   for m in L:
    b2=b[:];k2=k[:]
    e2=M(b2,m,w,e,k2)
    v=-S(b2,-w,d,-z,-a,1,e2,k2)
    if v>a:a=v;cb=m
   bm,bv=cb,a
  except AB:break
 return bm,bv
def X(p,y):
 try:
  with urlopen(Request(os.getenv("MAKEFUN_ENV_URL")+p,J.dumps(y).encode(),{"content-type":"application/json"}),timeout=9) as s:return J.load(s)
 except:return{"status":"error"}
if __name__=="__main__":
 while 1:
  g=X("/game",{})
  if g["status"]=="done":break
  i=g["game"]
  while g["status"]=="your_move":
   b,w,e,k=Y(g["fen"]);ls=g["legal_moves"]
   m,v=R(b,w,e,k,ls)
   g=X("/resign",{"game":i}) if v<=-MT+200 else X("/move",{"game":i,"move":Z(m)})
   if g["status"]=="error":X("/resign",{"game":i});break
