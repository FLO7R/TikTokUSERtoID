import requests
print("""\
███████╗██╗      ██████╗ ███████╗██╗  ██╗
██╔════╝██║     ██╔═══██╗╚════██║╚██╗██╔╝
█████╗  ██║     ██║   ██║    ██╔╝ ╚███╔╝
██╔══╝  ██║     ██║   ██║   ██╔╝  ██╔██╗
██║     ███████╗╚██████╔╝   ██║  ██╔╝ ██╗
╚═╝     ╚══════╝ ╚═════╝    ╚═╝  ╚═╝  ╚═╝ """)
while True:
 user= input('Enter TikTok Username--> ')
 url = "https://countik.com/api/exist/"+user
 resp = requests.get(url).json()
 print(resp['nickname'] )
 "\r\n"
 print(resp['id'])
 continue
