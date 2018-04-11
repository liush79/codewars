from collections import OrderedDict

def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url
    u, uri = url.split('?')
    params = uri.split('&')
    new_param = OrderedDict()
    for param in params:
        k, v = param.split('=')
        if k in new_param:
            continue
        new_param[k] = v
    for rm in params_to_strip:
        if rm in new_param:
            del new_param[rm]
    new_uri = ''
    for k, v in new_param.items():
        new_uri += '%s=%s&' % (k, v)
    result = '%s?%s' % (u, new_uri)
    return result[:-1]


print strip_url_params('www.codewars.com?a=1&b=2&a=2')
print strip_url_params('www.codewars.com?a=1&b=2&a=3')
print strip_url_params('www.codewars.com', ['b'])


