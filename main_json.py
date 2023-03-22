from exportcomments import ExportComments, base
from exportcomments.settings import DEFAULT_BASE_URL
import pandas as pd
import requests, os, time, json
############ Importing configuration from config.json  ############
path=os.path.dirname(__file__)
with open(os.path.join(path,'config.json'), 'r') as f:
    config = json.load(f)
if not os.path.exists(os.path.join(path,'img')): os.makedirs(os.path.join(path,'img'))
############ Please only edit the following three lines ############
input_=config['input'] #Input file
output_=config['output'] #Output file
token=config['token'] #ExportComments API Access Token
#################################
ex=ExportComments(token)
version=base.version
mod=base.ModelEndpointSet(token=token, base_url=DEFAULT_BASE_URL)
#Loading Log data if the logfile exists
logfile=os.path.join(path,config['log']) #The log file
if not os.path.isfile(logfile): IDs,GUIDs,STATUS,Upload,Download=([] for i in range(5))
else:
    log=pd.read_excel(logfile)
    IDs=log['ID'].values.tolist()
    GUIDs=log['GUID'].values.tolist()
    STATUS=log['STATUS'].values.tolist()
    Upload=log['Upload'].values.tolist()
    Download=log['Download'].values.tolist()
df=pd.read_excel(os.path.join(path,input_))
#Just to check the internet connection if everything is okay
def GetContent(data,type):
    while True:
        try:
            if requests.get("https://www.google.com").status_code==200:
                if type=='GUID': return ex.exports.check(guid=data)
                elif type=='URL': return ex.exports.create(url=data, replies='false')
                elif type=='GET': return requests.get(data)
        except:time.sleep(2)

def DownloadImg(cont):
    filepath=os.path.join(path,'img',cont['commentId']+'.jpg')
    if not os.path.isfile(filepath):
        with open(filepath, 'wb') as f: f.write(GetContent(cont['images'][0],'GET').content)
#Upload requests
for i in range(10,15):
    url=df["URL"][i]
    ID=url.split('/')[-1]
    #If comments NB > 0 AND if this ID has never been downloaded before
    if df['Comments'][i] > 0 and True not in [True for x in [y for y,x in enumerate(IDs) if x==ID] if STATUS[x]=='done']:
        #Check the possibility to upload a post URL; Maximum parallel requests=4
        while True:
            rep=GetContent(url,'URL').body
            if len(rep['data'])==4:time.sleep(20)
            else:
                IDs.append(str(ID))
                GUIDs.append(rep['data']['guid'])
                STATUS.append('progress')
                Upload.append(str(time.time()))
                Download.append('0')
                break

log=pd.DataFrame({'ID': IDs, 'GUID': GUIDs, 'STATUS': STATUS,'Upload': Upload,'Download': Download})
#Downloading ready files
lista=[[] for x in range(6)]
key=['postId','commentId','time','message','likes','images']

while 'progress' in list(log['STATUS']):
    time.sleep(20)
    for i in range (len(log)):
        r=GetContent(log['GUID'][i],'GUID').body #Getting information on the status of the request
        new=r['data'][0]['status']
        if log['STATUS'][i]=='progress' and new=='done':
            #UPDATE the status/time of eatch Request
            log.at[i,'STATUS']=new
            log.at[i,'Download']=str(time.time())
            content=json.loads(GetContent("https://exportcomments.com"+r['data'][0]['rawUrl'],'GET').content.decode('utf-8'))
            for cont in content:
                for i in range(len(lista)-1):lista[i].append(str(cont[key[i]]).split('\r\n[PHOTO]')[0])
                if len(cont['images'])==0:lista[5].append('0')
                else:
                    DownloadImg(cont)
                    lista[5].append('1')
log.to_excel(logfile)
data=pd.DataFrame(
    {
    'PostID': lista[0],
    'CommentID': lista[1],
    'Time': lista[2],
    'Message': lista[3],
    'Likes': lista[4],
    'Images': lista[5]
    })
data.to_excel(os.path.join(path,output_))
