def is_isbn(keyword):
    '''
    判断keyword是isbn还是key
    :param keyword:
    :return:
    '''
    if (len(keyword)==13 and keyword.isdigit()):
        return True
    short_keyword = keyword.replace("-",'')
    if '-' in keyword and short_keyword.isdigit() and len(short_keyword) == 10:
        return True
    return False