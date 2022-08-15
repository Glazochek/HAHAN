from django.db import models


class Mothers(models.Model):
    mom_like_id_user = models.PositiveIntegerField(verbose_name='лайки', default=0)
    mom_id = models.PositiveIntegerField(verbose_name='лайки', default=0)

    # def create(self, mid, umid):
    #     mom = Mothers.objects.create(mom_like_id_user=request.user.id, mom_id=mom)
    #     self.mom_id = mid
    #     self.mom_like_id_user = umid
    #     self.save()


class Read(models.Model):
    text = models.TextField(verbose_name='text', max_length=4048, blank=True)

