"""
Search Book using google book api
import this library and call method 'search_item' with required parameters query and API_KEY
"""
import requests
import urllib

def search_item(query,API_KEY,language='en',max_result=5,**kwargs):
    url     = "https://www.googleapis.com/books/v1/volumes?"
    data    = urllib.urlencode({'q':query,'langRestrict':language,
                            'key':API_KEY})
    res     = requests.get(url+data)
    if res.status_code == 200:
        res = res.json()
        total_items = res[u'totalItems']
        print total_items
        items = res[u'items']
        result = [] #['link','title',publish_date','author','rating','image_link']
        for i in xrange(len(items)):
            item = items[i]
            data    = {}
            data[u'link'] = item[u'selfLink']
            vol_info = item[u'volumeInfo']
            try:
                data[u'title'] = vol_info[u'title']
            except:
                data[u'title'] = None
            try:
                data[u'author']= vol_info[u'authors']
            except:
                data[u'author']= None
            try:
                data[u'publish_date'] = vol_info[u'publishedDate']
            except:
                data[u'publish_date'] = None
            try:
                data[u'rating'] = vol_info[u'averageRating']
            except:
                data[u'rating'] = None
            try:
                data[u'image_link']=vol_info[u'imageLinks'][u'thumbnail']
            except:
                data[u'image_link']= None
            result.append(data)
        return result
    else:
        print res.status
        return None
    
