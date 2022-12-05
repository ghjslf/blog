from django.contrib import admin

from articles.models import Article, Tag

admin.site.register(Article)
admin.site.register(Tag)

admin.site.site_header = 'Администрирование блога'
admin.site.index_title = 'Вся основная информация о блоге'