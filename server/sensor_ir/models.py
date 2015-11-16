from datetime import datetime
from rf24.models import rf24
from django.db import models



class IRModule(rf24):
    def __unicode__(self):
        return self.name



class IRRemoute(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class IRCommand(models.Model):
    remoute = models.ForeignKey(IRRemoute, verbose_name='Remoute control', blank=True, null=True, default=None)
    name = models.CharField(max_length=64, default='', blank=True)
    encoding = models.CharField(verbose_name='Command encoding', max_length=64, default='')
    code = models.CharField(verbose_name='Command hex code', max_length=64, default='')
    created = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)

    def __unicode__(self):
        if self.remoute:
            return '%s %s [%s]' % (self.remoute.name, self.name, self.code)
        else:
            return '%s [%s]' % (self.name, self.code)
