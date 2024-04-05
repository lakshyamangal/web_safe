from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask import send_from_directory
from flask import send_file
import re
import joblib
import pickle
from fpdf import FPDF
import time
# import model.py
import pandas as pd
from urllib.parse import urlparse, urlencode
from urllib.parse import parse_qsl, urljoin, urlparse
import ipaddress

from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
import requests

from datetime import datetime
import os



class features:

    def getDomain(self, url):
        domain = urlparse(url).netloc
        if re.match(r"^www.", domain):
            domain = domain.replace("www.", "")
        return domain

    def havingIP(self, url):
        try:
            ipaddress.ip_address(url)
            ip = 1
        except:
            ip = 0
        return ip

    def haveAtSign(self, url):
        if "@" in url:
            at = 1
        else:
            at = 0
        return at

    def getLength(self, url):

        if len(url) < 54:
            length = 0
        else:
            length = 1
        return length

    def getDepth(self, url):
        s = urlparse(url).path.split('/')
        depth = 0
        for j in range(len(s)):
            if len(s[j]) != 0:
                depth = depth + 1
        return depth

    def redirection(self, url):
        pos = url.rfind('//')
        if pos == 6 or pos == 7:
            return 0
        else:
            return 1

    def httpDomain(self, url):
        domain = urlparse(url).netloc
        if 'https' in domain:
            return 1
        else:
            return 0

    def tinyURL(self, url):
        shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                              r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                              r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                              r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                              r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                              r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                              r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                              r"tr\.im|link\.zip\.net"
        match = re.search(shortening_services, url)
        if match:
            return 1
        else:
            return 0

    def prefixSuffix(self, url):
        if '-' in urlparse(url).netloc:
            return 1
        else:
            return 0

    def web_traffic(self, url):
        try:
            url = urllib.parse.quote(url)
            a = urllib.request.urlopen("http://" + url).read()
            print('innerinner')
    
            rank =  BeautifulSoup(a,"html.parser").find("REACH")['RANK']
            print('inner')
    
            rank = int(rank)

        except TypeError:
            return 1
        if rank < 100000:
            return 1
        else:
            return 0

    def domainAge(self, domain_name):
        creation_date = domain_name.creation_date
        expiration_date = domain_name.expiration_date
        if (isinstance(creation_date, str) or isinstance(expiration_date, str)):
            try:
                creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
            except:
                return 1

            if ((expiration_date is None) or (creation_date is None)):
                return 1
            elif ((type(expiration_date) is list) or (type(creation_date) is list)):
                return 1
            else:
                ageofdomain = abs((expiration_date - creation_date).days)

            if ((ageofdomain / 30) < 6):
                age = 1
            else:
                age = 0

        return age

        def domainEnd(self, domain_name):
            expiration_date = domain_name.expiration_date
            if isinstance(expiration_date, str):
                try:
                    expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
                except:
                    return 1

                if (expiration_date is None):
                    return 1
                elif (type(expiration_date) is list):
                    return 1
                else:
                    today = datetime.now()
                    end = abs((expiration_date - today).days)

                    if ((end / 30) < 6):
                        end = 0
                    else:
                        end = 1
            return end

    def iframe(self, response):
        if response == "":
            return 1
        else:
            if re.findall(r"[<iframe>|<frameBorder>]", response.text):
                return 0
            else:
                return 1

    def mouseOver(self, response):
        if response == "":
            return 1
        else:
            if re.findall("<script>.+onmouseover.+</script>", response.text):
                return 1
            else:
                return 0

    def rightClick(self, response):
        if response == "":
            return 1
        else:
            if re.findall(r"event.button ?== ?2", response.text):
                return 0
            else:
                return 1

    def forwarding(self, response):
        if response == "":
            return 1
        else:
            if len(response.history) <= 2:
                return 0
            else:
                return 1

    def create_report(self,arr,sol):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20)

        pdf.cell(200, 10, txt="Report of URL", ln=1, align='C')

        pdf.cell(200, 10, txt="", ln=2, align='C')

        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Domain of the URL: {}".format(arr[0]), ln=3, align='J')
        pdf.cell(200, 10, txt="Do the URL contain IP: {}".format(arr[1]), ln=4, align='J')
        pdf.cell(200, 10, txt="Does it have @ sine: {}".format(arr[2]), ln=5, align='J')
        pdf.cell(200, 10, txt="Length of URL: {}".format(arr[3]), ln=6, align='J')
        pdf.cell(200, 10, txt="How deep is your URL: {}".format(arr[4]), ln=7, align='J')
        pdf.cell(200, 10, txt="Does it redirect: {}".format(arr[5]), ln=8, align='J')
        pdf.cell(200, 10, txt="Does it follow HTTP protocol: {}".format(arr[6]), ln=9, align='J')
        pdf.cell(200, 10, txt="Is the URL very small: {}".format(arr[7]), ln=10, align='J')
        pdf.cell(200, 10, txt="Does it have misleading prefix or suffix: {}".format(arr[8]), ln=11, align='J')
        pdf.cell(200, 10, txt="Does it have DNS: {}".format(arr[9]), ln=12, align='J')
        pdf.cell(200, 10, txt="Does it have enough Web Traffic: {}".format(arr[10]), ln=13, align='J')
        pdf.cell(200, 10, txt="Does it have enough Domain Age: {}".format(arr[11]), ln=14, align='J')
        pdf.cell(200, 10, txt="Does it have enough Domain End: {}".format(arr[12]), ln=15, align='J')
        pdf.cell(200, 10, txt="iframe: {}".format(arr[13]), ln=16, align='J')
        pdf.cell(200, 10, txt="mouseover: {}".format(arr[14]), ln=17, align='J')
        pdf.cell(200, 10, txt="rightclick: {}".format(arr[15]), ln=18, align='J')
        pdf.cell(200, 10, txt="Does it forward you further: {}".format(arr[16]), ln=19, align='J')

        if sol == 1:
            result = 'Malicious Website'
        else:
            result = 'Safe Website'
        pdf.set_font("Arial", size=20)
        pdf.cell(200, 20, txt="Finally we Declare this as a "+result, ln=20, align='J',)


        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 20, txt="Through the following graph you can compare your report with others", ln=21, align='c')
        workingdir = os.path.abspath(os.getcwd())
        pdf.image(workingdir + '/static/plotcheck.png', w=175, h=128)
        pdf.cell(200, 20, txt="Understand contribution of features to which form such Malicious websites", ln=22, align='c')
        pdf.image(workingdir + '/static/feature.png', w=150, h=90)

        pdf.add_page()
        pdf.set_font("Arial", size=17)
        pdf.cell(200, 30, txt="Meaning of the Report", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 20, txt="We will try to explain what you can infer from the above document", ln=2, align='J')

        pdf.cell(200, 10, txt='If an IP address is used as an alternative of the domain name in the URL, such as', ln=3,
                 align='J')
        pdf.cell(200, 10, txt='http://125.98.3.123/fake.html , users can be sure that someone is trying to steal ',
                 ln=3, align='J')
        pdf.cell(200, 10, txt='their personal information. Sometimes, the IP address is even transformed into ', ln=3,
                 align='J')
        pdf.cell(200, 10,
                 txt='hexadecimal code as shown in the following link http://0x58.0xCC.0xCA.0x62/2/paypal.ca/index.html.',
                 ln=3, align='J')

        pdf.cell(200, 20, txt="Long URL can hide information therefore length of URL is calculated", ln=4, align='J')

        pdf.cell(200, 10,
                 txt="Such Websites have less age and usually a closer ending period and most of the time they ", ln=5,
                 align='J')
        pdf.cell(200, 10, txt="are missing the domain ", ln=5, align='J')

        pdf.cell(200, 10,
                 txt="Web traffic measures the popularity of the website by determining the number of visitors and",
                 ln=5, align='J')
        pdf.cell(200, 10, txt=' the number of pages they visit. However, since phishing websites live for a short ',
                 ln=5, align='J')
        pdf.cell(200, 10, txt="period of time, they may not be recognized by the Alexa database (Alexa the Web ", ln=5,
                 align='J')
        pdf.cell(200, 10, txt="Information Company., 1996). By reviewing our dataset, we find that in worst scenarios,",
                 ln=5, align='J')
        pdf.cell(200, 10,
                 txt="legitimate websites ranked among the top 100,000. Furthermore, if the domain has no traffic",
                 ln=5, align='J')
        pdf.cell(200, 10, txt='or is not recognized by the Alexa database, it is classified as Phishing.', ln=6,
                 align='J')
        pdf.cell(200, 10, txt='IFrame is an HTML tag used to display an additional webpage into', ln=7, align='J')
        pdf.cell(200, 10,
                 txt='one that is currently shown. Phishers can make use of the iframe tag and make it invisible', ln=7,
                 align='J')
        pdf.cell(200, 10,
                 txt='i.e. without frame borders. In this regard, phishers make use of the frameBorder attribute which causes',
                 ln=7, align='J')
        pdf.cell(200, 10, txt='the browser to render a visual delineation', ln=7, align='J')
        pdf.set_font("Arial", size=17)
        pdf.cell(200, 20, txt='REFERENCES', ln=8, align='C')

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 5, txt='Mohammad, R.M., Thabtah, F. and McCluskey, L., 2015.', ln=9, align='C')
        pdf.cell(200, 5, txt='Phishing websites features. ', ln=9, align='C')
        pdf.cell(200, 5, txt='School of Computing and Engineering, University of Huddersfield.', ln=9, align='C')
        pdf.output("report.pdf")

    def featureExtraction(self, url, label):
        features = []
        features.append(self.getDomain(url))
        features.append(self.havingIP(url))
        features.append(self.haveAtSign(url))
        features.append(self.getLength(url))
        features.append(self.getDepth(url))
        features.append(self.redirection(url))
        features.append(self.httpDomain(url))
        features.append(self.tinyURL(url))
        features.append(self.prefixSuffix(url))
        # print('inner')
    
        dns = 0
        try:
            domain_name = whois.whois(urlparse(url).netloc)
        except:
            dns = 1
        # print('inner')
    
        features.append(dns)
        print('inner')
    
        features.append(self.web_traffic(url))
        print('inner')
    
        features.append(1 if dns == 1 else domainAge(domain_name))
        print('inner')

        features.append(1 if dns == 1 else domainEnd(domain_name))
        print('inner')
    
        try:
            response = requests.get(url)
        except:
            response = ""
        print('inner')
    
        features.append(self.iframe(response))
        features.append(self.mouseOver(response))
        features.append(self.rightClick(response))
        features.append(self.forwarding(response))
        features.append(label)
        print('inner')
    
        return features


# setup the app
application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SECRET_KEY'] = "SuperSecretKey"





feat = []
@application.route('/')
@application.route('/home')
def workstation():
    return render_template('index.html')


@application.route('/result', methods = ['POST'])
def signup():
    # URL = request.form['url']
    URL= "www.google.com"
    
    feat_obj = features()
    # feat = pickle.load(open('features.pkl','rb'))
    print('hello')
    feat = feat_obj.featureExtraction(URL,0)

    column = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth',
       'Redirection', 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record',
       'Web_Traffic', 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over',
       'Right_Click', 'Web_Forwards', 'Label']


    d = {}
    print('hello')
    
    for i,elem in enumerate(column):
        d[elem]=feat[i]

    df = pd.DataFrame(d, index=[0])

    df = df.drop(columns=['Domain'])
    df = df.drop(columns=['Label'])
    print('hello')
    
    # print(df.columns)
    # print(df.head)
    #
    # model = pickle.load(open('mlp.pkl','rb'))

    model = joblib.load('mlp.pkl')
    print("The email address is " + str(feat) + "")
    sol = model.predict(df)
    print('hello')

    # print("The email address is " + feat + "")
    print("solution" + str(sol) + "")
    return download_file(URL,feat,feat_obj,sol)


#


@application.route('/download')
def download_file(URL,feat,feat_obj,sol):


    feat_obj.create_report(feat,sol)
    time.sleep(5)
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files/'
    return send_from_directory('', 'report.pdf')