from flask import jsonify,request
from . import web
from app.lib.helper import is_isbn
from app.spiders.yushu_book import YuShuBook
from app.forms.book import SearchForm

@web.route('/book/search')
def search():
    '''
    :parameter：
        keyword 普通关键字 or isbn
        page分页
        1. ?传参 ?keyword=金庸&page=1
    :return: response
    '''
    form = SearchForm(request.args)
    if form.validate():
        keyword = form.keyword.data.strip()
        page = form.page.data
        if is_isbn(keyword):
            result = YuShuBook.search_by_isbn(keyword)
        else:
            result = YuShuBook.search_by_keyword(keyword, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    #return json.dumps(result),200, {'content-type':'application/json'}