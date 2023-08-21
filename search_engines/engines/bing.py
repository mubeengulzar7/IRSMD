from ..engine import SearchEngine
from ..config import PROXY, TIMEOUT, FAKE_USER_AGENT
#Test_GetURL Method
from ..utils import unquote_url
import requests



class Bing(SearchEngine):
    '''Searches bing.com (Requires Headers[Cookie] for Human-Readable Responses)'''
    def __init__(self, proxy=PROXY, timeout=TIMEOUT):
        super(Bing, self).__init__(proxy, timeout)
        #self._base_url = u'https://www.bing.com'
        self._base_url = u'https://www.bing.com/'
        #self.set_headers({'User-Agent':FAKE_USER_AGENT})
        #self.set_headers({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:100.0) Gecko/20100101 Firefox/100.0'})
        '''self.set_headers({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'})
        self.set_headers({'Cookies':'MUID=387DD974B44D621E1404D4E7B5996380; MUIDB=387DD974B44D621E1404D4E7B5996380;SRCHD=AF=S00028; SRCHUID=V=2&GUID=A729AD9F5A974C87AEEF35B2757E1F3C&dmnchg=1; ANON=A=0CAA0A2BE5471045C54E60F3FFFFFFFF&E=19dd&W=1; SRCHUSR=DOB=20190715&T=1641461861000&POEX=W; BFBUSR=BAWAS=1&BAWFS=1; BFB=AhCGUY1GNkLE-CueLG4N8NxFmRWriUkYLcFGJWz_eBxPj0ao0gTqnYHg4vWti2lSZHHQCQyqCp6Sl_tW097EE4tOawqlRuhTGl_463HQ7Rxn41hTQ5_FClIrHb6I_905u_BgxfkcQioFTYW6EZnAiC0rnm8Oc8cAaNQjM03i6lNUpQ; USRLOC=HS=1; UR=QS=0&TQS=0; SUID=A; WLS=C=1f23957445735855&N=Syed; SS=SID=23D67438C6C6693C20436585C7CF687B; U=1KqzpmU_icb8RNvTFGuuc2ojYuqFdaQ20bOEFBQdPIPaqRVHATsjyS-cvgYsgaJJXv79IWdLrSxMyVTxxc2rtsbMyevofQ77leArjSzKZyKby5InPwCYqntiV5jT6cX-AS5pSX_n3nMKeVF-cHTG67KlzKf7UYSrgZfcSD2XxJ7jOoYcFWh2Ta4NjzJI-buU6ETUCkz2HXeAVOyqbVm6tCw; ipv6=hit=1654687912665&t=4; EDGE_S=SID=23D67438C6C6693C20436585C7CF687B&mkt=en-pk; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wNi0wOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NH0=; OID=AhDVpqkihJaP_PUe8jzWqdXCfBQ1f-PeclDJ9Qs0kndCNTpOtfegeae_dT8N-SNgtH9-Vqr7Lu4JDsH4Lgc3GrSd; OIDI=AhDQtbLk5uXanVJygJlfqMj7xs5oZWaezyN5boYvGoDvzg; SRCHHPGUSR=SRCHLANGV2=en&BRW=XW&BRH=S&CW=1519&CH=150&DPR=1.25&UTC=300&DM=1&EXLTT=31&WTS=63765033202&HV=1654685068&SRCHLANG=en&SW=1536&SH=864&PV=10.0.0'})
        self.set_headers({'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
        self.set_headers({'referer':'https://www.bing.com/?q=something'})
        self.set_headers({'x-client-data':'eyIxIjoiMiIsIjIiOiIxIiwiMyI6IjAiLCI0IjoiNDcyMjcxOTg2MDMyMDU5NzQyNyIsIjUiOiJcImtKSjk0YTNEU2ZDeHEvZWNJYXlkVGswSFJXcVFzSEhOUDNjTjYvM0FYc3c9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjM4Mzk3MDA3NjI2MjYiLCI5IjoiZGVza3RvcCJ9'})
        self.set_headers({'ec-fetch-site':'same-origin'})
        self.set_headers({'sec-fetch-user':'?1'})
        self.set_headers({'cache-control': 'max-age=0'})'''
        #self.set_headers({'Host':'https://www.bing.com'})
        self.set_headers({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
        self.set_headers({'Accept-Language':'en-US,en;q=0.9'})
        self.set_headers({'Cache-Control':'max-age=0'})
        self.set_headers({'Cookie':'MUID=387DD974B44D621E1404D4E7B5996380; MUIDB=387DD974B44D621E1404D4E7B5996380; SRCHD=AF=S00028; SRCHUID=V=2&GUID=A729AD9F5A974C87AEEF35B2757E1F3C&dmnchg=1; ANON=A=0CAA0A2BE5471045C54E60F3FFFFFFFF&E=19dd&W=1; SRCHUSR=DOB=20190715&T=1641461861000&POEX=W; BFBUSR=BAWAS=1&BAWFS=1; BFB=AhCGUY1GNkLE-CueLG4N8NxFmRWriUkYLcFGJWz_eBxPj0ao0gTqnYHg4vWti2lSZHHQCQyqCp6Sl_tW097EE4tOawqlRuhTGl_463HQ7Rxn41hTQ5_FClIrHb6I_905u_BgxfkcQioFTYW6EZnAiC0rnm8Oc8cAaNQjM03i6lNUpQ; USRLOC=HS=1; UR=QS=0&TQS=0; SUID=A; WLS=C=1f23957445735855&N=Syed; SS=SID=23D67438C6C6693C20436585C7CF687B; U=1KqzpmU_icb8RNvTFGuuc2ojYuqFdaQ20bOEFBQdPIPaqRVHATsjyS-cvgYsgaJJXv79IWdLrSxMyVTxxc2rtsbMyevofQ77leArjSzKZyKby5InPwCYqntiV5jT6cX-AS5pSX_n3nMKeVF-cHTG67KlzKf7UYSrgZfcSD2XxJ7jOoYcFWh2Ta4NjzJI-buU6ETUCkz2HXeAVOyqbVm6tCw; ipv6=hit=1654687912665&t=4; EDGE_S=SID=23D67438C6C6693C20436585C7CF687B&mkt=en-pk; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wNi0wOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NH0=; OID=AhDVpqkihJaP_PUe8jzWqdXCfBQ1f-PeclDJ9Qs0kndCNTpOtfegeae_dT8N-SNgtH9-Vqr7Lu4JDsH4Lgc3GrSd; OIDI=AhDQtbLk5uXanVJygJlfqMj7xs5oZWaezyN5boYvGoDvzg; SRCHHPGUSR=SRCHLANGV2=en&BRW=XW&BRH=S&CW=1519&CH=150&DPR=1.25&UTC=300&DM=1&EXLTT=31&WTS=63765033202&HV=1654685068&SRCHLANG=en&SW=1536&SH=864&PV=10.0.0'})
        self.set_headers({'Referer':'https://https://www.bing.com/?toWww=1&redig=6956DB824D3E4512A06C4341A17DB523'})
        # self.set_headers({'Sec-Ch-Ua':' " Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"'})
        # self.set_headers({'Sec-Ch-Ua-Arch':' "x86"'})
        # self.set_headers({'Sec-Ch-Ua-Bitness':' "64"'})
        # self.set_headers({'Sec-Ch-Ua-Full-Version':' "102.0.1245.33"'})
        # self.set_headers({'Sec-Ch-Ua-Mobile':' ?0'})
        # self.set_headers({'Sec-Ch-Ua-Model':' ""'})
        # self.set_headers({'Sec-Ch-Ua-Platform':' "Windows"'})
        # self.set_headers({'Sec-Ch-Ua-Platform-Version':' "10.0.0"'})
        # self.set_headers({'Sec-Fetch-Dest':' document'})
        # self.set_headers({'Sec-Fetch-Mode':' navigate'})
        # self.set_headers({'Sec-Fetch-Site':' same-origin'})
        # self.set_headers({'Sec-Fetch-User':' ?1'})
        # self.set_headers({'Upgrade-Insecure-Requests':' 1'})
        # self.set_headers({'X-Client-Data':' eyIxIjoiMiIsIjIiOiIxIiwiMyI6IjAiLCI0IjoiNDcyMjcxOTg2MDMyMDU5NzQyNyIsIjUiOiJcImtKSjk0YTNEU2ZDeHEvZWNJYXlkVGswSFJXcVFzSEhOUDNjTjYvM0FYc3c9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjM4Mzk3MDA3NjI2MjYiLCI5IjoiZGVza3RvcCJ9'})
        # #self.set_headers({'Decoded':'message ClientVariations {{"1":"2","2":"1","3":"0","4":"4722719860320597427","5":"\"kJJ94a3DSfCxq/ecIaydTk0HRWqQsHHNP3cN6/3AXsw=\"","6":"stable","7":"3839700762626","9":"desktop"}}'})
        #self.set_headers({'X-Edge-Shopping-Flag':' 1'})

    def _selectors(self, element):
        '''Returns the appropriate CSS selector.'''
        selectors = {
            'url': 'a[href]', 
            'title': 'h2', 
            'text': 'p', 
            'links': 'ol#b_results > li.b_algo', 
            'next': 'div#b_content nav[role="navigation"] a.sb_pagN'
        }
        #print(selectors[element])
        return selectors[element]
    
    def _first_page(self):
        '''Returns the initial page and query.'''
        self._get_page(self._base_url)
        url = u'{}?q={}'.format(self._base_url,self._query)
        #print(url)
        url = url+'&qs=n&form=QBRE'
        #url += '{}'.format(self._query)
        #print(url)
        #url = u'{}/search?q={}&search=&form=QBLH'.format(self._base_url, self._query)
        #response = requests.head(url, allow_redirects=True,timeout=3.00)
        #print(redrt.url)
        #print(response.request.url)
        return {'url':url, 'data':None}
    
    def _next_page(self, tags):
        '''Returns the next page URL and post data (if any)'''
        selector = self._selectors('next')
        next_page = self._get_tag_item(tags.select_one(selector), 'href')
        url = None
        if next_page:
            url = (self._base_url + next_page) 
            url = url+'&qs=n&form=QBRE&sp=-1&pq=&sc=0-0&sk=&cvid=79821510679340B8A05F33CDC72475AC'
        return {'url':url, 'data':None}
        

     
