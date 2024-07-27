import os
import asyncio
from duckduckgo_search import AsyncDDGS as ddgs

red = '\033[31;1m'
green = '\033[92;1m'
falcon = '\033[101m[(0)--(0)]\033[0m' + green
def draw():
    text2 ="""
"""
    text = """
               _,.,  °        ,-·-.          ,'´¨;                   _,.,  °    
        ,.·'´  ,. ,  `;\ '      ';   ';\      ,'´  ,':\'          ,.·'´  ,. ,  `;\ '  
      .´   ;´:::::\`'´ \'\       ;   ';:\   .'   ,'´::'\'       .´   ;´:::::\`'´ \'\  
     /   ,'::\::::::\:::\:'      '\   ';::;'´  ,'´::::;'       /   ,'::\::::::\:::\:' 
    ;   ;:;:-·'~^ª*';\'´          \  '·:'  ,'´:::::;' '      ;   ;:;:-·'~^ª*';\'´   
    ;  ,.-·:*'´¨'`*´\::\ '          '·,   ,'::::::;'´        ;  ,.-·:*'´¨'`*´\::\ '  
   ;   ;\::::::::::::'\;'            ,'  /::::::;'  '       ;   ;\::::::::::::'\;'   
   ;  ;'_\_:;:: -·^*';\          ,´  ';\::::;'  '         ;  ;'_\_:;:: -·^*';\   
   ';    ,  ,. -·:*'´:\:'\°        \`*ª'´\\::/‘            ';    ,  ,. -·:*'´:\:'\° 
    \`*´ ¯\:::::::::::\;' '        '\:::::\';  '            \`*´ ¯\:::::::::::\;' '
      \:::::\;::-·^*'´               `*ª'´‘                  \:::::\;::-·^*'´     
        `*´¯                          '                       `*´¯              
"""
    os.system("clear")
    os.system("echo " + red)
    print(text2)
    print(text)
    os.system("echo " + green)

async def duckSearch(word,max_result=100,file='robots.txt'):
        result = await ddgs(proxy=None).atext(word,max_results=max_result)
        with open(file,'w+') as f:
          for r in result:
              print(r["href"])
              f.writelines(r['href'] + '\n')


if __name__ == "__main__":
      draw()
      asyncio.run(duckSearch(word=input(falcon+" Enter dork query: "),max_result=int(input(falcon+" Display results[eg: 100]: ")),file=input(falcon+" Save file[robots.txt]: ")))

