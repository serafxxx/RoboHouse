from django.db import models

class rf24(models.Model):

    name = models.CharField(verbose_name='Sensor name', max_length=64, blank=True, default='')
    ip = models.GenericIPAddressField(verbose_name='IP address', protocol='IPv4')


    class Meta:
        abstract = True

    def __unicode__(self):
        if self.name:
            return '%s %s' % (self.name, self.ip, )
        else:
            return self.ip
