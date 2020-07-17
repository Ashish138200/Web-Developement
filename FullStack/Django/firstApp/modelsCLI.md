* First migrate:
```bash
python manage.py migrate
```
* For making new migrations
```bash
python manage.py makemigrations
```

* For applying changes for new migrations
```bash
python manage.py migrate
```
* For opening shell 
```bash
python manage.py shell
``` 
* For checking it's working fine
```bash
>>> from firstApp.models import Topic
>>> print(Topic.objects.all())
<QuerySet []>
>>> t = Topic(topName="Social network")
>>> t.save()
>>> print(Topic.objects.all())
<QuerySet [<Topic: Social network>]>
>>> quit()
```