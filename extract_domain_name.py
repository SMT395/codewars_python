def domain_name(url):
    from urllib.parse import urlparse
    url=urlparse(url)
    # if the domain name loads into the netloc parsing list
    if len(url.netloc)!=0:
        url=url.netloc
        if "www." in url:
            url=url[url.find(".")+1:]
            url=url[:url.find(".")]
        else:
            url=url[:url.find(".")]
    #if the domain name loads into the path parsing list
    else:
        url=url.path
        if 'www.' in url:
            url=url[url.find(".")+1:]
            url=url[:url.find(".")]
        else:
            url=url[:url.find(".")]

    return url