from django.contrib import admin
import nested_admin
from .models import Question, Profile, Solved
from .models import Tag, Tag1, Tag2, Tag3, Tag4, Tag5, Tag6, Tag7, Tag8, Tag9, Tag10, Tag11
# Register your models here.

#admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Solved)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('number_short', 'part', 'stage', 'year', 'grade', 'text_short', 'comment_short')

    def text_short(self, obj):
        return str(obj.text)[:30] + '...'
    text_short.short_description = 'ВОПРОС'

    def comment_short(self, obj):
        return str(obj.comment)[:20] + '...'
    comment_short.short_description = 'РАЗБОР'

    def number_short(self, obj):
        return str(obj.number)
    number_short.short_description = '№'
    number_short.admin_order_field = 'number'

admin.site.register(Tag1)
admin.site.register(Tag2)
admin.site.register(Tag3)
admin.site.register(Tag4)
admin.site.register(Tag5)
admin.site.register(Tag6)
admin.site.register(Tag7)
admin.site.register(Tag8)
admin.site.register(Tag9)
admin.site.register(Tag10)
admin.site.register(Tag11)


class PersonAdmin(admin.ModelAdmin):
    list_filter = (Question)
