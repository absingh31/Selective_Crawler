from urllib.parse import urlparse

def get_domain_name(link):       # Get Domain name
    try:
        results = fetch_sub_domain_name(link).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def fetch_sub_domain_name(link): # Time to get the subdomain
    try:
        return urlparse(link).netloc
    except:
        return ''
